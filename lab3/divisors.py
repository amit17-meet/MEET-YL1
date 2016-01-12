def divisors(n):
	if n == 0:
		print("The number 0 has no divisors")
	for i in range(1,n+1):
		if n%i==0:
			print(i)


print("Enter a number")
n = int(input())
divisors(n)
