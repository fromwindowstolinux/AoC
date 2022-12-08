starter = []
part1 = 0
part2 = 0

with open("2206input.txt") as file:
    line = file.read()

    # Part 1
    while (len(starter) < 4): 
        character = line[part1]
        if character not in starter: 
            starter.append(character)
            part1 += 1 
        else: 
            while character in starter:
                starter.pop(0)

            starter.append(character)
            part1 += 1

    # Part 2
    while (len(starter) < 14): 
        character = line[part2]
        if character not in starter: 
            starter.append(character)
            part2 += 1 
        else: 
            while character in starter:
                starter.pop(0)

            starter.append(character)
            part2 += 1
            
print("Answer for Part 1:", part1)
print("Answer for Part 2:", part2)