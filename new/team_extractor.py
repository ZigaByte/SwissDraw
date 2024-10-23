from swiss import Swiss	
from reader import generate
from reader import getTeamName
from round_generator import generatePairs
import csv

matchesFile = "data/games_euf_2019_open.csv"

def readMatches(matchesFile):
	f = open(matchesFile, "rt", encoding="utf-8")
	reader = csv.reader(f, delimiter=",")
	next(reader)

	teams = set()

	for line in reader:
		teams.add(line[3])
		teams.add(line[4])
	print(teams)
	for t in teams:
		print(t)


if __name__ == "__main__":
	readMatches(matchesFile)