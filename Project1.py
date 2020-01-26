from pymd5 import md5, padding
m = "Use HMAC, not hashes"
h = md5()
h.update(m)
print(h.hexdigest())
bits = (len(m) + len(padding(len(m) * 8))) * 8
h = md5(state=bytes.fromhex("3ecc68efa1871751ea9b0b1a5b25004d"), count=bits)
x = "Good advice"
print(h.hexdigest())
h.update(x)
print(h.hexdigest())


h2 = md5()
h2.update(m.encode() + padding(len(m)*8) + x.encode())
print(h2.hexdigest())