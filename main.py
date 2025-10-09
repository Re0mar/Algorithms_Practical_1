import re
from sys import maxsize


# 0: no route, 0:foot, 1:bus, 2:both
def add_edge_to_list(adj, i, j, transport):
    adj[i].append([j,transport])
    adj[j].append([i,transport])


def constructRoadList(src):
    src = open(src)
    prod = [[] for _ in range(int(src.readline()[4:].split()[0]))]

    for line in src:
        road = line.split()
        add_edge_to_list(prod, int(road[0]), int(road[1]), int(road[2]))

    return prod

def display_adj_list(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(j[0], end=" ")
        print()


def stage_bfs(adj, transport):
    # create an array to store the traversal
    res = []
    s = 0
    # Create a queue for BFS
    from collections import deque
    q = deque()

    # Initially mark all the vertices as not visited
    visited = [False] * len(adj)

    # Mark source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    if transport == 0:
        while q:
            curr = q.popleft()
            res.append(curr)
            for x in adj[curr]:
                if not visited[x[0]] and x[1] != 1:
                    # print(x, end="")
                    visited[x[0]] = True
                    q.append(x[0])
    elif transport == 1:
        while q:
            curr = q.popleft()
            res.append(curr)
            for x in adj[curr]:
                # print(x, end="")
                if not visited[x[0]] and x[1] != 0:
                    visited[x[0]] = True
                    q.append(x[0])
    return res


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


def PrimMST(adjList):
    vertexCount = len(adjList)
    key = [float('inf')] * vertexCount
    parent = [-1] * vertexCount
    minHeap = Heap()

    for v in range(vertexCount):
        minHeap.array.append(minHeap.createMinHeapNode(v, key[v]))
        minHeap.pos.append(v)

    minHeap.pos[0] = 0
    key[0] = 0
    minHeap.decreaseKey(0, key[0])
    minHeap.size = vertexCount

    while not minHeap.isEmpty():
        newHeapNode = minHeap.extractMin()
        u = newHeapNode[0]

        for v in adjList[u]:
            if minHeap.isInMinHeap(v) and 1 < key[v]:
                key[v] = 1
                parent[v] = u
                minHeap.decreaseKey(v, key[v])

    printArr(parent, vertexCount)

def printArr(parent, n):
    for i in range(1, n):
        print("%d - %d" % (parent[i], i))


if __name__ == '__main__':
    testFiles = ["testset1.txt"]

    #Construct modified adjacency list, with i: [j,transport]
    road_adj_list = constructRoadList(testFiles[0])
    display_adj_list(road_adj_list)

    # 0:foot, 1: bus
    foot_ans = stage_bfs(road_adj_list,0)
    bus_ans = stage_bfs(road_adj_list,1)
    print(foot_ans)
    print(len(foot_ans))
    print(len(bus_ans))




    mockAdjList = [
        [1, 2], # 0
        [0, 3, 4], # 1
        [0, 4], # 2
        [1], # 3
        [1, 2] # 4
    ]

    PrimMST(mockAdjList)

