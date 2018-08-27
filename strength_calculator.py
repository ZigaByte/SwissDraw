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
def computeB (A, d):
    teams = len(A[0])

    # Generate an empty matrix to for gauss initial values
    B = []
    for i in range(teams):
        b = []
        for i in range(teams + 1):
            b.append(0)
        B.append(b)
        
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
        for m in range(len(A)):
            if(A[m][i] != 0):
                B[i][len(B[0]) - 1] += -A[m][i] * d[m] 
    return B

# Divides the i-th row of M by f
def divideRow(M, i, f):
    if(abs(f) < 0.001):
        return M
    for j in range(len(M[0])):
        M[i][j] /= f
    return M

# Adds row j multiplied by f to row i
def addRowMultiple(M, i, j, f):
    for k in range(len(M[0])):
        M[i][k] += M[j][k] * f;
        if(abs(M[i][k]) < 0.0001): # If that close to 0, get it to 0
            M[i][k] = 0
    return M

# Perform Gauss on the matrix
def gauss(B):
    for c in range(len(B[0]) - 1):
        #print("Step ", c)
        #printMatrix(B)
        B = divideRow(B, c, B[c][c])
        #printMatrix(B)

        for r in range(c+1, len(B)):
            if(B[c][c] != 0):
                B = addRowMultiple(B, r, c, -B[r][c] / B[c][c])
                #printMatrix(B)

    for c in range(1, len(B[0]) - 2):
        for r in range(c):
            if(B[c][c] != 0):
                B = addRowMultiple(B, r, c, -B[r][c] / B[c][c])

    return B

def printMatrix(M):
    for b in M:
        print(b)

def calculateStrength(M, d):
    # Get initial matrix for Gauss
    B = computeB(M, d)

    # Perform Gauss
    C = gauss(B)

    #   printMatrix(C)

    for i in range(len(C)):
        for j in range(len(C[i])-1):
            C[i][j] = round(C[i][j])

    printMatrix(C)

    # Read the strngths from the last Gauss matrix
    s = [0.0] * len(C)
    minS = 10000
    for r in range(len(C)):
        s[r] = C[r][len(C[r]) - 1]

        # Test for new scoring>
        '''
        for i in range(len(C[r]) - 1):
            if(C[r][i] == 1.0):
                s[i] = C[r][len(C[r]) - 1] / 2
            elif(C[r][i] == -1.0):
                s[i] = -C[r][len(C[r]) - 1] / 2
        '''

        minS = min(minS, s[r])

    return s
'''
    for r in range(len(C)):
        s[r] -= minS
'''

