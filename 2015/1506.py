
counter = 0
light = {}

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
                    light[(x, y)] = True
                elif instruction == "off":
                    light[(x, y)] = False
                else: # instruction = "toggle"
                    if (x, y) in light:
                        light[(x, y)] = not light[(x, y)]
                    else:
                        light[(x, y)] = True

for key, value in light.items():
    if value:
        counter += 1

print(counter)