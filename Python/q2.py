
def is_palindrome(x):
	l = len(a)
	for i in range(int((l-l%2)/2)):
		if a[i] == a[l-i-1]:
			continue

		else:
			print(x," is not palindrome")
			return False
	return True
a= input("Please enter the palindrome digit \n")
if is_palindrome(a):
	l = len(a)
	if int(a)!=9:
		a = list(a)
		for i in range(int((l-l%2)/2),l):
			if a[i] is not '9':
				a[i] = str(int(a[i])+1)
				if i != l-i-1:
					a[l-i-1]=a[i]
				break
			else:
				if i == l-1:
					a[i] ='1'
					a[l-i-1] ='1'
					a.insert(2,'0')
					continue

				a[i] = '0'
				if i != l-i-1:
					a[l-i-1]=a[i]
	else:
		a = '11'


print("".join(a))