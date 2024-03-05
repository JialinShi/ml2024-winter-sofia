
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

def read(n):
    dp = []
    for i in range(n):
        x = float(input("Enter x "))
        y = int(input("Enter y "))
        dp.append((x, y))
    return np.array(dp)

def main():
    #The program asks the user for input N (positive integer) and reads it.
    #Then the program asks the user to provide N (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.
    #This set of pairs constitutes the training set TrainS = {(x, y)_i}, i = 1..N.
    N = int(input("Enter N "))
    train_dp = read(N)
    X_train = train_dp[:, 0].reshape(-1, 1)  # Reshape for sklearn compatibility
    y_train = train_dp[:, 1]

    #Then the program asks the user for input M (positive integer) and reads it.
    #Then the program asks the user to provide M (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.
    
    M = int(input("Enter M "))
    test_dp = read(M)
    X_test = test_dp[:, 0].reshape(-1, 1)
    y_test = test_dp[:, 1]

    #In the end, the program outputs: the best k for the kNN Classification method and the corresponding test accuracy. kNN Classifier should be trained on pairs from TrainS, tested on x values from TestS and compared with y values from TestS.
    param = {'n_neighbors': range(1, 11)}
    knn = KNeighborsClassifier()
    classifier = GridSearchCV(knn, param)
    classifier.fit(X_train, y_train)

    optimal_k = classifier.best_params_['n_neighbors']
    test_accuracy = classifier.score(X_test, y_test)

    print(f"The best k for the kNN Classification method is {optimal_k} with corresponding test accuracy of {test_accuracy:.2f}")

if __name__ == "__main__":
    main()
