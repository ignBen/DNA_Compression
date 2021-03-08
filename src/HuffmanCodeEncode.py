from Node import *

def calculate_freq(string):
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

def convert_binary(binary, input_string):
	output_string = ''
	for char in input_string:
		output_string += binary[char]

	print(output_string)

	return int(output_string, 2).to_bytes((len(output_string) + 7) // 8, byteorder='big')
