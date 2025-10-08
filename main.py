import re


def add_edge(matrix, i, j, transweight):
    matrix[i][j] = transweight
    matrix[j][i] = transweight


def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def constructRoadMatrix(src):
    src = open(src)
    stagecount = int(src.readline()[4:].split()[0])
    mat = [[0] * stagecount for _ in range(stagecount)]

    for line in src:
        road = line.split()
        add_edge(mat, int(road[0]), int(road[1]),int(road[2]))

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



if __name__ == '__main__':
    testFiles = ["testset1.txt"]

    #Constructs adjacency matrix without weights, values inside are the type of transport
    roadMatrix = constructRoadMatrix(testFiles[0])
    display_matrix(roadMatrix)


