from pandas import read_csv
import numpy as np

# input format:
# n - the number of nodes in the graph
# g - the adjacency matrix containing {0,1} where 1 represents an edge.

#to_numpy extracts from pandas DataFrame.
# 0 because pandas reads csv as 2d array.

adjacency_matrix =  read_csv("adjacency_matrix.csv", header=None).to_numpy() 
labels = read_csv("labels_matching_adjacency_matrix.csv", header=None).to_numpy()[0] 
n = len(labels)

def solve(s: int):
    q = [] # queue data structure with enqueue = .append() and dequeue = .pop(0)
    q.append(s)

    visited = [False] * n
    visited[s] = True

    prev = [-1] * n

    while q:
        node = q.pop(0)
        
        # get neighbours
        neighbours = []
        for i, e in enumerate(adjacency_matrix[node]):
            if(e):
                neighbours.append(i)
        
        for Next in neighbours:
            if not visited[Next]:
                q.append(Next)
                visited[Next] = True
                prev[Next] = node
    
    return prev

def reconstruct_path(prev, s, e):
    if(prev[e] == -1):
        return []
    else:
        current = e
        path = []
        while(current != s):
            path.append(current)
            current = prev[current]
        path.append(s)
        path.reverse()
        return path
# reconstruct path does not work.


def breadth_first_search(s,e):
    # do a bfs starting at node s
    prev = solve(s)

    # return the reconstructed path from s->e
    return reconstruct_path(prev,s,e)
    
print(breadth_first_search(0,12))