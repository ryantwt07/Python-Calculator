# ---- VARIABLES ---- #

pi = 0
maincmd = 0
cmd = 0
in1 = 0
in2 = 0
num1 = 0
num2 = 0
answer = 0

# ---- ERROR (IMPORT) ---- #

def error_message(error_num):
	print("Unable to Proceed with Request. Analysing Error...")
	if error_num == 0:
		print("400: Console Import Module Failure.")
	elif error_num == 1:
		print("401: Math Import Module Failure.")

# ---- IMPORTS ----- # 

try:
	import console
except ImportError:
	error_message(0)
else:
	try:
		console.clear()
		import math
		from math import pi
	except ImportError:
		error_message(1)
	else:
		print("Import Success!")

# ---- DEFINITIONS ---- #

def work_in_progress():
	print("This function is a work in progress.")
def addition(num1, num2):
	answer = num1 + num2
	print(answer)
def subtraction(num1, num2):
	answer = num1 - num2
	print(answer)
def multiplication(num1, num2):
	answer = num1 * num2
	print(answer)
def division(num1, num2):
	answer = num1 / num2
	print(answer)
def matrix_2_2(n11, n12, n21, n22, m11, m12, m21, m22):
	X = [[n11, n12], [n21, n12]]
	Y = [[m11, m12], [m21, m22]] 
	result = [[0, 0], [0, 0]]
	for i in range(len(X)):
		for j in range(len(X[0])):
			result[i][j] = X[i][j] + Y[i][j]
	for r in result:
		print(r)
def area_of_square(length):
	area = length * length
	print(area)
def perimeter_of_square(length):
	perimeter = length * 4
	print(perimeter)
def area_of_rectangle(length, breath):
	area = length * breath
	print(area)
def perimeter_of_rectangle(length, breath):
	perimeter = 2 * (length + breath)
	print(perimeter)
def area_of_triangle(base, height):
	area = 0.5 * base * height
	print(area)
def perimeter_of_triangle(base, in1, in2):
	perimeter = base + in1 + in2
	print(perimeter)
def area_of_trapezium(a, b, height):
	area = 0.5 * (a + b) * height
	print(area)
def perimeter_of_trapezium(a, b, height, in1):
	perimeter = a + b + height + in1
	print(perimeter)
def pythagoras_theorem_lega(b, c):
	b2 = b * b
	c2 = c * c
	a2 = c2 - b2
	a = math.sqrt(a2)
	print(a)
def pythagoras_theorem_legb(a, c):
	a2 = a * a
	c2 = c * c
	b2 = c2 - a2
	b = math.sqrt(b2)
	print(b)
def pythagoras_theorem_hyp(a, b):
	a2 = a * a
	b2 = b * b
	c2 = a2 + b2
	c = math.sqrt(c2)
	print(c)
def toa_angle(opp, adj):
	angle = math.degrees(math.atan(opp / adj))
	print(angle)
def cah_angle(adj, hyp):
	angle = math.degrees(math.atan(adj / hyp))
	print(angle)
def soh_angle(opp, hyp):
	angle = math.degrees(math.atan(opp / hyp))
	print(angle)
def toa_side(side, angle, in2):
	if side == "adj" or "adjecent":
		side = in2 / math.degrees(math.tan(angle))
		print(side)
	elif side == "opp" or "opposite":
		side = in2 * math.degrees(math.tan(angle))
		print(side)
	else:
		error_message(2)
def cah_side(side, angle, in2):
	if side == "hyp" or "hypotenuse":
		side = in2 / math.degrees(math.cos(angle))
		print(side)
	elif side == "adj" or "adjecent":
		side = in2 * math.degrees(math.cos(angle))
		print(side)
	else:
		error_message(2)
def soh_side(side, angle, in2):
	if side == "hyp" or "hypotenuse":
		side = in2 / math.degrees(math.sin(angle))
		print(side)
	elif side == "opp" or "opposite":
		side = in2 * math.degrees(math.sin(angle))
		print(side)
	else:
		error_message(2)		

# ---- ERROR (SYSTEMS) ---- #

def error_message(error_num):
	print("Unable to Proceed with Request. Analysing Error...")
	if error_num == 2:
		print("402: Trigonometry: Unknown side is invalid.")
	elif error_num == 3:
		print("403: Main Command Input is invalid.")
	elif error_num == 4:
		print("404: Command Input is invalid.")
	elif error_num == 5:
		print("405: Input is invalid.")
	elif error_num == 6:
		print("406: Request cannot be conducted.")
	else:
		print("407 Error. Unable to detect error. Please do us a solid and start a issue on Github! Thanks!")

# ---- USER INPUTS ---- #

