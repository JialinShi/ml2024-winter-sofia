
import numpy as np

def knn_reg(dp, k, X):
    # Calculate EU distance
    dist = np.sqrt((dp[:, 0] - X) ** 2)
    # Get KNN
    knn = np.argsort(dist)[:k]
    # Calculate Y based on knn
    pred_y = np.mean(dp[knn, 1])
    return pred_y

def main():
    #initialize data points
    dp = np.empty((0, 2), float)
    
    #input # of datapoints and decide k
    N = int(input("Enter N: "))
    k = int(input("Enter k for # of neighbors: "))
    # Error
    if k > N:
        print("Error: k must be <= N.")
        return
    
    # Reading data points
    for i in range(N):
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
        # Appending the new point to the points array
        dp = np.append(dp, np.array([[x, y]]), axis=0)
        
    #predict the value for X
    X = float(input("Enter input X: "))
    res = knn_reg(dp, k, X)
    print(res)

if __name__ == "__main__":
    main()
