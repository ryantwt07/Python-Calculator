def matrix_2_2_input():
	cmd = int(input('''
	Enter 1 for 2 X 2 Matrix
	>>> '''))
	if cmd == 1:
		n11 = float(input("Enter the element of the 1st column and 1st row of the 1st matrix: "))
		n12 = float(input("Enter the element of the 2nd column and the 1st row of the 1st matrix: "))
		n21 = float(input("Enter the element of the 1st column and 2nd row of the 1st matrix: "))
		n22 = float(input("Enter the element of the 2nd column and the 2nd row of the 1st matrix: "))
		m11 = float(input("Enter the element of the 1st column and 1st row of 2nd matrix: "))
		m12 = float(input("Enter the element of the 2nd column and 1st row of 2nd matrix: "))
		m21 = float(input("Enter the element of the 2nd column and 1st row of 2nd matrix: "))
		m22 = float(input("Enter the element of the 2nd column and 2nd row of 2nd matrix: "))
	else:
		print("Invalid Request")

def matrix_2_2_calculate():
	X = [[n11, n12], [n21, n22]]
	Y = [[m11, m12], [m21, m22]]
	result = [[0, 0], [0, 0]]
	for i in range(len(x)):
		for j in range(len(X[0])):
			result[i][j] = X[i][j] + Y[i][j]
	for r in result:
		print(r)
