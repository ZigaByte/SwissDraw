
def allTaken(taken):
    for i in taken:
        if not i:
            return False
    return True

# Generate new matchups with A and leaderboad
def generatePairs(leaderboard, A, currentI, taken, pairs):    
    if(allTaken(taken)):
        return True

    if(taken[currentI]):
        return generatePairs(leaderboard, A, currentI + 1, taken, pairs)

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
        result = generatePairs(leaderboard, A, currentI+1, taken, pairs)
        if(result):
            return True
        else:
            # Undo last and continue
            pairs.pop(len(pairs) - 1)
            taken[currentI] = False
            taken[otherI] = False
            continue
