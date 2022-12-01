def do(start, keypad, current):
   
    position = start
    code = ''
    for line in lines:
        for move in line:
            if move == 'R':
                next = [position[0], position[1] + 1]
            elif move == 'L':
                next = [position[0], position[1] - 1]
            elif move == 'D':
                next = [position[0] + 1, position[1]]
            elif move == 'U':
                next = [position[0] - 1, position[1]]

            if next in current:
                position = next

        code += keypad[position[0]][position[1]]

    return code


keypad_layout = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
]

diamond_keypad = [
    ['', '', '1', '', ''],
    ['', '2', '3', '4', ''],
    ['5', '6', '7', '8', '9'],
    ['', 'A', 'B', 'C', ''],
    ['', '', 'D', '', ''],
]

with open('1602input.txt') as file:
    lines = [line.strip() for line in file]

buttons = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
print("Answer for Part 1:", do([1, 1], keypad_layout, buttons))

diamond_button = [[0, 2], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3],[4, 2]]
print("Answer for Part 2:", do([1, 1], diamond_keypad, diamond_button))