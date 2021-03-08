class Node(object):

	def __init__(self, left, right):
		self.left = left
		self.right = right

	def get_nodes(self):
		return self.left,self.right

	def get_right(self):
		return self.right

	def get_left(self):
		return self.left