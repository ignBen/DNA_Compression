"""
Main module for running Huffman Compression and Decompression
Gives comparison infomration on compressed files upon successfull compression
"""

import sys
import os
import HuffmanCodeEncode
import HuffmanCodeDecode
from time import time


def menu():
	"""Handler for diciding if request is compression or decompression"""

	try:
		file1 = sys.argv[1]
		file2 = sys.argv[2]
	except:
		print('Invalid Files')
		exit()

	if file1.split('.')[-1] == 'txt' and file2.split('.')[-1] == 'bin':
		time_start = time()

		HuffmanCodeCompress(file1, file2)
		compare_sizes(file1,file2)

		time_end = time()
		time_to_complete = time_end - time_start
		print(round(time_to_complete, 4), "Seconds to compress\n") # output time in seconds for compression to complete

	elif file1.split('.')[-1] == 'bin' and file2.split('.')[-1] == 'txt':
		time_start = time()

		HuffmanCodeDecompress(file1, file2)

		time_end = time()
		time_to_complete = time_end - time_start
		print(round(time_to_complete, 4), "Seconds to decompress\n") # output time in seconds for decompression to complete
	else:
		print('Invalid Files')
		exit()


def HuffmanCodeCompress(file_text, file_bin):
	"""Runs the HuffmanCode compression module in seperate parts.
	This was done to help with debugging

	Keyword arguments:
	file_text -- input text file (required)
	file_bin -- output binary file name (required)
	"""

	input_file = open("../files/"+file_text,"r")
	input_string = ""
	for line in input_file:
		input_string += line

	time_start = time()
	freq = HuffmanCodeEncode.generate_freq(input_string)
	nodes = HuffmanCodeEncode.generate_nodes(freq)
	tree = HuffmanCodeEncode.generate_binary_tree(nodes[0][0])

	binary_data = HuffmanCodeEncode.convert_binary_data(tree, input_string)

	with open("../files/"+file_bin,"wb") as output_file:
		binary_data.tofile(output_file)



def HuffmanCodeDecompress(file_bin, file_text):
	"""Runs decode on binary file compressed using this programs
	implementation of HuffmanCoding

	Keyword arguments:
	file_bin -- input text file (required)
	file_text -- output text file name (required)
	"""
	with open("../files/"+file_bin,"rb") as compressed_file:
		result = HuffmanCodeDecode.decode(compressed_file)

	with open("../files/"+file_text,'w') as new_file:
		new_file.write(result)

def compare_sizes(file1,file2):
	o = os.path.getsize("../files/"+file1)
	c = os.path.getsize("../files/"+file2)

	print("\nOriginal file: {} bytes".format(o))
	print("Compressed file: {} bytes".format(c))
	print("Compressed file {}% of percent of original".format(round((((c/o)*100)))))

menu()