part1 = 0
lightp1 = {}

part2 = 0
lightp2 = {}

with open("1506input.txt") as file:

    for line in file:

        remove_noise = line.replace("turn","").replace(",", " ").replace("through", "")
        # print(l_rep)
        remove_space = remove_noise.strip()
        # print(l_str)
        words = remove_space.split(" ")
        # print(words)
        instruction = words[0]
        x1 = int(words[1])
        y1 = int(words[2])
        x2 = int(words[4])
        y2 = int(words[5])
        
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):  
                if instruction == "on":
                    lightp1[(x, y)] = True
                    if (x, y) in lightp2:
                        lightp2[(x, y)] += 1
                    else:
                        lightp2[(x, y)] = 1
                elif instruction == "off":
                    lightp1[(x, y)] = False
                    if (x, y) in lightp2:
                        if lightp2[(x, y)] > 0:
                            lightp2[(x, y)] -= 1
                        else: 0
                else: # instruction = "toggle"
                    if (x, y) in lightp1:
                        lightp1[(x, y)] = not lightp1[(x, y)]
                    if (x, y) in lightp2:
                        lightp2[(x, y)] += 2
                    else:
                        lightp1[(x, y)] = True
                        lightp2[(x, y)] = 2

for key, value in lightp1.items():
    if value:
        part1 += value
print("Answer for Part 1:", part1)

for key, value in lightp2.items():
    if value:
        part2 += value
print("Answer for Part 2:", part2)