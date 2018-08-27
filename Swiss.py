# Example input for the strength calculator
e = [5,5,5,1,5,1,3,7,1] # Results of matches
E = [[ 1,  0,  0,  -1,  0,  0],
     [ 0,  1,  0,  0,  -1,  0],
     [ 0,  0,  1,  0,  0,  -1],
     [ 1, -1,  0,  0,  0,  0],
     [ 0,  0,  1, -1,  0,  0],
     [ 0,  0,  0,  0,  1,  -1],
     [ 1,  0,  -1,  0,  0,  0],
     [ 0,  1,  0,  0,  0,  -1],
     [ 0,  0,  0,  1,  -1,  0]]

# TODO MOVE THIS TO TEAM_RECOGNISER
def getTeamName(t, i):
    for tt in t:
        if(t[tt] == i):
            return tt


from strength_calculator import calculateStrength
from team_recogniser import generateValuesFromFile
from team_recogniser import getTeamDictionary

(A, d) = generateValuesFromFile("swiss_draw.xlsx")
teams = getTeamDictionary("swiss_draw.xlsx")

#print(A)
print(d)
print(teams)

s = calculateStrength(A, d)
print(s)



# Generate new matchups
leaderboard = []
for i in range(len(teams)):
    leaderboard.append(i)
#print(leaderboard)

# Sort in the same way the leaderboard and the copy of s
cs = s.copy()
#print(cs)

for i in range(len(cs)):
    for j in range(1, len(cs)-i):
        if(cs[j] > cs[j - 1]):
            # Swap
            t = cs[j]
            cs[j] = cs[j-1]
            cs[j-1] = t

            t = leaderboard[j]
            leaderboard[j] = leaderboard[j-1]
            leaderboard[j-1] = t

#print(cs)
#print(leaderboard)

for i in range(len(leaderboard)):
    print(str(i+1) + ". place: " + getTeamName(teams, leaderboard[i]) + "\t " + str(s[leaderboard[i]]) + " points")

def allTaken(taken):
    for i in taken:
        if not i:
            return False
    return True

# Generate new matchups with A and leaderboad
def generatePairs(currentI, taken):    
    if(allTaken(taken)):
        return True

    if(taken[currentI]):
        return generatePairs(currentI + 1, taken)

    # Look for another team
    for otherI in range(currentI + 1, len(leaderboard)):
        other = leaderboard[otherI]
        current = leaderboard[currentI]

        # Check if other is available
        if(taken[otherI]):
            continue

        # Check if matched before
        haveMatchedBefore = False
        for match in A:
            if(match[current] != 0 and match[other] != 0):
                haveMatchedBefore = True
        if(haveMatchedBefore):
            continue

        # If all other things passed, add the pair
        pairs.append((currentI, otherI))
        taken[currentI] = True
        taken[otherI] = True

        # Do recursion and check if it worked
        result = generatePairs(currentI+1, taken)
        if(result):
            return True
        else:
            # Undo last and continue
            pairs.pop(len(pairs) - 1)
            taken[currentI] = False
            taken[otherI] = False
            continue

    
pairs = [] # append pairs to this
taken = [False] * len(leaderboard)

generatePairs(0, taken)
#print(pairs)

print("Next matches:")
for (t1, t2) in pairs:
    print(getTeamName(teams, leaderboard[t1]),"\t", getTeamName(teams, leaderboard[t2]))
