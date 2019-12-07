import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    print(visited.add(root))
    while queue:
        vertex = queue.popleft()
        for neigher in graph[vertex]:
            if neigher not in visited:
                visited.add(neigher)
                queue.append(neigher)

    print(visited)

if __name__ == '__main__':
    graph = {
        0 : [1, 2],
        1 : [2],
        2 : [3],
        3 : [1, 2]
    }
    bfs(graph, 0)
