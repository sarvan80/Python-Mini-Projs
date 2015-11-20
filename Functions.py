# Assignment 2

H = 176
W = 145

Gh = input('Enter your height guess: ')
Gw = input('Enter your weight guess: ')



# if (Gh == 0 / Gw == 0)/(Gh == 0 & Gw == 0):
if Gh > 0:
	if Gw > 0:
		if Gh > H & Gw > W:
			print("Both are Higher")
		elif Gh < H & Gw < W:			
			print("Both are Lower")	
		elif (Gh < H & Gw > W)/(Gh > H & Gw < W):
		    print("One is Lower")			
	else:
		print("Game Over")
else:
	print("Game Over")
