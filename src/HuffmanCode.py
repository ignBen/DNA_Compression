from Node import *

class HuffmanCode:

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

	def generate_tree(nodes):
		tree = {}
		for node in nodes:
			left,right = node[0].get_nodes()
			if type(left) is not str and type(right) is not str:
				tree.update((left, binary + '0'))
				tree.update((right, binary + '1'))
				print(tree)

