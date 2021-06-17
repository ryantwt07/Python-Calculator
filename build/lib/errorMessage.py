def systemsError(error_num):
	print("Unable to Proceed with Request. Analysing Error...")
	if error_num == 1:
		print("401: Math Import Module Failure.")
	elif error_num == 2:
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
