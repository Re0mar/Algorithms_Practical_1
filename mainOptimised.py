import sys

class DisjointSet:
    __slots__ = ("parent", "rank", "components")

    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

        self.components -= 1
        return True


def optRoadRemovalForFile(road_list):
    split = road_list.split()
    stages = int(split[0])

    disjoint_foot = DisjointSet(stages)
    disjoint_bus = DisjointSet(stages)
    used_road_count = 0

    # Forming the lists of roads
    twin_roads = []
    single_roads = []

    # Assuming file has n + x numbers in it, with n=2 and x / 3 = number of roads
    data = split[2:]
    for i in range(0, len(data), 3):
        a = int(data[i])
        b = int(data[i + 1])
        t = int(data[i + 2])
        if t == 2:
            twin_roads.append((a, b))
        else:
            single_roads.append((a, b, t))

    if int(split[1]) != (len(twin_roads) + len(single_roads)):
        return -1

    # Using as many double usable roads as possible for efficiency
    # Essentially going over every double use road and checking it, forming a sort of base grid that both parties then branch off of
    for s,e in twin_roads:
        if disjoint_foot.union(s, e) | disjoint_bus.union(s, e):
            used_road_count += 1

    # Checking if we've already finished so we can skip the remainder
    if disjoint_foot.components == 1 and disjoint_bus.components == 1:
        return len(twin_roads) + len(single_roads) - used_road_count

    # Checking the individual roads we need to add
    # Essentially going from the base grid we just made to all yet unreached stages, adding roads as we do
    for s,e,t in single_roads:
        if t == 0: # Usable by feet
            if disjoint_foot.union(s, e):
                used_road_count += 1
        if t == 1: # Usable by wheel
            if disjoint_bus.union(s, e):
                used_road_count += 1

    # Checking if both sets are still 'complete' and thus valid
    if disjoint_foot.components != 1 or disjoint_bus.components != 1:
        return -1

    # Returning total roads - roads used to get the amount we can remove
    return len(twin_roads)+len(single_roads) - used_road_count


if __name__ == '__main__':
    text = sys.stdin.read()
    print(optRoadRemovalForFile(text))
