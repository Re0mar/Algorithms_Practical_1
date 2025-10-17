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
    stages = int(src.readline().split()[0])
    prod = [[] for _ in range(stages)]

    for line in src:
        road = line.split()
        add_edge_to_list(prod, int(road[0]), int(road[1]), int(road[2]))
        edge_count += 1

    return prod, edge_count, stages


def primMST_with_type(adj_list, ignored_types):
    vertex_count = len(adj_list)
    global_mst_adj = [[] for _ in range(vertex_count)]
    global_visited = [False] * vertex_count
    global_edges = set()

    unique_vertex_count = 0
    unique_road_count = 0

    for ignored_types in ignored_types:
        visited = [False] * vertex_count
        heap = [(0, -1, 0, None)]

        while heap:
            weight, parent, u, edge_type = heappop(heap)
            if visited[u]:
                continue
            visited[u] = True

            if not global_visited[u]:
                global_visited[u] = True
                unique_vertex_count += 1

            if parent != -1:
                edge_key = tuple(sorted((parent, u)))
                if edge_key not in global_edges:
                    global_edges.add(edge_key)
                    unique_road_count += 1

                    global_mst_adj[parent].append([u, edge_type])
                    global_mst_adj[u].append([parent, edge_type])

            for v, link_type in adj_list[u]:
                if not visited[v] and link_type not in ignored_types:
                    heappush(heap, (1, u, v, link_type))

    return global_mst_adj, unique_vertex_count, unique_road_count


if __name__ == '__main__':
    testFiles = []

    for file in range(1,41):
        testFiles.append("samples/"+str(file) + ".in")

    for testFile in testFiles:
        #Construct modified adjacency list, with i: [j,transport]
        road_adj_list, road_count, stage_count = constructRoadList(testFile)
        # display_adj_list(road_adj_list)

        # Forms MST, ignores the type provided as second argument, returns an adjacency list
        prim_list_roads, unique_stages, unique_roads = primMST_with_type(road_adj_list,[[0],[1]])

        result = -1

        if stage_count == unique_stages:
            result = road_count - unique_roads

        print("Test for "+testFile+", Act_Stage: "+str(unique_stages)+
              ", Exp_Stage"+str(stage_count)+", Form_Roads: "+str(road_count)+
              ", Roads_Left: "+str(unique_roads)+", Roads_Removed: "+str(result))
