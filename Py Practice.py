

# Height and weight values are input
H = 176
W = 145
# User interface for the weight and height to be guessed
Gh = int(input('Enter your height guess: '))
Gw = int(input('Enter your weight guess: '))
# Initial block Initialization to check guess legitimacy(Close if Weight or height =0)
if (Gh == 0 & Gw == 0):
	print("Its Working")
	