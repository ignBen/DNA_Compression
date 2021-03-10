from bitstring import BitArray

def compress(string):
	
	compressed_list = []

	prev = ''
	count = 1

	for char in string:
		if char != prev:
			if prev != '':
				compressed_list.append([count,prev])
			count = 1
			prev = char
		else:
			count += 1
	else:
		compressed_list.append([count,prev])

	max_size = 0
	for item in compressed_list:
		if item[0] > max_size:
			max_size = item[0]

	max_bit_lenght = len(bin(max_size)[2:])

	compressed_binary_string = ""

	for item in compressed_list:
		count = ("{:0%db}" % max_bit_lenght).format(item[0])
		key = [bin(ord(x))[2:].zfill(8) for x in item[1]][0]
		compressed_binary_string += count+key

	compressed_binary_string = "{:08b}".format(max_bit_lenght) + compressed_binary_string

	no_padding_bits_dec = (8-((len(compressed_binary_string)+3)%8))%8 #data stored in bytes so add calculate number of padding bits needed
	no_padding_bits_bin = "{:03b}".format(no_padding_bits_dec) #max number of padding bits can be 7 so store this in 3 bits 

	compressed_binary_string = no_padding_bits_bin + compressed_binary_string + (no_padding_bits_dec*'0') # add the number of padding bits, data, padding bits 

	binary_string = BitArray(bin=compressed_binary_string)

	return binary_string




		


