
from strength_calculator import calculateStrength

from team_recogniser import generateValuesFromFile
from team_recogniser import getTeamDictionary
from team_recogniser import getTeamName

from round_generator import generatePairs

#file = "swiss_draw.xlsx"
file = "sul.xlsx"

(A, d) = generateValuesFromFile(file)
teams = getTeamDictionary(file)

s = calculateStrength(A, d)

# Generate new matchups
leaderboard = []
for i in range(len(teams)):
    leaderboard.append(i)

# Gerenate leaderboard, sorted indexes of teams
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

pairs = generatePairs(leaderboard, A, 2)

print("Next matches:")
for (t1, t2) in pairs:
    print(getTeamName(teams, leaderboard[t1]),"\t", getTeamName(teams, leaderboard[t2]))
