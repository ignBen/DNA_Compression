"""Implementation of Run-Length decompression in python3"""

from bitstring import BitArray

def decode(file):
	"""decodes the binary file and turns it into the origonal string

	Keyword arguments:
	file -- compressed file (required)
	"""

	file = file.read() # Read file

	binary = BitArray(file).bin # Turn into binary string
	total_bits = len(binary)

	padding_bits = (int(str(binary[:3]),2)) #first 3 bits identify number of padding bits
	if padding_bits > 0:
		binary = binary[:-padding_bits] #remove padding bits
	binary = binary[3:] #remove bits identifying number of padding bits

	count_len = int(str(binary[:8]),2) # get the length of bits that that store the count
	binary = binary[8:] # remove these bits


	text = ""

	while binary: # while there are stil bits left in binary string
		count = int(str(binary[:count_len]),2) # get the count
		binary = binary[count_len:] # remove count from binary

		char = chr(int(str(binary[:8]),2)) # get character
		binary = binary[8:] # remove character from binary

		text += char*count # add character to text count times
		print(total_bits-(len(binary)),"/",total_bits,"bits decoded") # print decode progress

	return text