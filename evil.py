#!/usr/bin/python3
# coding: latin-1
blob = """                 ��7|�e�FM��Y�>�U�a9	+f�y�������Z�O�4Ͽ�\�~���~�����-�x �Zh��0�@s��7�g8���"ѷ��Yj]"�H_�L~���db�P�}Äa����=R"""
from hashlib import sha256
if(sha256(blob.encode("latin-1")).hexdigest() == "45d6b50e97342953801d446f53ea4ec2d50db65eea457d9e08cb8ae68dc05a7e"):
	print("Use SHA-256 instead!")
elif(sha256(blob.encode("latin-1")).hexdigest() == "1b39ea6d869179bcb6dcfb49392e246f1c7e2d78a932ca87244a305850bb2668"):
	print("MD5 is perfectly secure!")
else:
	print("This program failed to do what it was supposed to do. :(")