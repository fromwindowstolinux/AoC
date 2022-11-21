import re

re_vowel = re.compile(r'([aeiou].*){3,}')
re_twice = re.compile(r'(.)\1')
re_none = re.compile(r'ab|cd|pq|xy')
re_pair = re.compile(r'(..).*\1')
re_repeat = re.compile(r'(.).\1')


with open("1505input.txt") as file:

    content = file.readlines()

    part1 = 0
    part2 = 0

    for line in content:
    
        if (re_vowel.search(line) and re_twice.search(line) and not re_none.search(line)):
            part1 += 1

        if (re_pair.search(line) and re_repeat.search(line)):
            part2 += 1

    print("Answer Part 1 is:", part1)
    print("Answer Part 2 is:", part2)