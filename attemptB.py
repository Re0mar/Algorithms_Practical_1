
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        self.parent[y_root] = x_root
        self.components -= 1
        return True


# def optRoadRemoval(n, roads):
#     disjoint_foot = DisjointSet(n)
#     disjoint_bus = DisjointSet(n)
#     used_road_count = 0
#
#     for road in roads:
#         u, v, road_type = road
#         if road_type == 3:
#             if disjoint_foot.union(u, v) | disjoint_bus.union(u, v):
#                 used_road_count += 1
#         if road_type == 1:
#             if disjoint_foot.union(u, v):
#                 used_road_count += 1
#         if road_type == 2:
#             if disjoint_bus.union(u, v):
#                 used_road_count += 1
#
#     if disjoint_foot.components != 1 or disjoint_bus.components != 1:
#         return -1
#
#     return len(roads) - used_road_count

def optRoadRemovalForFile(road_file):
    src = open(road_file)
    stages = int(src.readline().split()[0])

    disjoint_foot = DisjointSet(stages)
    disjoint_bus = DisjointSet(stages)
    used_road_count = 0

    roads = []
    for line in src:
        road = line.split()
        roads.append([int(road[0]), int(road[1]), int(road[2])])

    for road in roads:
        if road[2] == 2: # Usable by both feet and wheel
            if disjoint_foot.union(road[0], road[1]) | disjoint_bus.union(road[0], road[1]):
                used_road_count += 1

    for road in roads:
        if road[2] == 0: # Usable by feet
            if disjoint_foot.union(road[0], road[1]):
                used_road_count += 1
        if road[2] == 1: # Usable by wheel
            if disjoint_bus.union(road[0], road[1]):
                used_road_count += 1

    if disjoint_foot.components != 1 or disjoint_bus.components != 1:
        return -1

    return len(roads) - used_road_count


if __name__ == '__main__':
    testFiles = []
    for file in range(1,41):
        testFiles.append(["samples/"+str(file) + ".in", int(open("samples/"+str(file)+ ".ans").readline().split()[0])])

    for file in testFiles:
        output = optRoadRemovalForFile(file[0])
        print(file[0] + ", Output: " +str(output) + ", Expected: " +str(file[1])+ ", Succeeded: " + str(output==file[1]))
