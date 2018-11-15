from swiss import Swiss	
from reader import generate
from reader import getTeamName
from round_generator import generatePairs
	
teamsFile = "teams.csv"
roundsFile = "round2.csv"

def name(i):
	return getTeamName(teamsFile, i)

# To naj bo zadnja ekipa, ki še ni počivala
teamWithNoRound = 16

A, Q, d, n = generate(teamsFile, roundsFile)

# Calculate scores
swiss = Swiss(A, d, n)
s = swiss.getScores()

# Generate Leaderboard
leaderboard = sorted([(name(i), i, si) for i, si in enumerate(s)], key = lambda x: -x[2]) 
for i, (teamName, team_index, score) in enumerate(leaderboard):
	print(i, teamName, score)
	
print("--------------------------------")

# Izpis za lestvico
for ss in s:
	print(ss)

print("--------------------------------")


newPairs = generatePairs([i for teamName, i, si in leaderboard], A + Q, teamWithNoRound)
# Izpis parov
for i, j in newPairs:
	print(name(i), "\t", name(j))
