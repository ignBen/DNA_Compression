tree = dict(sorted(tree.items(), key=lambda item: item[0])) #Sort alphabetically
	tree = sorted(tree.items(), key=lambda item: len(item[1])) #Sort by length of code

	tree[0] = [tree[0][0],len(tree[0][1])*'0']

	count = 1
	while count < len(tree):
		new = [tree[count][0],inc_binary(tree[count-1][1])]
		if len(tree[count-1][1]) < len(tree[count][1]):
			new[1] += (len(tree[count][1]) - len(tree[count-1][1]))*'0'
		tree[count] = new
		count += 1

	# code := 0
	# while more symbols do
 	#    	print symbol, code
 	#    	code := (code + 1) << ((bit length of the next symbol) − (current bit length))

 	
	
	print(tree)