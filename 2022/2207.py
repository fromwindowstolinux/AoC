current_directory = []
is_ls = False
dir_size = {}

with open("2207input.txt") as file:
    for line in file:
        line = line.split()
        # print(line)       
        if "$" in line[0]:
            is_ls = False
            if "cd" in line[1]:
                if "/" in line[2]:
                    current_directory = ['']
                elif ".." in line[2]:
                    current_directory.pop()
                else:
                    current_directory.append(line[2])
            else:
                is_ls = True
        elif is_ls == True:
            if "dir" in line[0]:
                continue
            else:
                for i in range(len(current_directory)):
                    filesize = int(line[0])
                    dir_id = '/' + '/'.join(current_directory[1:i+1])
                    if dir_id not in dir_size.keys():
                        dir_size[dir_id] = 0
                    dir_size[dir_id] += filesize

    # from pprint import pprint
    # pprint(dir_size)

a = dir_size.values()

part1 = 0
for size in a:
    if size < 100000:
        part1 += size    


total_space = 70000000
space_needed = 30000000
used_space = dir_size['/']
free_space = total_space - used_space
part2 = total_space
for space in a:
  freed = free_space + space
  if freed >= space_needed and space < part2:
    part2 = space

print("Answer for Part 1:", part1)
print("Answer for Part 2:", part2)