from bitstring import BitArray
from Node import *

def generate_freq(string):
	freq = {}

	for char in string:
		if char in freq:
			freq[char] += 1
		else:
			freq[char] = 1

	freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
	
	return freq

def generate_nodes(freq):
	
	nodes = freq

	while len(nodes) > 1:
		key1, freq1 = nodes[-1]
		key2, freq2 = nodes[-2]
		nodes = nodes[:-2]
		node = Node(key1, key2)
		nodes.append((node, freq1 + freq2))
		
		nodes = sorted(nodes, key=lambda item: item[1], reverse=True)
	
	return nodes

def generate_binary_tree(node, binary=''):
	
	if type(node) is str:
		return {node: binary}

	tree = {}
	left,right = node.get_nodes()
	tree.update(generate_binary_tree(left, binary + '0'))
	tree.update(generate_binary_tree(right, binary + '1'))
	
	return tree

def convert_binary_data(tree, input_string):
	binary_string = ''
	for char in input_string:
		binary_string += tree[char]

	binary_tree = encoded_huffman_tree(tree)
	binary_string = binary_tree	+ binary_string

	no_padding_bits_dec = (8-((len(binary_string)+3)%8))%8
	no_padding_bits_bin = "{:03b}".format(no_padding_bits_dec)

	binary_string = no_padding_bits_bin + binary_string + (no_padding_bits_dec*'0')

	binary_string = BitArray(bin=binary_string)

	return binary_string
	
def encoded_huffman_tree(tree):
	binary_string = ''
	no_keys = 0
	for item in tree:
		key = [bin(ord(x))[2:].zfill(16) for x in item][0]
		no_bits = "{:08b}".format(len(tree[item]))
		code = tree[item]
		no_keys +=1
		binary_string += key+no_bits+code

	no_keys = "{:08b}".format(no_keys)


	binary_string = no_keys+binary_string

	return binary_string
		



	
	
