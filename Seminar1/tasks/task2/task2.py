from include import number_repeater as nr

while True:
	try: 
		number = int(input("enter number: "))
	except ValueError:
		print('error: invalid number type')
		print('enter correct number again')
		continue
	break

while True:
	try: 
		n = int(input("enter n: "))
	except ValueError:
		print('error: invalid n type')
		print('enter correct n again')
		continue
	break

print(nr.number_repeater(number, n))