#!/usr/bin/python3

"""
Solution to Firetruck problem from the 
'From Baylor to Baylor' packet.
"""

from collections import defaultdict

class Node(object):
    def __init__(self, value):
        self.value = value
        self.connections = set()

    def addConnection(self, node):
        self.connections.add(node)


target = int(input())
n1, n2 = map(int, input().split(' ')) # Read in the first pair of nodes
graph = defaultdict(list)

while n1 != 0 and n2 != 0:
    # Fill the graph out
    graph[n1].append(n2)

    # Read in the next pair of nodes
    n1, n2 = map(int, input().split(' '))

# print('\nGraph:')
# for k in graph:
#     print(str(k) + ': ' + str(graph[k]))

# Find all paths
def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

print('\nPaths:')
for path in find_all_paths(graph, 1, target):
    path = [str(x) for x in path]
    print(' '.join(path))



