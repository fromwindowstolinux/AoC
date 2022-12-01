p1, p2, esc = 2, 2, False
for c in open("1508input.txt").read():
    if c == "\n":
        p1, p2 = p1+2, p2+2
    if c == '"' or c == "\\":
        p2 += 1
    if c == "\\" and not esc:
        p1 += 1
        esc = True
        continue
    elif c == "x" and esc:
        p1 += 2
    esc = False
print(p1,p2)