import csv

teams = {}

def readTeams(teamsFile):
	f = open(teamsFile, "rt", encoding="utf-8")
	reader = csv.reader(f, delimiter=",")
	next(reader)
	return {t[0]:i for i,t in enumerate(reader)}

def invertTeams(teamsFile):
	f = open(teamsFile, "rt", encoding="utf-8")
	reader = csv.reader(f, delimiter=",")
	next(reader)
	return {i:t[0] for i,t in enumerate(reader)}

def readMatches(matchesFile,teams):
	f = open(matchesFile, "rt", encoding="utf-8")
	reader = csv.reader(f, delimiter=",")
	next(reader)

	matches = []
	queued = []
	for line in reader:
		if(line[0] == "" and line[1] == ""):
			queued.append((teams[line[0]], teams[line[1]]))
		else:
			matches.append((teams[line[0]], teams[line[1]], float(line[2]), float(line[3])))

	return (queued, matches)

def generateA(matches, teams):
	n = len(teams)
	m = len(matches)

	A = []
	for m in matches:
		a = [0] * n
		a[m[0]] = 1
		a[m[1]] = -1
		A.append(a)
	return A

def generateD(matches):
	m = len(matches)

	d = [0] * m
	for i,m in zip(range(m), matches):
		d[i] = m[2] - m[3]
	return d

def generate(teamsFile, matchesFile):
	teams = readTeams(teamsFile)
	print(teams)
	queued, matches = readMatches(matchesFile,teams)

	return (generateA(matches, teams), generateA(queued, teams), generateD(matches), len(teams))

def getTeamName(teamsFile, i):
	teams = invertTeams(teamsFile)
	return teams[i]
