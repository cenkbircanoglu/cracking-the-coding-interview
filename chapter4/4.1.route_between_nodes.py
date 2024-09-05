class Solution:

    def route_between_nodes(self, graph, u, v):
        seen = set()
        queue = [u]

        while queue:
            length = len(queue)

            for _ in range(length):
                node = queue.pop()
                seen.add(node)
                if node == v:
                    return True
                for child in graph[node]:
                    if child not in seen:
                        queue.append(child)
        return False


G = {
    1: [2, 3, 4],
    2: [3, 4],
    3: [1],
    4: [1, 2, 3],
    5: [1, 2, 3, 4]
}

solution = Solution()
assert solution.route_between_nodes(G, 1, 2) == True
assert solution.route_between_nodes(G, 3, 4) == True
assert solution.route_between_nodes(G, 1, 5) == False
assert solution.route_between_nodes(G, 2, 5) == False
