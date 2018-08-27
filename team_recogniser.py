# The idea of this program is to open an excel file and read
# the different team names from column A and column B
import pandas

# Returns a pair with:
# - 2D incidence matrix for matches in the list
# - vector with difference in results
def generateValuesFromFile(file_name):
    data = pandas.read_excel(file_name, "swiss_matches", None)
    matches = data.to_dict("index")

    team_index = getTeamDictionary(file_name)
    team_count = len(team_index)

    # What we fill in
    A = [] 
    d = []
    
    for match in matches:
        team1 = matches[match][0].strip()
        team2 = matches[match][1].strip()

        # Fill the row of this match
        a = []
        for i in range(team_count):
            if(i == team_index[team1]):
                a.append(1)
            elif(i == team_index[team2]):
                a.append(-1)
            else:
                a.append(0)

        # Add this match's row to the matrix
        A.append(a)

        d.append(matches[match][2] - matches[match][3])
 
    return (A, d)
    
    
# Returns a dictionary of teams. Format: {'Team Name': index, ...}
def getTeamDictionary(file_name):
    data = pandas.read_excel(file_name, "teams", None)
    team_list = data.to_dict("list")

    teams = dict()
    i = 0
    for team in team_list[0]:
        teams[team.strip()] = i
        i += 1

    return teams
