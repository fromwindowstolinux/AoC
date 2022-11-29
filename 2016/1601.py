from pprint import pprint

directions = []
count = 0

# iterate, if diff add, same minus

with open("1601input.txt") as file:
    for line in file:
        # pprint(line)
        rep = line.replace(",","")
        str = rep.strip()
        instruction = str.split()
        # pprint(instruction)

    for item in instruction:
        turn = item[0]
        step = item[1:]
        direction = {
            "turn": turn,
            "step": int(step)
            }
        directions.append(direction)
        # pprint(directions)

for direction in directions:

    if direction["turn"] == direction["turn"]:
        count += direction["step"]
    else:
        count -= direction["step"]

print(count)