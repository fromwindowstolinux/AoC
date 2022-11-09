# Day 2: I Was Told There Would Be No Math


# dimension = "2x3x4"

def do(dimension):
    if (dimension == ""):
        return 0
    # 2*l*w + 2*w*h + 2*h*l

    # [0] l - 2 
    # [1] w - 3
    # [2] h - 4

    area = dimension.split('x')
    # print(type(area))
    # print(area)
    d = [int(area[0]), int(area[1]), int(area[2])]
    # a = 2 * int(area[0]) * int(area[1])
    # b = 2 * int(area[1]) * int(area[2])
    # c = 2 * int(area[2]) * int(area[0])
    area2 = 2 *( d[0] * d[1] + d[1] * d[2] + d[0] * d[2] )
    # d.append(a)
    # d.append(b)
    # d.append(c)
    print(d)
    d.sort()
    # print(d)
    print(area2)
    area2 += d[0] * d[1]
    print(area2 )
    return area2
do("2x3x4") # expect 58
do("1x1x10") # expect 43


def santa(answer_part_2 = False):

    with open('1502input.txt') as file:

        content = file.read()
        # floor = 0
        # floor_count = 0
        total=0
        for bracket in content.split("\n"):
            total+=do(bracket)
            # if bracket == '(':
            #     floor += 1
            # elif bracket == ')':
            #     floor -= 1
            # floor_count += 1

            # if answer_part_2:
            #     if floor == -1:
            #         print("Part 2 answer:", floor_count)
            #         return
        print(total)
        # print("Part 1 answer:", floor)
    
santa()
# santa(answer_part_2 = True)
