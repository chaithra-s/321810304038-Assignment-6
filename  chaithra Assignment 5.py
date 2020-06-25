#display multiplication table of k 
k=int(input("enter k"))
for i in range (1,11):
	print(k,"*i=",k*i)
	
#number of odd and evens
count=0	
n=int(input("enter val og n"))
for i in range (1,n):
	if i%2==0:
		count+=1
print("no. of even numbers are:",count)
print("no. of odd numbers",(n-1)-count)

#print all numbers 0-6 except 3 and 6
for x in range (0,6):
    if x==3:
        	continue
	print("\n",x)	
	
#fibonacci
n=int (input ("enter the limit"))
a=0
b=1
count=0
if n<0:
							print("enter the positive number")
		elif n==1:
							print("fibonacci series upto",n)
							print(a)
		else:
							print("fibonacci series are:")
							while count<n:
												print(a)
												sum=a+b
												a=b
												b=sum
												count=count+1
															
																			
#hcf
def hcf(x,y):
		if x > y:
			smaller = y
		else:
			smaller = x
		for i in range (1,smaller +1):
		if ((x % i == 0) and (y % i == 0)):
					hcf  = i
				return hcf
		num1= int(input("Enter first number:"))
		num2=int(input("Enter second number:"))
		print(" The H.C.F. of", num1,"and", num2,"is", hcf( num1,num2))																																
																		
																		
																		
																	
															
																	
																	
							