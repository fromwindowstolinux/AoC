def delivery(direction):

    present_delivered = 1
    x_coordinate = 0
    y_coordinate = 0
    coordinates = []

    for arrow in direction:

        present_delivered += 1

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

        # print(total_nd)
    return nd
        
def total():

    with open('1503input.txt') as file:

        content = file.read()
        total_nd = delivery(content)
        
        print("Answer for Part 1:", total_nd)

    # print("present delivered:", present_delivered)
    # return present_delivered

if __name__ == "__main__":
    total()
    # assert delivery("^>v<") == 5
    # assert delivery(">") == 2
    # assert delivery("^v^v^v^v^v") == 11