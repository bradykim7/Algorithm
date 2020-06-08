#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bfs function below.
def bfs(n, m, edges, s):
    # we will going to stored the fastest path in ans .
    ans =[]
    # DFS , BFS : We should make graph
    graph = {}
    # 'n' is the number of nodes
    # And node start with 1 not 0
    for i in range(1,n+1):
        graph[i] = []

    # actually in python3 we have to set the default setting if we want to 'list' dictionary values
    for i in edges:
        a,b = i[0],i[1]
        graph.setdefault(a,[]).append(b)
        graph.setdefault(b,[]).append(a)
    # We made graph to use search the shortest way to the edge !

    # Now we're going to make bfs function !
    def bfs_ms(graph,start,end):
        visited=[]
        # queue stored path to goal
        queue=[[start]]
        while queue:
            path = queue.pop(0)
            # node would be path's last node so we store the fastest way
            node = path[-1]
            if node not in visited:
                neighbours = graph[node]
                for i in neighbours:
                    new_path = list(path)
                    new_path.append(i)
                    # path updated
                    queue.append(new_path)
                    if i == end:
                        ans.append((len(new_path)-1)*6)
                        return
                visited.append(node)
        ans.append(-1)
    for i in range(1,n+1):
        # s is the starting point so we pass
        if i == s:
            continue;
        else:
            (bfs_ms(graph,s,i))

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
