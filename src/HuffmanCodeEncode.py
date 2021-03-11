"""Implementation of HuffmanCode compression in python3"""

from bitstring import BitArray
from Node import *

def generate_freq(string):
	"""From a given input string generates the freqencies of characters

	Keyword arguments:
	string -- input string (required)
	"""
	freq = {} #Frequency dictionary

	for char in string:
		if char in freq:
			freq[char] += 1 #increment character if already in tree
		else:
			freq[char] = 1 #add character if not already in tree

	#Sort dictionary by freq
	freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
	
	return freq

def generate_nodes(freq):
	"""Creates the binary tree using nodes. To create a node for Huffman
	We only need to point to the two connecting nodes. We sort these nodes by
	freqency as stated in specification of HuffmanCode

	Keyword arguments:
	freq -- dictionary of frequencies of input string (required)
	"""
	
	nodes = freq

	while len(nodes) > 1:
		key1, freq1 = nodes[-1] #take the last key,freqency (or node, freq)
		key2, freq2 = nodes[-2] #take the second to key,freqency (or node, freq)
		nodes = nodes[:-2] #remove the above key,freqency (or node,freq) from dictionary
		node = Node(key1, key2) #generate new parent node pointing to two child nodes of freqency key1,key2
		nodes.append((node, freq1 + freq2)) # add this new node to end of tree
	
		#each iteration sort new nodes in decending order	
		nodes = sorted(nodes, key=lambda item: item[1], reverse=True)
	
	return nodes

def generate_huffman_table(node, binary=''):
	"""Creates the huffman dictionary containg each key, with it corresponding
	code. Traverses the tree and records wether a node is left or right (0 or 1)
	once final node is hit, the {key: code} is returned

	Keyword arguments:
	node -- the starting node in the tree (required)
	binary -- the current huffman binary code for that speific treversal state (default None)
	"""
	
	if type(node) is str:
		return {node: binary} #if end of tree is reached return generated huffman code

	tree = {}
	left,right = node.get_nodes() 
	tree.update(generate_huffman_table(left, binary + '0')) #traverse the left hand side of the tree
	tree.update(generate_huffman_table(right, binary + '1')) #traverse the right hand side of the tree 
	
	return tree

def convert_binary_data(tree, input_string):
	"""Converts the input string into a string of binary using
	the huffman tree generated prevoiusly.
	Padding and the encoded tree is concatonated here also.

	Keyword arguments:
	tree -- huffman tree (required)
	input_string -- the string, i.e contents of file (required)
	"""

	binary_string = '' #string of binary characters to be written to compressed file
	for char in input_string: 
		binary_string += tree[char] #for each character append corresponding huffman code to binary_string

	binary_tree = encoded_huffman_tree(tree) #generate the encoded huffman tree (in binary)
	binary_string = binary_tree	+ binary_string #add this infront of the data so that it can be regerated

	no_padding_bits_dec = (8-((len(binary_string)+3)%8))%8 #data stored in bytes so add calculate number of padding bits needed
	no_padding_bits_bin = "{:03b}".format(no_padding_bits_dec) #max number of padding bits can be 7 so store this in 3 bits 

	binary_string = no_padding_bits_bin + binary_string + (no_padding_bits_dec*'0') # add the number of padding bits, data, padding bits

	binary_string = BitArray(bin=binary_string) #turn into byte array that can be written to .bin file

	return binary_string
	
def encoded_huffman_tree(tree):
	"""Converts the huffman tree into a binary format that can be read back
	and used to regerate the tree during decompression.

	Keyword arguments:
	tree -- huffman tree (required)	"""

	binary_string = '' #huffman tree in binary form stored as string
	no_keys = 0 #count number of item in huffman tree, needed for decompression
	for item in tree:
		key = [bin(ord(x))[2:].zfill(16) for x in item][0] #convert each key into 16 bit ascii
		no_bits = "{:08b}".format(len(tree[item])) #convert the number of bits used for each huffman code to binary
		code = tree[item] #get huffman code
		no_keys +=1
		binary_string += key+no_bits+code #item in tree is stored as | key | length of code | code | 

	no_keys = "{:08b}".format(no_keys) #number of items in huffman tree in binary form

	binary_string = no_keys+binary_string 

	return binary_string
		



	
	
