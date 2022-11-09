# Day 2: I Was Told There Would Be No Math


def wrapper(dimension):

    if (dimension == ""):
        return 0

    size = dimension.split('x')
    d = [int(size[0]), int(size[1]), int(size[2])]
    area = 2 * ( (d[0]*d[1]) + (d[1]*d[2]) + (d[2]*d[0]) )
    d.sort()
    area += d[0] * d[1]
    return area


def ribbon_and_bow(dimension):

    if (dimension == ""):
        return 0

    size = dimension.split('x')
    d = [int(size[0]), int(size[1]), int(size[2])]
    d.sort()
    ribbon = 2 * (d[0] + d[1])
    ribbon += d[0] * d[1] * d[2]
    return ribbon


def total():
    
    with open('1502input.txt') as file:

        content = file.read()
        total_wrapper = 0
        total_ribbon = 0

        for item in content.split("\n"):
            total_wrapper += wrapper(item)
            total_ribbon += ribbon_and_bow(item)

        print("Part 1 answer:", total_wrapper)
        print("Part 2 answer:", total_ribbon)


if __name__ == "__main__":
    total()