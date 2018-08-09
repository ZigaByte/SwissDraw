d = [5,5,2,5] # Results of matches
s = [0,0,0,0] # Strengths of teams

A = [[ 1, -1,  0,  0],
     [ 0,  0,  1, -1],
     [ 1,  0, -1,  0],
     [ 0,  1,  0, -1]]

# Count the number of matches between team i and team j
def matchCount(A, i, j):
    count = 0
    # Check each match
    for m in range(len(A)):
        if(A[m][i] != 0 and A[m][j] != 0):
            count += 1
    return count

# Computes the start matrix depending on the number of
# games teams played and so on
# A is an incidence matrix, with matchups
def computeB (A):
    teams = len(A[0])
    B = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]
    # Calculate numbers in the matrix
    for i in range(teams):
        totalMatchesForI = 0
        for j in range(teams):
            if(i != j):
                inc = matchCount(A, i, j)
                B[i][j] = matchCount(A, i, j)
                totalMatchesForI += inc
        B[i][i] = -totalMatchesForI

    # Calculate last column
    for i in range(teams):
        for m in range(teams):
            if(A[m][i] != 0):
                B[i][4] += -A[m][i] * d[m] 

        
    return B

def divideRow(M, i, f):
    for j in range(len(M[0])):
        M[i][j] /= f
    return M

# Adds row j multiplied by f to row i
def addRowMultiple(M, i, j, f):
    for k in range(len(M[0])):
        M[i][k] += M[j][k] * f;
    return M

def gauss(B):
    for c in range(len(B[0]) - 1):
        B = divideRow(B, c, B[c][c])
        for r in range(c+1, len(B)):
            B = addRowMultiple(B, r, c, -B[r][c] / B[c][c])

    for c in range(1, len(B[0]) - 1):
        for r in range(c):
            B = addRowMultiple(B, r, c, -B[r][c] / B[c][c])
        
    return B

def printMatrix(M):
    for b in M:
        print(b)

def start():
    print("Computing B:")
    B = computeB(A)
    printMatrix(B)
    print()

    C = gauss(B)
    printMatrix(C)

    minS = 10000
    for r in range(len(C)):
        s[r] = C[r][len(C)]
        minS = min(minS, s[r])

    for r in range(len(C)):
        s[r] -= minS
    print(s)
