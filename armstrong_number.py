import math

num = int(input("Enter a number to check if it is a armstrong number or not: "))
save = num
length = len(str(num))
sum1 = 0

while num != 0:
	rem = num % 10
	sum1 = sum1 + pow(rem, length)
	# num = int(num / 10)
	num = math.floor(num / 10)

if save == sum1:
	print(str(save)+" is armstrong number")
else:
	print(str(save)+" is not a armstrong number")
