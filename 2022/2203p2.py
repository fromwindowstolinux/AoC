letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
part2 = 0
badges = []
group = 0

with open("2203input.txt") as file:   
    content = file.readlines()
    while True:
        text = content[0+group:3+group]
        for chara in letters:
            if (chara in text[0]) and (chara in text[1]) and (chara in text[2]):
                badges.append(chara)
        group += 3    
        if group == 300:
            break

for badge in badges:
    priorities2 = letters.index(badge) + 1
    part2 += priorities2

print("Answer for Part 2:", part2)