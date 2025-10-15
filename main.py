from heapq import heappush, heappop

def display_adj_list(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(j[0], end=" ")
        print()

class Heap():

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def createMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    def generateMinHeap(self, nodeIndex):
        smallest = nodeIndex
        left = 2 * nodeIndex + 1
        right = 2 * nodeIndex + 2

        if left < self.size and self.array[left][1] < \
                self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < \
                self.array[smallest][1]:
            smallest = right

        if smallest != nodeIndex:
            self.pos[self.array[smallest][0]] = nodeIndex
            self.pos[self.array[nodeIndex][0]] = smallest

            self.swapMinHeapNode(smallest, nodeIndex)
            self.generateMinHeap(smallest)

    def extractMin(self):

        if self.isEmpty() == True:
            return

        root = self.array[0]

        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        self.size -= 1
        self.generateMinHeap(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):
        i = self.pos[v]

        self.array[i][1] = dist

        while i > 0 and self.array[i][1] < \
                self.array[(i - 1) // 2][1]:
            self.pos[self.array[i][0]] = (i - 1) / 2
            self.pos[self.array[(i - 1) // 2][0]] = i
            self.swapMinHeapNode(i, (i - 1) // 2)

            i = (i - 1) // 2

    def isInMinHeap(self, v):

        if self.pos[v] < self.size:
            return True
        return False



# 0: no route, 0:foot, 1:bus, 2:both
def add_edge_to_list(adj, i, j, transport):
    adj[i].append([j,transport])
    adj[j].append([i,transport])


def constructRoadList(src):
    src = open(src)
    edge_count = 0
    stages = int(src.readline()[4:].split()[0])
    prod = [[] for _ in range(stages)]

    for line in src:
        road = line.split()
        add_edge_to_list(prod, int(road[0]), int(road[1]), int(road[2]))
        edge_count += 1

    return prod, edge_count, stages


def primMST_with_type(adj_list, ignored_type):
    vertex_count = len(adj_list)
    visited = [False] * vertex_count
    mst_adj_list = [[] for _ in range(vertex_count)]
    unique_vertex_count = 0
    unique_road_count = 0

    heap = [(0, -1, 0, None)]

    while heap:
        weight, parent, u, edge_type = heappop(heap)
        if visited[u]:
            continue
        visited[u] = True

        if parent != -1:
            mst_adj_list[parent].append([u, edge_type])
            mst_adj_list[u].append([parent, edge_type])
            unique_vertex_count += 1
            unique_road_count += 1

        for neighbor_entry in adj_list[u]:
            v, link_type = neighbor_entry
            if not visited[v] and link_type != ignored_type:
                heappush(heap, (1, u, v, link_type))

    return mst_adj_list, unique_vertex_count, unique_road_count


if __name__ == '__main__':
    testFiles = ["testset1.txt"]

    #Construct modified adjacency list, with i: [j,transport]
    road_adj_list, road_count, stage_count = constructRoadList(testFiles[0])
    display_adj_list(road_adj_list)

    # Forms MST, ignores the type provided as second argument, returns an adjacency list
    prim_list_roads_foot, unique_foot_stages, unique_foot_roads = primMST_with_type(road_adj_list,1)
    prim_list_roads_bus, unique_bus_stages, unique_bus_roads= primMST_with_type(road_adj_list,1)

    print(stage_count)
    print(unique_foot_stages)
    print(unique_bus_stages)

    print(road_count)
    print(unique_foot_roads)
    print(unique_bus_roads)

    if stage_count == unique_foot_stages and stage_count == unique_bus_stages:
        print(road_count-unique_foot_roads-unique_bus_roads)
    else:
        print(-1)
