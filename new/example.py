from swiss import Swiss	
	
A = [[1, -1, 0, 0, 0],
	 [0, 0, 1, -1, 0],
	 [0, 0, 1, -1, 0],
	 [1, 0, 0, 0, -1],
	 [1, 0, -1, 0, 0]]	
d = [3, 1, 2, 2, 1]

swiss = Swiss(A, d, len(A[0]))
print(swiss.getScores())
