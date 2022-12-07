
def do():

    group = []
    total_cal = 0

    with open("2201input.txt") as file:
        for line in file:
            line = line.strip('\n')
            if line == '':
                group.append(total_cal)
                total_cal = 0
            else:
                total_cal += int(line)

            group.sort()
                    
    print("Answer for Part 1:", group[-1])
    print("Answer for Part 2:", sum(group[-3:]))

do()
