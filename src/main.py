import json
import sys
import os
import HuffmanCodeEncode
import HuffmanCodeDecode


def menu():

	try:
		file1 = sys.argv[1]
		file2 = sys.argv[2]
	except:
		print('Invalid Files')
		exit()

	if file1.split('.')[1] == 'txt' and file2.split('.')[1] == 'bin':
		tree = HuffmanCodeCompress(file1, file2)
		compare_sizes(file1,file2)
		# HuffmanCodeDecompress(file2, file1, tree)
	elif file1.split('.')[1] == 'bin' and file2.split('.')[1] == 'txt':
		# HuffmanCodeDecompress(file1, file2)
		pass
	else:
		print('Invalid Files')
		exit()


def HuffmanCodeCompress(file_text, file_bin):

	input_file = open("../files/"+file_text,"r")
	input_string = ""
	for line in input_file:
		input_string += line


	freq = HuffmanCodeEncode.generate_freq(input_string)
	nodes = HuffmanCodeEncode.generate_nodes(freq)
	tree = HuffmanCodeEncode.generate_binary_tree(nodes[0][0])

	binary_data = HuffmanCodeEncode.convert_binary_data(tree, input_string)
	binary_tree = HuffmanCodeEncode.convert_binary_tree(tree)
	print(binary_tree)

	with open("../files/"+file_bin,"wb") as output_file:
		binary_data.tofile(output_file)

	return tree

def HuffmanCodeDecompress(file_bin, file_text, tree):
	with open("../files/"+file_bin,"rb") as compressed_file:
		result = HuffmanCodeDecode.decode(compressed_file, tree)

	print(result)

def compare_sizes(file1,file2):
	o = os.path.getsize("../files/"+file1)
	c = os.path.getsize("../files/"+file2)

	print("\nOriginal file: {} bytes".format(o))
	print("Compressed file: {} bytes".format(c))
	print("Compressed file {}% of percent of Original\n".format(round((((c/o)*100)))))

menu()