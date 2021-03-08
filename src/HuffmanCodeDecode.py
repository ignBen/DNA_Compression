from bitstring import BitArray
import struct

def decode(file, dic):
	file = file.read()

	binary = BitArray(file).bin
	padding_bits = (int(str(binary[:3]),2))

	binary = binary[3:-padding_bits]

	text = ""
	while binary:
		for item in dic:
			if binary.startswith(dic[item]):
				text += item
				binary = binary[len(dic[item]):]
	return text