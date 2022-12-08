starter = []
part1 = 0
part2 = 0

def a(starter, line, l):
    part = 0
    while (len(starter) < l): 
        character = line[part1]
        if character not in starter: 
            starter.append(character)
            part += 1 
        else: 
            while character in starter:
                starter.pop(0)

            starter.append(character)
            part += 1
    return part

with open("2206input.txt") as file:
    line = file.read()
    part1 = a(starter, line, 4)
    part2 = a(starter, line, 14)

print("Answer for Part 1:", part1)
print("Answer for Part 2:", part2)