try:
	maincmd = int(input('''
	Enter 1 for Basic Operation
	Enter 2 for Matrix
	Enter 3 for Area and Perimeter
	Enter 4 for Therom
	>>> ''')
except ValueError:
	error_message(3)
else:
	if maincmd == 1:
		try:
			cmd = int(input('''
			Enter 1 for Addition
			Enter 2 for Subtraction
			Enter 3 for Multiplication
			Enter 4 for Division
			>>> '''))
		except ValueError:
			error_message(4)
		else:
			in1 = float(input("Enter first number: "))
			in2 = float(input("Enter second number: "))
	elif maincmd == 2:
		try:
			cmd = int(input('''
			Enter 1 for Addition of 2 X 2 Matrix
			>>> '''))
		except ValueError:
			error_message(4)
		else:
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
				error_message(5)
	elif maincmd == 3:
		try:
			cmd = int(input('''
			Enter 1 for Area of Square
			Enter 2 for Perimeter of Square
			Enter 3 for Area of Rectangle
			Enter 4 for Perimeter of Rectangle
			Enter 5 for Area of Triangle
			Enter 6 for Perimeter of Triangle
			Enter 7 for Area of Trapezium
			Enter 8 for Perimeter of Trapezium
			>>> '''))
		except ValueError:
			error_message(4)
		else:
			if cmd == 1:
				length = float(input("Enter length of Square: "))
			elif cmd == 2:
				length = float(input("Enter length of Squaare: "))
			elif cmd == 3:
				length = float(input("Enter length of Rectangle: "))
				breath = float(input("Enter breath of Rectangle: "))
			elif cmd == 4:
				length = float(input("Enter length of Rectangle: "))
				breath = float(input("Enter breath of Rectangle: "))
			elif cmd == 5:
				base = float(input("Enter base of Triangle: "))
				height = float(input("Enter height of Triangle: "))
			elif cmd == 6:
				base = float(input("Enter base of Triangle: "))
				in1 = float(input("Enter another length of Triangle: "))
				in2 = float(input("Enter last length of Triangle: "))
			elif cmd == 7:
				a = float(input("Enter length 'a' of Trapezium: "))
				b = float(input("Enter length 'b' of Trapezium: "))
				height = float(input("Enter height of Trapezium: "))
			elif cmd == 8:
				a = float(input("Enter length 'a' of Trapezium: "))
				b = float(input("Enter length 'b' of Trapezium: "))
				height = float(input("Enter height of Trapezium: "))
				in1 = float(input("Enter last length of Trapezium: "))
			else:
				error_message(5)
	elif maincmd == 4:
		try:
			cmd = int(input('''
			Enter 1 for Pythagoras (Leg A)
			Enter 2 for Pythagoras (Leg B)
			Enter 3 for Pythagoras (Hypotenuse)
			Enter 4 for Trigonometry (TOA)
			Enter 5 for Trigonometry (CAH)
			Enter 6 for Trigonometry (SOH)
			>>> '''))
		except ValueError:
			error_message(4)
		else:
			if cmd == 1:
				in1 = float(input("Enter the value of B: "))
				in2 = float(input("Enter the value of C: "))
			elif cmd == 2:
				in1 = float(input("Enter the value of A: "))
				in2 = float(input("Enter the value of C:"))
			elif cmd == 3:
				in1 = float(input("Enter the value of A: "))
				in2 = float(input("Enter the value of B: "))
			elif cmd == 4:
				try:
					subcmd = int(input('''
					Enter 1 for Length
					Enter 2 for Degree
					>>> '''))
				except ValueError:
					error_message(4)
				else:
					if subcmd == 1:
						side = input("Enter Side that is unknown: ")
						in2 = float(input("Enter length of known side: "))
						angle = float(input("Enter known degree: "))
					elif subcmd == 2:
						opp = input("Enter length of Opposite: ")
						adj = float(input("Enter length of Adjecent: "))
			elif cmd == 5:
				try:
					subcmd = int(input('''
					Enter 1 for Length
					Enter 2 for Degree
					>>> '''))
				except ValueError:
					error_message(4)
				else:
					if subcmd == 1:
						side = input("Enter Side that is unknown: ")
						in2 = float(input("Enter length of known side: "))
						angle = float(input("Enter known degree: "))
					elif subcmd == 2:
						adj = float(input("Enter length of Adjecent: "))
						hyp = float(input("Enter length of Hypotenuse: "))
			elif cmd == 6:
				try:
					subcmd = int(input('''
					Enter 1 for Length
					Enter 2 for Degree
					>>> '''))
				except ValueError:
					error_message(4)
				else:
					if subcmd == 1:
						side = input("Enter Side that is unknown: ")
						in2 = float(input("Enter length of known side: "))
						angle = float(input("Enter known degree: "))
					elif subcmd == 2:
						opp = float(input("Enter length of Opposite: "))
						adj = float(input("Enter length of Adjecent: "))
			else:
				error_message(5)

# ---- SOLVING ---- #

if maincmd == 1:
	if cmd == 1:
		addition(in1, in2)
	elif cmd == 2:
		subtraction(in1, in2)
	elif cmd == 3:
		multiplication(in1, in2)
	elif cmd == 4:
		division(in1, in2)
	else:
		error_message(6)
elif maincmd == 2:
	if cmd == 1:
		matrix_2_2(n11, n12, n21, n22, m11, m12, m21, m22)
elif maincmd == 3:
	if cmd == 1:
		area_of_square(length)
	elif cmd == 2:
		perimeter_of_square(length)
	elif cmd == 3:
		area_of_rectangle(length, breath)
	elif cmd == 4:
		perimeter_of_rectangle(length, breath)
	elif cmd == 5:
		area_of_triangle(base, height)
	elif cmd == 6:
		perimeter_of_triangle(base, in1, in2)
	elif cmd == 7:
		area_of_trapezium(a, b, height)
	elif cmd == 8:
		perimeter_of_trapezium(a, b, height, in1)
	else:
		error_message(6)
elif maincmd == 4:
	if cmd == 1:
		pythagoras_theorem_lega(in1, in2)
	elif cmd == 2:
		pythagoras_theorem_legb(in1, in2)
	elif cmd == 3:
		pythagoras_theorem_hyp(in1, in2)
	elif cmd == 4:
		if subcmd == 1:
			toa_side(side, angle, in2)
		elif subcmd == 2:
			toa_angle(opp, adj)
	elif cmd == 5:
		if subcmd == 1:
			cah_side(side, angle, in2)
		elif subcmd == 2:
			cah_angle(adj, hyp)
	elif cmd == 6:
		if subcmd == 1:
			soh_side(side, angle, in2)
		elif subcmd == 2:
			soh_angle(opp, hyp)
	else:
		error_message(6)
else:
	error_message(6)
