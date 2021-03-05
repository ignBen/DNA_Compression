class HuffmanCode:

	class Tree:
		def __init__(self,data):
			self.left = None
			self.right = None

		def child(self):
			return self.right,self.left

	def calculate_freq(string):
		freq = {}

		for char in string:
			if char in freq:
				freq[char] += 1
			else:
				freq[char] = 1

		freq = dict(sorted(freq.items(), key=lambda item: item[1]))
		return freq