import copy
 
crates1 = [
    ['F','H','B','V','R','Q','D','P'],  # 1
    ['L','D','Z','Q','W','V'],          # 2
    ['H','L','Z','Q','G','R','P','C'],  # 3
    ['R','D','H','F','J','V','B'],      # 4
    ['Z','W','L','C'],                  # 5
    ['J','R','P','N','T','G','V','M'],  # 6
    ['J','R','L','V','M','B','S',],     # 7
    ['D','P','J'],                      # 8
    ['D','C','N','W','V'],              # 9    
]

crates2 = copy.deepcopy(crates1) 

with open("2205input.txt") as file:
    for line in file:
        if not line.startswith('move'):
            continue

        number = line.replace("move","").replace("from", "").replace("to", "").split()
        quantity, from_crate, to_crate = number

        crate = {
            "move": int(quantity),
            "from": int(from_crate),
            "to": int(to_crate)
        }

        for _ in range(crate["move"]):
            popped = crates1[crate["from"]-1].pop()
            crates1[crate["to"]-1].append(popped)

        right = crates2[crate["from"]-1][-1*crate["move"]:]
        left = crates2[crate["from"]-1][:-1*crate["move"]]
        crates2[crate["from"]-1] = left
        crates2[crate["to"]-1] += right

part1 = ''
for i in crates1:
    part1 += i[-1]

part2 = ''
for i in crates2:
    part2 += i[-1]

print("Answer for Part 1:", part1)
print("Answer for Part 2:", part2)