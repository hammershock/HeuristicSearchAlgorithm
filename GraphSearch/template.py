class Graph:
    def __init__(self, vertices, links):
        self.vertices = vertices
        self.links = links


def dfs(graph, start_vertex):

    def dfs_recursive(graph, v, visited):
        visited[v] = True
        print(v, end=' ')

        for neighbour in graph[v]:
            if not visited[neighbour]:
                dfs_recursive(graph, neighbour, visited)

    visited = {v: False for v in graph.keys()}
    dfs_recursive(graph, start_vertex, visited)


def bfs(graph, start_vertex):
    def bfs_queue(graph, start_vertex, visited):
        # 创建一个队列用于BFS
        queue = []
        # 把开始节点标记为已访问并入队
        visited[start_vertex] = True
        queue.append(start_vertex)

        while queue:
            # 出队一个顶点并打印它
            v = queue.pop(0)
            print(v, end=' ')

            # 从当前顶点v出发，访问所有与其相邻的顶点
            for neighbour in graph[v]:
                if not visited[neighbour]:
                    # 标记节点并入队
                    visited[neighbour] = True
                    queue.append(neighbour)

    visited = {v: False for v in graph.keys()}
    bfs_queue(graph, start_vertex, visited)


if __name__ == "__main__":
    g = {1: [2, 3, 4], 2: [1, 6, 7], 3: [5, 7], 4: [2, 7], 5: [1, 2, 4], 6: [2, 5], 7: [4, 5]}
    bfs(g, 1)
    dfs(g, 1)
