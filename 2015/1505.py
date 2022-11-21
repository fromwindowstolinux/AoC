import re

re_vowel = re.compile(r'([aeiou].*){3,}')
re_twice = re.compile(r'(.)\1')
re_none = re.compile(r'ab|cd|pq|xy')

with open("1505input.txt") as file:

    content = file.readlines()
    ctr = 0

    for line in content:
        if (re_vowel.search(line) and re_twice.search(line) and not re_none.search(line)):
            # print(line)
            ctr += 1
    print(ctr)