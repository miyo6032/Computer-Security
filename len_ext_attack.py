import sys
from pymd5 import md5, padding
import re
from urllib.parse import quote, unquote

def get_encoding_length(length):
	return (length + len(padding(length * 8))) * 8

if len(sys.argv) >= 2:
	original_link = quote(sys.argv[1])
	print(original_link)
	result = re.search(r'command%3D.*', original_link) # Find the original message
	if(result != None):
		message = original_link[result.start():] # Convert to string
		message_length = len(message)
		passcode_length = 8
		
		bits = get_encoding_length(passcode_length) + get_encoding_length(message_length)
		h = md5(state=bytes.fromhex("7976a258772fe07d857fef32a19ed611"), count=bits)
		malicious_message = quote("&command=UnlockSafes")
		print(h.hexdigest())
		h.update(malicious_message)
		new_token = h.hexdigest()

		print("\n")
		print("New Token:", new_token)
		print("\n")
		print("Message:", message)
		print("\n")
		print("New Message", malicious_message)
		print("\n")
		# Substitute new token and the new message into the url
		print(unquote(re.sub(r'api\?token=.*$', "api?token={}&{}{}".format(new_token, message, malicious_message), unquote(original_link))))