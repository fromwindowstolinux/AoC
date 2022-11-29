from pprint import pprint
from itertools import permutations

places = []
cities = set()

with open("1509input.txt") as file:
    for line in file:
        rep = line.replace("to","").replace("=","")
        str = rep.strip()
        words = str.split()

        doko_kara, doko_made, kyori = words
        place = {
            "from": doko_kara,
            "to": doko_made,
            "distance": int(kyori)
        }
        places.append(place)
        cities.add(doko_kara)

distance = 0
for route in permutations(cities):
    # print(route)
    for j in places:
        # print(j)
        if j["from"] == route[0]:
            distance = j["distance"]
print(route, distance)
    
# test test

# l = [{'from': 'AlphaCentauri', 'to': 'Snowdin'}, {'from': 'AlphaCentauri', 'to': 'Tambi'}]
# l2 = []
# for i in l:
#     li = []
#     start = i["from"]
#     end = i["to"]
#     for j in places:
#         if ((j["from"] == start and j["to"] == end) or 
#             (j["from"] == end and j["to"] == start)):
#             distance = j["distance"]
#     li.append(start)
#     li.append(end)
#     li.append(distance)
#     l2.append(li)
# pprint(l2)