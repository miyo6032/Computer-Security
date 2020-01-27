#!/usr/bin/python3

import sys
from collections import Counter
import numpy as np

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

input = """ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletot
hinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedt
ocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolate
thelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesev
enprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpuls
ioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacya
ndpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawf
ullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandab
useactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisi
soneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindou
btwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoft
echnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper""".replace("\n", "").replace(" ", "").upper()


def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    # cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()

    #################################################################
    # Your code to determine the key and decrypt the ciphertext here

    index_to_letter = {i: alphabet[i] for i in range(26)}
    letter_to_index = {alphabet[i]: i for i in range(26)}

    def encrypt(key, plaintext):
        key = key.upper()
        text = ""
        for i in range(len(plaintext)):
            adjustment = letter_to_index[key[i % len(key)]]
            letter = index_to_letter[(letter_to_index[plaintext[i]] + adjustment) % 26]
            text += letter
        return text

    def text_multiples(ciphertext, start, jump):
        text = ""
        for i in range(start, len(ciphertext), jump):
            text += ciphertext[i]
        return text;

    def calculate_caesar_mean(key_length, ciphertext):
        variances = []
        for j in range(key_length):
            variances.append(pop_var(text_multiples(ciphertext, j, key_length)))
        return np.mean(variances)

    def find_key_length(ciphertext):
        variances = [calculate_caesar_mean(i, ciphertext) for i in range(2, 14)]
        return variances.index(max(variances)) + 2

    # Finds the letter offset that matches the frequencies above the best
    def match_frequencies(letter_frequencies):
        variances = []
        for i in range(26):
            offset_frequencies = { index_to_letter[(letter_to_index[key] - i) % 26]: freq for key, freq in letter_frequencies.items() }
            variance = np.mean([(freq - letter_freqs[key])**2 for key, freq in offset_frequencies.items()])
            variances.append(variance)
        return variances.index(min(variances))

    def find_key(ciphertext):
        key_length = find_key_length(ciphertext)
        key = ""
        for i in range(key_length):
            text = text_multiples(ciphertext, i, key_length)
            letter_frequencies = { char: len(list(filter(lambda c: c == char, text))) / len(text) for char in text }
            key += index_to_letter[match_frequencies(letter_frequencies)]
        return key

    # print(pop_var(encrypt("z", input)))          
    # print(pop_var(encrypt("yz", input)))
    # print(pop_var(encrypt("xyz", input)))
    # print(pop_var(encrypt("wxyz", input)))
    # print(pop_var(encrypt("vwxyz", input)))
    # print(pop_var(encrypt("uvwxyz", input)))
    # print(pop_var(letter_freqs))
    ciphertext = encrypt("antelopes", input)
    print(find_key(ciphertext))


