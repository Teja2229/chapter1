print("to caluclate sum and average. Input 0 to exit.")
count = 0
sum = 0.0
number = 1
while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1
if count == 0:
	print("Input some numbers")
else:
	print("Average and Sum")