letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
part1 = 0
rucksacks = []

with open("2203input.txt") as file:   
    for line in file:
        line = line.strip()
        divide = len(line)/2
        convert_int = int(divide)
        first_half = line[0:convert_int]
        second_half = line[convert_int:]
        for item in range(len(letters)):
            if letters[item] in first_half:
                if letters[item] in second_half:
                    rucksacks.append(letters[item])

for rucksack in rucksacks:
    priorities1 = letters.index(rucksack) + 1
    part1 += priorities1

print("Answer for Part 1:", part1)