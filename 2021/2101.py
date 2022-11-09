# Day1 : Sonar Sweep
# Part 1


fh = open("input.txt")
list1 = fh.read().split()
# print(list1)
list2 = []
# cast item in list1 into integer and put it inside list2
for item in list1 :
    cast = int(item)
    # print(cast)
    list2.append(cast)
# print(list2)

# increase
list2_length = len(list2)
i = 0
count = 0
# while you are not at the end of list2
while i < list2_length - 1:
    current_number = list2[i]
    # print(current_number)
    next_number = list2[i + 1]
    i = i + 1
    # print(next_number)
    # compare the current item with the next item.
    if next_number > current_number:
        count = count + 1
        # print("%i->%i is increase" % (current_number, next_number))
print("Total count:", count)