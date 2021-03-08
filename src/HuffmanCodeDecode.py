import struct

def decode(file, dic):
	binary = ""
	for byte in file.read():
		binary += (bin(byte)[2:])

	print(binary)

	# text = ""
	# for item in dic:
	# 	if binary.startswith(item):
	# 		print('Hello')
