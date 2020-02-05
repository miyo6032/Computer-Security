import sys
from pymd5 import md5, padding
import re
from urllib.parse import quote

def get_encoding_length(length):
	return (length + len(padding(length * 8))) * 8

if len(sys.argv) >= 2:
	original_link = sys.argv[1]

	result = re.search(r'command=.*', original_link) # Find the original message
	token_result = re.search(r'token=.*', original_link) # Find original token
	if(result != None and token_result != None):
		message = original_link[result.start():]
		old_token = original_link[token_result.start() + 6:token_result.start() + 6 + 32]
		message_length = len(message)
		secret_length = 8 # Assumption that the secret is always 8 bytes
		
		bits = get_encoding_length(secret_length + message_length) # Calculate bit position of message and padding
		h = md5(state=bytes.fromhex(old_token), count=bits)
		malicious_message = "&command=UnlockSafes"
		h.update(malicious_message)
		new_token = h.hexdigest() # Get our new token, which is secret||message||pad_m||x||pad_x

		# Format the link to match secret||message||pad_m||x
		previous_padding = quote(padding((message_length + secret_length) * 8))
		subbed_link = re.sub(r'token=.*$', "token=" + new_token + "&" + message + previous_padding + malicious_message, original_link)

		print(subbed_link)