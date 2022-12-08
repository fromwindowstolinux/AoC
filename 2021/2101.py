list_int = []
item = 0
part1 = 0
part2 = 0
# 2101input
with open("test.txt") as file:
    for line in file:
        convert_int = int(line)
        list_int.append(convert_int)

        if item < len(list_int)-1:
            current_item = list_int[item]
            next_item = list_int[item + 1]
            item += 1

            if next_item > current_item:
                part1 += 1

    

            #     part2 += 1
#increased = sum([1 for i in range(3, len(depths)) if depths[i] > depths[i-3]])

print("Answer for Part 1:", part1)
# print("Answer for Part 2:", part2)