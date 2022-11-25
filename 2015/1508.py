with open("1508input.txt") as file:

    literal = 0
    esc_quote = 0
    in_memory = 0
    new_encoded = 0

    for line in file:
        literal += len(line)
        memory = 0
        encoded = 2
        char = 0
        esc_quote += 2

        while char < len(line):
            memory += 1
            if line[char] == '\\':
                if line[char + 1] == 'x':
                    char += 4
                else:
                    char += 2
            else:
                char += 1
                
        in_memory += memory

        for character in line:
            if character in ('\\', '"'):
                encoded += 2
            else:
                encoded += 1

        new_encoded += encoded


part1 = literal + esc_quote - in_memory
part2 = new_encoded - literal

print("Answer for Part 1:", part1)
print("Answer for Part 2:", part2)