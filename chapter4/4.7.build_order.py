class Solution:
    def make_graph(self, projects, dependencies):
        graph = {project: set() for project in projects}
        for u, v in dependencies:
            graph[v].add(u)
        return graph

    # Computes in-degree of every vertex
    def compute_indegree(self, graph):
        indegrees = {project: 0 for project in graph.keys()}
        for project, neighbors in graph.items():
            for neigh in neighbors:
                indegrees[neigh] += 1
        return indegrees

    def build_order(self, projects, dependencies):
        G = self.make_graph(projects, dependencies)
        indegrees = self.compute_indegree(G)
        zero_queue = [key for key, degree in indegrees.items() if degree == 0]
        zero_queue.sort()  # This is only for consistency in the test case
        toposort = []
        while zero_queue:
            zero = zero_queue.pop(0)
            toposort.append(zero)
            for neigh in G[zero]:
                indegrees[neigh] -= 1
                if indegrees[neigh] == 0:
                    zero_queue.append(neigh)
        return toposort[::-1] if len(toposort) == len(projects) else []


projects = ["a", "b", "c", "d", "e", "f"]

dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]

solution = Solution()
result = solution.build_order(projects, dependencies)
assert result == ['f', 'b', 'a', 'd', 'e', 'c']
