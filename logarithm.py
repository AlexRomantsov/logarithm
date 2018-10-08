#------------------------------------------
#---------------Python 3.7.0---------------
#-----------------Source:------------------
#https://github.com/AlexRomantsov/logarithm
#------------------------------------------

def log(number, base):
	number, base = float(number), float(base)
	result = 0.0
	while(number >= base):
		number/=base
		result += 1
	return result