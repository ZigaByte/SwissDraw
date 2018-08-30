# TODO MOVE THIS TO TEAM_RECOGNISER
def getTeamName(t, i):
    for tt in t:
        if(t[tt] == i):
            return tt


from strength_calculator import calculateStrength

from team_recogniser import generateValuesFromFile
from team_recogniser import getTeamDictionary

from round_generator import generatePairs

(A, d) = generateValuesFromFile("swiss_draw.xlsx")
teams = getTeamDictionary("swiss_draw.xlsx")

print(d)
print(teams)

s = calculateStrength(A, d)
print(s)



# Generate new matchups
leaderboard = []
for i in range(len(teams)):
    leaderboard.append(i)

# Sort in the same way the leaderboard and the copy of s
cs = s.copy()

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

for i in range(len(leaderboard)):
    print(str(i+1) + ". place: " + getTeamName(teams, leaderboard[i]) + "\t " + str(s[leaderboard[i]]) + " points")

pairs = [] # append pairs to this
taken = [False] * len(leaderboard)

generatePairs(leaderboard, A, 0, taken, pairs)
#print(pairs)

print("Next matches:")
for (t1, t2) in pairs:
    print(getTeamName(teams, leaderboard[t1]),"\t", getTeamName(teams, leaderboard[t2]))
