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

from strength_calculator import calculateStrength
from team_recogniser import generateValuesFromFile

(A, d) = generateValuesFromFile("swiss_draw.xlsx")
#print(A)
#print(d)

s = calculateStrength(A, d)
print(s)
