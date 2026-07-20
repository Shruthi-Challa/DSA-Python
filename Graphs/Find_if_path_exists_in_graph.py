class Solution(object):
    def validPath(self, n, edges, source, destination):
        queue = deque([source])
        graph = {}

        for i in range(n):
            graph[i]=[]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        visited.add(source)

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False