def do(instruction, part2 = False):

    x = 0
    y = 0
    orientation = 0
    visit_twice = [[0, 0]]

    for direction in instruction:
        turn = direction[0]
        steps = int(direction[1:])

        if turn == "R":
            orientation = (orientation + 1) % 4
        else:
            orientation = (orientation - 1) % 4

        for _ in range(steps):
            if orientation == 0:
                y += 1
            elif orientation == 1:
                x += 1
            elif orientation == 2:
                y -= 1
            else:
                x -= 1

            if part2:
                if [x, y] in visit_twice:
                    return abs(x) + abs(y)            
                else:
                    visit_twice.append([x, y])

    return abs(x) + abs(y)

if __name__ == "__main__":

    with open("1601input.txt") as file:

        for line in file:
            rep = line.replace(",","")
            str = rep.strip()
            instruction = str.split()

print("Answer for Part 1:", do(instruction))
print("Answer for Part 2:", do(instruction, part2=True))