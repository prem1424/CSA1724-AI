from collections import deque

def bfs(graph,start):
    visited=set()
    queue=deque([start])
    result=[]

    while queue:
        node=queue.popleft()
        if node not in visited:
            result.append(node)
            visited.add(node)
            queue.extend(graph[node])

    return result
graph ={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
    }
print("BFS Traversal:",bfs(graph, 'A'))
