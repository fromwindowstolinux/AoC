import numpy as np

l1 = np.zeros((1000,1000))
l2 = np.zeros((1000,1000))

with open("input.txt") as file:
    for line in file:
        words = line.replace("turn","").replace(",", " ").replace("through", "").strip().split(" ")
        instruction, x1, y1, f, x2, y2 = words
        x1, x2, y1, y2 = int(x1), int(x2)+1, int(y1), int(y2)+1
        
        if instruction == "on":
            l1[x1:x2, y1:y2] = 1
            l2[x1:x2, y1:y2] += 1
        elif instruction == "off":
            l1[x1:x2, y1:y2] = 0
            l2[x1:x2, y1:y2] -= 1
            np.clip(l2, 0, None, l2)
        else:
            l1[x1:x2, y1:y2] = 1 - l1[x1:x2, y1:y2]
            l2[x1:x2, y1:y2] += 2

print("Answers", int(np.sum(l1)), int(np.sum(l2)))