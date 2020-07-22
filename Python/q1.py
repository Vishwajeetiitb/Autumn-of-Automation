L = []
file = open('MyFirstFile.txt', 'w') 
# file.writelines(L) 
# file.close() 

num_digits = input("Enter the digit")
num_digits = int(num_digits)
last_digit = 10**num_digits
is_prime = True
first = True
i_last = 3
for i in range(5,last_digit):
	is_prime = True
	for m in range(2,int((i+i%2)/2)):
		# print(i)
		if i%m ==0:
			is_prime = False
			# print(i)
			break

	if is_prime:
		print(i_last,i)
		L.append(str(i_last)+" "+ str(i)+"\n")
		i_last = i


file.writelines(L) 
file.close() 	