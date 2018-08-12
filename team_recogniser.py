# The idea of this program is to open an excel file and read
# the different team names from column A and column B

import pandas

# Returns a dictionary of teams. Format: {'Team Name': index, ...}
def getTeamDictionary(file_name):
    data = pandas.read_excel(file_name, "teams", None)
    team_list = data.to_dict("list")

    teams = dict()
    i = 0
    for team in team_list[0]:
        teams[team] = i
        i += 1

    return teams

print(getTeamDictionary("swiss_draw.xlsx"))
