x = 0
y = 0
orientation = 0

with open("1601input.txt") as file:

    for line in file:
        rep = line.replace(",","")
        str = rep.strip()
        instruction = str.split()

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

        p1 = abs(x) + abs(y)

print("Answer for Part 1:", p1)