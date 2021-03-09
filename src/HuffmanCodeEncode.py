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

	no_padding_bits_dec = 8-((len(binary_string)+3)%8)
	no_padding_bits_bin = "{:03b}".format(no_padding_bits_dec)

	binary_tree = encoded_huffman_tree(tree)

	binary_string = no_padding_bits_bin + binary_string + (no_padding_bits_dec*'0')

	binary_string = BitArray(bin=binary_string)

	return binary_string

def inc_binary(x):
	if len(x) == 0:
		return x

	if x[-1] == '0':
		x = x[:-1] + '1'
	else:
		x = inc_binary(x[:-1]) + '0'

	return x

	
def encoded_huffman_tree(tree):
	tree = dict(sorted(tree.items(), key=lambda item: item[0])) #Sort alphabetically
	tree = sorted(tree.items(), key=lambda item: len(item[1])) #Sort by length of code

	tree[0] = [tree[0][0],len(tree[0][1])*'0']

	count = 1
	while count < len(tree):
		new = [tree[count][0],inc_binary(tree[count-1][1])]
		if len(tree[count-1][1]) < len(tree[count][1]):
			new[1] += (len(tree[count][1]) - len(tree[count-1][1]))*'0'
		tree[count] = new
		count += 1
	
	print(tree)



	
	
