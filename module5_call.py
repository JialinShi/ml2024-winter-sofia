
from module5_mod import  CheckNum

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
