#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return c_lib*(n)
    else:
        # making graph for using DFS
        graph = {}
        for i in range(1,n+1):
            graph[i]=[]

        for i in cities:
            a, b = i[0], i[1]
            graph.setdefault(a, []).append(b)
            graph.setdefault(b, []).append(a)

        visited =set()
        g= []
        def dfs(visited, graph, node):
            if node not in visited:
                visited.add(node)
                g.append(node)
                for neighbour in graph[node]:
                    dfs(visited,graph,neighbour)
        ans = [];
        for i in range(1,n+1):
            g=[]
            if i not in visited:
                dfs(visited,graph,i)
                # 'g' is a path. So we can make groups that linked
                ans.append(g)
        cost= 0;
        for i in ans:
            cost += c_lib
            cost += (len(i)-1)*c_road
        for x,y in graph.items():
            if x not in visited:
                cost+=c_lib
        return (cost)





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
