import re


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




