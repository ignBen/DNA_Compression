"""Implementation of HuffmanCode decompression in python3"""

from bitstring import BitArray

def decode(file):
	"""Decode the compressed file

	Keyword arguments:
	file --  compressed file (required)
	"""

	file = file.read()

	binary = BitArray(file).bin
	total_bits = len(binary)

	#drop padding bits
	padding_bits = (int(str(binary[:3]),2)) #first 3 bits identify number of padding bits
	if padding_bits > 0:
		binary = binary[:-padding_bits] #remove padding bits
	binary = binary[3:] #remove bits identifying number of padding bits

	#regerate tree
	dic = {}
	no_keys = (int(str(binary[:8]),2)) #first 8 bits identify number of items in huffman tree
	binary = binary[8:] #remove bits identifiying number of items

	for i in range(0,no_keys): #for number of items in huffman tree
		key = chr(int(str(binary[:16]),2)) #first 16 characters is key
		binary = binary[16:] #remove key

		no_bits = int(str(binary[:8]),2) #first 8 characters identifis number of bits huffman code uses
		binary = binary[8:] #remove no_bits

		code = binary[:no_bits] #first no_bits is the huffman code
		binary = binary[no_bits:] #remove huffman code

		dic.update({key: code}) #add the decoded key and code to new huffman tree

	#itterate through text to regenerate text from decoded huffman tree

	text = ""
	while binary:
		for item in dic:
			if binary.startswith(dic[item]): # if starts with huffman code add this to decoded text
				text += item
				binary = binary[len(dic[item]):] # remove these deocded bits from start of binary string 
		print(total_bits-(len(binary)),"/",total_bits,"bits decoded") # output number of bits ramaining for decompression

	return text