import numpy as np

actions = []

with open('1506input.txt') as indata:
    for line in indata:
        line = line.replace('turn ','')
        op, start, _, end = line.split()
        
        sx, sy = start.split(',')
        ex, ey = end.split(',')
        action = {
            'op': op,
            'start': [int(sx), int(sy)],
            'end': [int(ex), int(ey)]
        }
        actions.append(action)


grid = np.zeros((1000,1000))

for action in actions:
    x1, y1 = action['start']
    x2, y2 = action['end']
    x2 += 1
    y2 += 1
    if action['op'] == 'on':
        grid[x1:x2, y1:y2] = 1
    elif action['op'] == 'off':
        grid[x1:x2, y1:y2] = 0
    elif action['op'] == 'toggle':
        grid[x1:x2, y1:y2] = (np.logical_not(grid[x1:x2, y1:y2])
                                .astype(int))

print(np.sum(grid))
