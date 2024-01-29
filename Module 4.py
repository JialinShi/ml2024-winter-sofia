N =int(input("Please enter a positive integer N: "))

nums=[]
for i in range(N):
    nums.append(int(input("Please enter a number: ")))

check = int(input("Please enter a number to see if it is stored in the list: " ))
if check in nums:
    print(nums.index(check)+1)
else: 
    print(-1)
    

