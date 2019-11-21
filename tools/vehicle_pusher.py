file_path = "../config/roadnet_manhattan.json"
import json
import itertools
json_roadnet = json.load(open(file_path))
intersections = json_roadnet["intersections"]
virtual = [x['id'] for x in intersections if x['virtual']]
# print(intersections)

roads = json_roadnet["roads"]
start_roads = [x['id'] for x in roads if x['startIntersection'] in virtual]
end_roads = [x['id'] for x in roads if x['endIntersection'] in virtual]
roads_name = [x['id'] for x in roads]
# start_roads = [
#     "22927373#0"
# ]
# end_roads = [
#     "25166922"
# ]
# print(roads[0])
# od_pair = list(itertools.product(start_roads, end_roads))
od_pair = list(itertools.product(roads_name, roads_name))

# od_pair_update=[]
#

# def dij(a, b):
#     v=roads_name.copy()
#     d={x:float("inf")/3 for x in roads}
#     while len(v)>0:
#         shortest = float("inf")
#         for i in v:
#             if d[i] < shortest:
#                 shortest = d[i]
#                 shortest_r = i
#         v.remove(shortest_r)
#         end_inter = roads[shortest_r]["endIntersection"]
#         neighbour = intersections[end_inter]["roads"]


# for x in od_pair:
import random
od_pair_sample = random.sample(od_pair, 2000)
print(len(od_pair))
flow = [
    {
        "vehicle": {
            "length": 5.0,
            "width": 2.0,
            "maxPosAcc": 2.0,
            "maxNegAcc": 4.5,
            "usualPosAcc": 2.0,
            "usualNegAcc": 4.5,
            "minGap": 2.5,
            "maxSpeed": 16.67,
            "headwayTime": 1.5
        },
        "route":x,
        "interval": 5.0,
        "startTime": random.randint(0,100),
        "endTime": -1
    }
    for x in od_pair_sample
]

json.dump(flow, open("../config/flow_manhattan_dense.json", "w"))