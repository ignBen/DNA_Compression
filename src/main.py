import json
import os
import HuffmanCodeEncode
import HuffmanCodeDecode

with open("../cfg/config.json", "r") as j:
	config = json.load(j)


def menu():
	while True:
		print("---Text file to be compressed: \'"+config["input_text"]+"\'---\n")
		print("1. Compressed File")
		print("2. Decompress File")
		print("0. Close")
		user_input = int(input())


		if user_input == 1:
			decode = HuffmanCodeCompress()
			compare_sizes(config["input_text"])
			# HuffmanCodeDecompress(decode)

		elif user_input == 2:
			pass

		elif user_input == 0:
			exit()


def HuffmanCodeCompress():

	input_file = open("../files/"+config["input_text"],"r")
	input_string = ""
	for line in input_file:
		input_string += line


	freq = HuffmanCodeEncode.generate_freq(input_string)
	nodes = HuffmanCodeEncode.generate_nodes(freq)
	tree = HuffmanCodeEncode.generate_binary_tree(node[0][0])
	
	binary_data = HuffmanCodeEncode.convert_binary_data(tree, input_string)
	binary_tree = HuffmanCodeEncode.convert_binary_tree(tree)

	with open("../files/"+config["input_text"].split('.')[0]+".bin","wb") as output_file:
		binary.tofile(output_file)

	return tree

def HuffmanCodeDecompress(decode):
	with open("../files/"+config["input_text"].split('.')[0]+".bin","rb") as compressed_file:
		result = HuffmanCodeDecode.decode(compressed_file, decode)

	print(result)

def compare_sizes(file):
	o = os.path.getsize("../files/"+file)
	c = os.path.getsize("../files/"+file.split('.')[0]+".bin")

	print("\nOriginal file: {} bytes".format(o))
	print("Compressed file: {} bytes".format(c))
	print("Compressed file {}% of percent of Original\n".format(round((((c/o)*100)))))

menu()