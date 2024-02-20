
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score



def main():
    
    #The program asks the user for input N (positive integer) and reads it.
    N = int(input("Please enter a positive integer N: "))
    #Then the program asks the user for input k (positive integer) and reads it.
    k = int(input("Please enter a positive integer k: "))
    if k > N:
        print("Error: k cannot be greater than N.")
        
    #Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.
    points = np.zeros((N, 2))
    for i in range(N):
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        points[i] = [x, y]
    
    #fit model    
    X_train = points[:, 0].reshape(-1, 1)  # Reshape for a single feature
    y_train = points[:, 1]
    #asks the user for input X
    X_test = np.array([float(input("Enter input X: "))]).reshape(-1, 1)
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X_train, y_train)
    y_pred = knn_regressor.predict(X_test)
    #outputs: the result (Y) of k-NN Regression
    print(f"The result (Y) of k-NN Regression is: {y_pred[0]}")
    
    # Coefficient of Determination (R^2)
    y_true = y_train 
    r2 = r2_score(y_true, knn_regressor.predict(X_train))
    # provide the coefficient of determination
    print(f"Coefficient of Determination (R^2): {r2}")


if __name__ == "__main__":
    main()
