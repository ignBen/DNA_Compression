from bitstring import BitArray
import struct

def decode(file, dic):
	binary = BitArray(file.read()).bin
	print(binary)

	# text = ""
	# for item in dic:
	# 	if binary.startswith(item):
	# 		print('Hello')
