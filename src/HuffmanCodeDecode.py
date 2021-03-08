from bitstring import BitArray
import struct

def decode(file, dic):
	binary = str(BitArray(file.read()).bin)

	text = ""
	while len(binary) > 0:
		for item in dic:
			if binary.startswith(dic[item]):
				text += item
				binary = binary[len(dic[item]):]
				print('Hello')

	return text