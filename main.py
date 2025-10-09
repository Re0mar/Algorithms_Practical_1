import re
from sys import maxsize


# 0: no route, 1:foot, 2:bus, 3:both
def add_edge(matrix, i, j, transweight):
    matrix[i][j] = transweight + 1
    matrix[j][i] = transweight + 1


def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def constructRoadMatrix(src):
    src = open(src)
    stagecount = int(src.readline()[4:].split()[0])
    mat = [[0] * stagecount for _ in range(stagecount)]

    for line in src:
        road = line.split()
        add_edge(mat, int(road[0]), int(road[1]), int(road[2]))

    return mat


def bfs(adj):
    V = len(adj)
    res = []
    s = 0
    from collections import deque
    q = deque()
    visited = [False] * V
    visited[s] = True
    q.append(s)

    while q:

        curr = q.popleft()
        res.append(curr)

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

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

    # Constructs adjacency matrix without weights, values inside are the type of transport
    roadMatrix = constructRoadMatrix(testFiles[0])
    display_matrix(roadMatrix)


    mockAdjList = [
        [1, 2], # 0
        [0, 3, 4], # 1
        [0, 4], # 2
        [1], # 3
        [1, 2] # 4
    ]

    PrimMST(mockAdjList)

