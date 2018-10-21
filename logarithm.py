def log(number, base):
	'''function to find the logarithm
https://github.com/AlexRomantsov/logarithm'''
	number, base = float(number), float(base)
	result = 0.0
	while(number >= base):
		number/=base
		result += 1
	return result