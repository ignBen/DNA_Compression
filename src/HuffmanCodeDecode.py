from bitstring import BitArray

def progress_bar(binary_start_len, binary_len):
	print("\n"*100)
	percent = round((binary_len/binary_start_len) * 100)
	print("[%s] | %d%%" % ("="*round(10-(percent/10)), percent))


def decode(file):
	file = file.read()

	binary = BitArray(file).bin
	binary_start_len = len(binary)

	#drop padding bits
	padding_bits = (int(str(binary[:3]),2))
	binary = binary[3:-padding_bits]

	#regerate tree
	dic = {}
	no_keys = (int(str(binary[:8]),2))
	binary = binary[8:]

	for i in range(0,no_keys):
		key = chr(int(str(binary[:16]),2))
		binary = binary[16:]

		no_bits = int(str(binary[:8]),2)
		binary = binary[8:]

		code = binary[:no_bits]
		binary = binary[no_bits:]

		dic.update({key: code})
	print(dic)

	progress_bar(binary_start_len,len(binary))


	text = ""
	while binary:
		for item in dic:
			if binary.startswith(dic[item]):
				text += item
				binary = binary[len(dic[item]):]
				progress_bar(binary_start_len,len(binary))
	return text