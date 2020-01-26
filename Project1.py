from pymd5 import md5, padding

def get_encoding_length(length):
	return (length + len(padding(length * 8))) * 8

eight = "abcdefgh"
m = "Use HMAC, not hashes"
x = "Good advice"

h = md5()
h.update(eight) # Add the 8 byte code with padding
h = md5(state=bytes.fromhex(h.hexdigest()), count=get_encoding_length(len(eight))) # Get the hexdigest and length
h.update(m) # Add the actual message
print("Original Hex:", h.hexdigest())

# This should be the same as the previous hexdigest
h2 = md5()
h2.update(eight.encode() + padding(len(eight)*8) + m.encode())
print("Original Hex:", h2.hexdigest())

# Guess the length of the encoded message
bits = get_encoding_length(len(eight)) + get_encoding_length(len(m))
h3 = md5(state=bytes.fromhex(h.hexdigest()), count=bits) # Input the token from the message
h3.update(x) # Add in the malicious message
print("New Hex:", h3.hexdigest())

# This should be the same as the previous hexdigest
h2 = md5()
h2.update(eight.encode() + padding(len(eight)*8) + m.encode() + padding(len(m)*8) + x.encode())
print("New Hex2:", h2.hexdigest())