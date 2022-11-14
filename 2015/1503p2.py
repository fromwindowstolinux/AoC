def santa_delivery(direction):

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
        total_nd = santa_delivery(content)
        
        print("Answer for Part 2:", total_nd)

if __name__ == "__main__":
    total()