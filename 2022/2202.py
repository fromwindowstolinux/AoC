# REVISED SOLUTION : REVISION 1

# PART 1
def p1(duel, shape, outcome):
    # rock
    if duel[1] == "X":
        shape += 1
        if duel[0] == "A":
            outcome += 3
        elif duel[0] == "B":
            outcome += 0
        else:
            outcome += 6
    # paper
    elif duel[1] == "Y":
        shape += 2
        if duel[0] == "A":
            outcome += 6
        elif duel[0] == "B":
            outcome += 3
        else:
            outcome += 0
    # scissors
    else:
        shape += 3
        if duel[0] == "A":
            outcome += 0
        elif duel[0] == "B":
            outcome += 6
        else:
            outcome += 3

    total = shape + outcome
    return total


# PART 2
def p2(duel, outcome, shape):
    # lose
    if duel[1] == "X":
        outcome += 0
        if duel[0] == "A":
            shape += 3
        elif duel[0] == "B":
            shape += 1
        else:
            shape += 2
    # draw
    elif duel[1] == "Y":
        outcome += 3
        if duel[0] == "A":
            shape += 1
        elif duel[0] == "B":
            shape += 2
        else:
            shape += 3
    # win
    else:
        outcome += 6
        if duel[0] == "A":
            shape += 2
        elif duel[0] == "B":
            shape += 3
        else:
            shape += 1

    total = outcome + shape
    return total


if __name__ == "__main__":
    shape = 0
    outcome = 0
    part1 = 0
    part2 = 0
    with open("2202input.txt") as file:
        for line in file:
            duel = line.split()
            part1 += p1(duel, shape, outcome)
            part2 += p2(duel, outcome, shape)

print("Answer for Part 1:", part1)
print("Answer for Part 2:", part2)



# FIRST SOLUTION

part1 = 0
part2 = 0

with open("2202input.txt") as file:
    for line in file:
        duel = line.split()

        # Part 1
        # scissors combo
        if duel[1] == "Z" and duel[0] == "A":  # lose
            part1 += 3  # 3 + 0 =
        elif duel[1] == "Z" and duel[0] == "B":  # win
            part1 += 9  # 3 + 6 =
        elif duel[1] == "Z" and duel[0] == "C":  # draw
            part1 += 6  # 3 + 3 =
        # paper combo
        elif duel[1] == "Y" and duel[0] == "A":  # win
            part1 += 8  # 2 + 6 =
        elif duel[1] == "Y" and duel[0] == "B":  # draw
            part1 += 5  # 2 + 3 =
        elif duel[1] == "Y" and duel[0] == "C":  # lose
            part1 += 2  # 2 + 0 =
        # rock combo
        elif duel[1] == "X" and duel[0] == "A":  # draw
            part1 += 4  # 1 + 3 =
        elif duel[1] == "X" and duel[0] == "B":  # lose
            part1 += 1  # 1 + 0 =
        elif duel[1] == "X" and duel[0] == "C":  # win
            part1 += 7  # 1 + 6 =

        # Part 2
        # lose combo
        if duel[0] == "A" and duel[1] == "X":  # lose
            part2 += 3
        elif duel[0] == "B" and duel[1] == "X":  # lose
            part2 += 1
        elif duel[0] == "C" and duel[1] == "X":  # lose
            part2 += 2
        # draw combo
        elif duel[0] == "A" and duel[1] == "Y":  # draw
            part2 += 4
        elif duel[0] == "B" and duel[1] == "Y":  # draw
            part2 += 5
        elif duel[0] == "C" and duel[1] == "Y":  # draw
            part2 += 6
        # win combo
        elif duel[0] == "A" and duel[1] == "Z":  # win
            part2 += 8
        elif duel[0] == "B" and duel[1] == "Z":  # win
            part2 += 9
        elif duel[0] == "C" and duel[1] == "Z":  # win
            part2 += 7

print("Answer for Part 1:", part1)
print("Answer for Part 2:", part2)