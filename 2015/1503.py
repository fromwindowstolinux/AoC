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


def santa_robo_delivery(direction):

    santa_x_coordinate = 0
    santa_y_coordinate = 0
    santa_coordinates = []

    robo_x_coordinate = 0
    robo_y_coordinate = 0
    robo_coordinates = []

    ctr = 0

    for arrow in direction:

        is_odd = ctr %2

        if is_odd:

            if arrow == '>':
                santa_x_coordinate += 1
            
            elif arrow == '<':
                santa_x_coordinate -= 1

            elif arrow == '^':
                santa_y_coordinate += 1
            
            elif arrow == 'v':
                santa_y_coordinate -= 1

            santa_c = santa_x_coordinate, santa_y_coordinate
            santa_coordinates.append(santa_c)
        
        else:

            if arrow == '>':
                robo_x_coordinate += 1
            
            elif arrow == '<':
                robo_x_coordinate -= 1

            elif arrow == '^':
                robo_y_coordinate += 1
            
            elif arrow == 'v':
                robo_y_coordinate -= 1

            robo_c = robo_x_coordinate, robo_y_coordinate
            robo_coordinates.append(robo_c)

        ctr += 1

    non_dupe = []
    nd = 0
        
    both = santa_coordinates + robo_coordinates

    for pair in both:    
        if pair not in non_dupe:
            non_dupe.append(pair)
            nd += 1

    return nd


def total():

    with open('1503input.txt') as file:

        content = file.read()
        
        part1 = santa_delivery(content)
        part2 = santa_robo_delivery(content)
        
        print("Answer for Part 1:", part1)
        print("Answer for Part 2:", part2)

if __name__ == "__main__":
    total()