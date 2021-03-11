"""Implementation of Run-Length compression in python3"""

from bitstring import BitArray

def compress(string):
	"""encodes the text file and turns it into the compressed binary string

	Keyword arguments:
	file -- compressed file (required)
	"""
	
	compressed_list = []

	prev = '' 
	count = 1

	for char in string: 
		if char != prev:
			if prev != '': # if new item 
				compressed_list.append([count,prev]) # add to list
			# if different character
			count = 1
			prev = char
		else: # if character already in list
			count += 1
	else: 
		compressed_list.append([count,prev])

	# get the maximum run length
	max_size = 0
	for item in compressed_list:
		if item[0] > max_size:
			max_size = item[0]

	max_bit_lenght = len(bin(max_size)[2:]) 

	compressed_binary_string = ""

	for item in compressed_list:
		count = ("{:0%db}" % max_bit_lenght).format(item[0]) # turn count into binary string of max_bit_length in length
		key = [bin(ord(x))[2:].zfill(8) for x in item[1]][0] # turn char into binary
		compressed_binary_string += count+key # add to compress string

	compressed_binary_string = "{:08b}".format(max_bit_lenght) + compressed_binary_string # add length of each count to start for decompression

	no_padding_bits_dec = (8-((len(compressed_binary_string)+3)%8))%8 #data stored in bytes so add calculate number of padding bits needed
	no_padding_bits_bin = "{:03b}".format(no_padding_bits_dec) #max number of padding bits can be 7 so store this in 3 bits 

	compressed_binary_string = no_padding_bits_bin + compressed_binary_string + (no_padding_bits_dec*'0') # add the number of padding bits, data, padding bits 

	binary_string = BitArray(bin=compressed_binary_string)

	return binary_string




		


