from bitstring import BitArray
import struct

def decode(file, dic):
	file = file.read()

	binary = BitArray(file).bin
	print(binary)

	text = ""
	while binary:
		for item in dic:
			if binary.startswith(dic[item]):
				text += item
				binary = binary[len(dic[item]):]


	return text