
class CheckNum:
    def __init__(self):
        self.nums = []

    def append_num(self, num):
        self.nums.append(num)

    def find_num(self, x):
        if x in self.nums:
            return self.nums.index(x) + 1  # start from 1
        return -1

def main():
    l1 = CheckNum()
    
    N = int(input("Please enter a positive integer N: "))
    for i in range(N):
        n = int(input("Enter a number: "))
        l1.append_num(n)
    
    X = int(input("Check if X is in the list: "))
    res = l1.find_num(X)
    
    print(res)

if __name__ == "__main__":
    main()
