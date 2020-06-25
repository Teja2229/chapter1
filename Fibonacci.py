t1=0
t2=1
nextterm=0
n=int(input("enter number:"))
print("fibonacci series:",t1,t2)
nextterm=t1+t2
while(nextterm<=n):
	print(nextterm)
	t1=t2
	t2=nextterm
	nextterm=t1+t2
	