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
        B = divideRow(B, c, B[c][c])

        for r in range(c+1, len(B)):
            if(B[c][c] != 0):
                B = addRowMultiple(B, r, c, -B[r][c] / B[c][c])

    for c in range(1, len(B[0]) - 2):
        for r in range(c):
            if(B[c][c] != 0):
                B = addRowMultiple(B, r, c, -B[r][c] / B[c][c])

    return B

def printMatrix(M):
    for b in M:
        print(b)

def allFixed(fixed):
    for f in fixed:
        if(not f):
            return False
    return True

def calculateStrength(M, d):
    # Get initial matrix for Gauss
    B = computeB(M, d)

    # Perform Gauss
    C = gauss(B)

    # Round the values for fun (there should only be -1s, 0s and 1s anyway), except the last column
    for i in range(len(C)):
        for j in range(len(C[i])-1):
            C[i][j] = round(C[i][j])

    # Get disjunct strength values and minimise the sum of them
    fixed = [False] * (len(C[0]) - 1)

    while(not allFixed(fixed)):
        current = 0
        toFix = set()
        # Get one that is not fixed
        for i in range(len(fixed)):
            if(not fixed[i]):
                current = i
                toFix.add(current)
                break
            
        # Find all connected teams and add to toFix list
        while(True):
            toAdd = set()
            for c in toFix:
                for i in range(len(C[c]) - 1):
                    if(C[c][i] != 0 and i != c and not(i in toFix)):
                        toAdd.add(i)
                for i in range(len(C)): 
                    if(C[i][c] != 0 and i != c and not(i in toFix)):
                        toAdd.add(i)
            toFix = toFix.union(toAdd)
            if(len(toAdd) is 0):
                break
        
        sumStrength = 0
        for f in toFix:
            fixed[f] = True
            sumStrength += C[f][len(C[f])-1]

        for f in toFix:
            C[f][len(C[f])-1] -= sumStrength / len(toFix)
                    
    # Read the strngths from the last Gauss matrix
    s = [0.0] * len(C)
    for r in range(len(C)):
        s[r] = C[r][len(C[r]) - 1]
        
    return s


