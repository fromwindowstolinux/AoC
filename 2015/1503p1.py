def santa_delivery(direction):

    x_coordinate = 0
    y_coordinate = 0
    coordinates = []

    for arrow in direction:

        if arrow == '>':
            x_coordinate += 1
        
        elif arrow == '<':
            x_coordinate -= 1

        elif arrow == '^':
            y_coordinate += 1
        
        elif arrow == 'v':
            y_coordinate -= 1

        c = x_coordinate, y_coordinate
        coordinates.append(c)

    non_dupe = []
    nd = 0
        
    for pair in coordinates:    
        if pair not in non_dupe:
            non_dupe.append(pair)
            nd += 1

    return nd
        
def total():

    with open('1503input.txt') as file:

        content = file.read()
        total_nd = santa_delivery(content)
        
        print("Answer for Part 1:", total_nd)

if __name__ == "__main__":
    total()