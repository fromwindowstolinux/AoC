# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

crates = [
    ['Z','N'],      # 1
    ['M','C','D'],  # 2
    ['P'],          # 3
]

with open("test.txt") as file:
    for line in file:
        if not line.startswith('move'):
            continue

        number = line.replace("move","").replace("from", "").replace("to", "").split()
        quantity, from_crate, to_crate = number
        
        for _ in range(1, int(quantity)):
            crates[int(from_crate)-1].append(crates[int(to_crate)-1].pop()) 
            
        print(crates)

            







# crates = [
#     ['F','H','B','V','R','Q','D','P'],  # 1
#     ['L','D','Z','Q','W','V'],          # 2
#     ['H','L','Z','Q','G','R','P','C'],  # 3
#     ['R','D','H','F','J','V','B'],      # 4
#     ['Z','W','L','C'],                  # 5
#     ['J','R','P','N','T','G','V','M'],  # 6
#     ['J','R','L','V','M','B','S',],     # 7
#     ['D','P','J'],                      # 8
#     ['D','C','N','W','V'],              # 9    
# ]