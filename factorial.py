num = int(input("Enter a number you want to know the factorial of: "))
fact = 1
for i in range(1, num+1):
    fact = fact * i

print("factorial of "+str(num)+" is: "+str(fact))