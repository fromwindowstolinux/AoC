def p1(line, total):

    rucksacks = []
    divide = len(line)/2
    convert_int = int(divide)
    first_half = line[0:convert_int]
    second_half = line[convert_int:]
    for item in range(len(letters)):
        if letters[item] in first_half:
            if letters[item] in second_half:
                rucksacks.append(letters[item])

    for rucksack in rucksacks:
        priorities = letters.index(rucksack) + 1
        total += priorities
    
    return total

def p2(content, total):

    group = 0
    badges = []
    while True:
        text = content[0+group:3+group]
        for chara in letters:
            if (chara in text[0]) and (chara in text[1]) and (chara in text[2]):
                badges.append(chara)
        group += 3    
        if group == 300:
            break

    for badge in badges:
        priorities = letters.index(badge) + 1
        total += priorities

    return total


if __name__ == "__main__":

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 0
    part1 = 0
    part2 = 0

    with open("2203input.txt") as file:     
        # # comment line 48-50 for answer part 2
        for line in file:
            line = line.strip()
            part1 += p1(line, total)
        # # comment line 52-53 for answer part 1
        # content = file.readlines()
        # part2 = p2(content, total)               
    
print("Answer for Part 1:", part1)
print("Answer for Part 2:", part2)
