from bitstring import BitArray

def decode(file):
	file = file.read()

	binary = BitArray(file).bin
	total_bits = len(binary)

	padding_bits = (int(str(binary[:3]),2)) #first 3 bits identify number of padding bits
	if padding_bits > 0:
		binary = binary[:-padding_bits] #remove padding bits
	binary = binary[3:] #remove bits identifying number of padding bits

	count_len = int(str(binary[:8]),2)
	binary = binary[8:]


	text = ""

	while binary:
		count = int(str(binary[:count_len]),2)
		binary = binary[count_len:]

		char = chr(int(str(binary[:8]),2))
		binary = binary[8:]

		text += char*count
		print(total_bits-(len(binary)),"/",total_bits,"bits decoded")

	return text