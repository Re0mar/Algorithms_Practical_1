class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.components = n

    # Finding something in our disjoint set, only used by union
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Checking if we can unionize something in the set, returns True if we can and False otherwise, reducing our count as we go
    # Forms backbone of algorithm cause if we can unionize something out of the total set of roads we removed a road, bringing us closer to the total
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        self.parent[y_root] = x_root
        self.components -= 1
        return True


def optRoadRemovalForFile(road_file):
    # Opening file
    #TODO: Should try to read whole file as one, split on space and newline, ignore [0],[1], loop on i <= (len-2)/3, then take i, i+1, i+2 for the input road things
    src = open(road_file) 
    split = open(road_file, 'r').read().split()
    stages = int(split[0])

    disjoint_foot = DisjointSet(stages)
    disjoint_bus = DisjointSet(stages)
    used_road_count = 0

    # Forming the lists of roads
    twin_roads = []
    single_roads = []

    # Assuming file has n + x numbers in it, with n=2 and x / 3 = number of roads
    for i in range(0,int((len(split)-2)/3)):
        loc = 2 + i*3

        if split[loc+2] == '2': # Comparing chars might be cheaper than casting to integer each time before compare
            twin_roads.append([int(split[loc]), int(split[loc+1]), int(split[loc+2])])
        else:
            single_roads.append([int(split[loc]), int(split[loc+1]), int(split[loc+2])])

    # Using as many double usable roads as possible for efficiency
    # Essentially going over every double use road and checking it, forming a sort of base grid that both parties then branch off of
    for road in twin_roads:
        if road[2] == 2: # Usable by both feet and wheel
            if disjoint_foot.union(road[0], road[1]) | disjoint_bus.union(road[0], road[1]):
                used_road_count += 1

    # Checking the individual roads we need to add
    # Essentially going from the base grid we just made to all yet unreached stages, adding roads as we do
    for road in single_roads:
        if road[2] == 0: # Usable by feet
            if disjoint_foot.union(road[0], road[1]):
                used_road_count += 1
        if road[2] == 1: # Usable by wheel
            if disjoint_bus.union(road[0], road[1]):
                used_road_count += 1

    # Checking if both sets are still 'complete' and thus valid
    if disjoint_foot.components != 1 or disjoint_bus.components != 1:
        return -1

    # Returning total roads - roads used to get the amount we can remove
    return len(twin_roads)+len(single_roads) - used_road_count


if __name__ == '__main__':
    testFiles = []
    for file in range(1,41):
        testFiles.append(["samples/"+str(file) + ".in", int(open("samples/"+str(file)+ ".ans").readline().split()[0])])

    for file in testFiles:
        output = optRoadRemovalForFile(file[0])
        print(file[0] + ", Output: " +str(output) + ", Expected: " +str(file[1])+ ", Succeeded: " + str(output==file[1]))
