from swiss import Swiss
from reader import generate
from reader import getTeamName
from round_generator import generatePairs
import csv

matchesFile = "wul/WUL_3.csv"


def readMatches(matchesFile):
    f = open(matchesFile, "rt", encoding="utf-8")
    reader = csv.reader(f, delimiter=",")
    next(reader)

    teams = []

    for line in reader:
        team1 = line[0]
        if team1 not in teams:
            teams.append(team1)
        team2 = line[1]
        if team2 not in teams:
            teams.append(team2)

    teams = sorted(teams)
    print("Teams for debugging similarity:")
    for t in teams:
        print("'", t, "'", sep="")
    print("Total of", len(teams), "teams", sep=" ")

    print("Teams:")
    for t in teams:
        print(t)


if __name__ == "__main__":
    readMatches(matchesFile)
