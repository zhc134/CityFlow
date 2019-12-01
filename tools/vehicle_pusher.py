file_path = "../local/map_xuhui.json"
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
od_pair_sample = random.sample(od_pair, 500)
print(len(od_pair))

vehicle_template = {
    "length": 5.0,
    "width": 2.0,
    "maxPosAcc": 2.0,
    "maxNegAcc": 4.5,
    "usualPosAcc": 2.0,
    "usualNegAcc": 4.5,
    "minGap": 2.5,
    "maxSpeed": 16.67,
    "headwayTime": 1.5
}

flow = [
    {
        "vehicle": vehicle_template,
        "route":x,
        "interval": 50.0,
        "startTime": random.randint(0,100),
        "endTime": -1
    }
    for x in od_pair_sample
]

xjh_flows = [
    ["492977118#4","492977118#6","11960404#2","11960404#3","465149399"],
    ["664078697#8","657311255","492981116#2","492981116#3","50409876#1","50409876#4","50409876#5"],
    ["682286685#2","682286685#3","682286685#4","12272379#0","12272379#1","465128019#0","465128019#1"],
    ["682286685#2","682286685#3","682286685#4","12272375#1","12272375#2","492977121#0"],
    ["50417295#6","12272375#1","12272375#2","492977121#0"],
    ["664078697#8","657311255","492981116#2","492981116#3","12272379#0","12272379#1","12272379#2","654530824#0"],
    ["50417295#4","50417295#5","50417295#6","50409876#1","50409876#4","50409876#5"]
]
for xjh_flow in xjh_flows:
    flow.append({
        "vehicle": vehicle_template,
        "route": xjh_flow,
        "interval": 15.0,
        "startTime": random.randint(0,20),
        "endTime": -1
    })

json.dump(flow, open("../local/flow_xuhui.json", "w"))