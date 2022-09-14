
graph = {'0': set(['1', '2']),
'1': set(['0', '3', '4']),
'2': set(['0']),
'3': set(['1']),
'4': set(['3'])} 
visited =[]  
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue: 
        cur_v = queue.pop(0)
        print(cur_v, end = ' ')

        for neighbour in graph[cur_v]: 
            if neighbour not in visited: 
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, '0')