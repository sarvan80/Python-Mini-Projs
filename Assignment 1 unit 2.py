'''
############# LOGICAL CONSTRUCT ###########
# Make an array of 100 elements#
# Check for divisibility with 3 and if the condition is satisfied make a sub-block to#
# check for divisibility if both conditions are satisfied print "CowPie" or if only one condition #
# is Satisfied type "Cow".IF the condition fails for 3 check for divisibility with 7 and #
# if that is satisfied type "Pie"(Here we dont have to check again for divisibility with 3#
# since that condition is already failed.If both the Main conditions ie divisibility with#
# 3 and 7 fail print the number#

########## Critical Aspect #################
# Avoid Rule clash on numbers which are divisible by 7 & 3 and keep the rules #
# Mutually exclusive ie any point in time only one rule is satisfied#


# Block to Initialize the Array to check the divisibility condition #
print("Printing the Numbers")
for i in range(1,100):
	
 # checking for both 3 & 7  
	if(i % 3 == 0):
	
	#Sub block to check divisibility with 7
		if(i % 7 == 0):
			print("CowPie")
		else:
			print("Cow")
	# Rule to check 7 only Divisibility
	elif(i % 7 == 0):
			print("Pie")						
    # Printing number on both rules not satisfied
	else:
		print(i)
'''
