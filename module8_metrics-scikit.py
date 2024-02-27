#!/usr/bin/python

import numpy as np
from sklearn.metrics import precision_score, recall_score


def main():
	
	#The program asks the user for input N (positive integer) and reads it.
	N = int(input("Please enter a positive integer N for points(N): "))
	
	x=np.zeros(N) # Truth
	y=np.zeros(N) # Predicted
	
	#Then the program asks the user to provide N (x, y) points (one by one) 
	#and reads all of them: first: x value, then: y value for every point one by one.
	#Both X and Y are either 0 or 1.
	points = np.zeros((N, 2))
	for i in range(N):
		x[i] = int(input("Enter x (0 or 1): ")) 
		y[i] = int(input("Enter y (0 or 1): ")) 
	
	#the program outputs: the Precision and Recall based on the inputs.
	prec = precision_score(x, y)
	rec = recall_score(x, y)
	print("\nPrecision: {:.2f}".format(prec))
	print("Recall: {:.2f}".format(rec))
	


if __name__ == "__main__":
	main()
