# Day 1: Not Quite Lisp


def santa(answer_part_2 = False):

    with open('1501_input.txt') as file:

        content = file.read()
        floor = 0
        floor_count = 0
        
        for bracket in content:
        
            if bracket == '(':
                floor += 1
            elif bracket == ')':
                floor -= 1
            floor_count += 1

            if answer_part_2:
                if floor == -1:
                    print("Part 2 answer:", floor_count)
                    return
            
        print("Part 1 answer:", floor)
    
santa()
santa(answer_part_2 = True)
