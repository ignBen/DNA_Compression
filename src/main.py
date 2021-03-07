import json
from HuffmanCode import *

with open("cfg/config.json", "r") as j:
	config = json.load(j)

input_file = open("cfg/"+config["input_text"],"r")
input_string = ""
for line in input_file:
	input_string += line

freq = HuffmanCode.calculate_freq(input_string)
nodes = HuffmanCode.generate_nodes(freq)
tree = HuffmanCode.generate_tree(nodes)

