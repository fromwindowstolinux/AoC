# Day 1: Not Quite Lisp


# --- Part One ---

# Santa is trying to deliver presents in a large apartment building, but he 
# can't find the right floor - the directions he got are a little confusing. 
# He starts on the ground floor (floor 0) and then follows the instructions 
# one character at a time.

# An opening parenthesis, (, means he should go up one floor, and a closing 
# parenthesis, ), means he should go down one floor.

# The apartment building is very tall, and the basement is very deep; he will 
# never find the top or bottom floors.

# For example:
# - (()) and ()() both result in floor 0.
# - ((( and (()(()( both result in floor 3.
# - ))((((( also results in floor 3.
# - ()) and ))( both result in floor -1 (the first basement level).
# - ))) and )())()) both result in floor -3.

# To what floor do the instructions take Santa?

# Solution for Day 1 Part 1:

# with open("1501_1_input.txt") as file:
    
#     op = "("
#     cp = ")"

#     for item in file:
#         total_op = item.count(op)
#         total_cp = item.count(cp)

#     floor = total_op - total_cp
#     print(floor)



# --- Part Two ---

# Now, given the same instructions, find the position of the first character 
# that causes him to enter the basement (floor -1). The first character in the 
# instructions has position 1, the second character has position 2, and so on.

# For example:

# - ) causes him to enter the basement at character position 1.
# - ()()) causes him to enter the basement at character position 5.
# - What is the position of the character that causes Santa to first enter the basement?

# Solution for Day 1 Part 2

with open("1501_1_input.txt") as file:
    b = ")"
    for item in file:
        if item == b:
            print(item)
