import json
import HuffmanCode

with open("cfg/config.json", "r") as j:
	config = json.load(j)

input_file = open("cfg/"+config["input_text"],"r")
input_string = ""
for line in input_file:
	input_string += line

freq = HuffmanCode.calculate_freq(input_string)
nodes = HuffmanCode.generate_nodes(freq)
binary = HuffmanCode.generate_binary_tree(nodes[0][0])
binary_string = HuffmanCode.convert_binary(binary, input_string)


def _to_Bytes(data):
	b = bytearray()
	for i in range(0, len(data), 8):
		b.append(int(data[i:i+8], 2))
	return bytes(b)

output_string = binary_string
output_string = _to_Bytes(output_string)

with open("cfg/"+config["compressed_text"],"wb") as output_file:
	output_file.write(output_string)


