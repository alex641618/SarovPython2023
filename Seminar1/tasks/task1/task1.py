from include import string_multiplier as sm

string = input("enter string: ")

while True:
	try: 
		n = int(input("enter n: "))
	except ValueError:
		print('error: invalid n type')
		print('enter correct n again')
		continue
	break

print(sm.string_multiplier(string, n))