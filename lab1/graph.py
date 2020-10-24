
class Graph:

    def __init__(self):
        self.dict = {}

    def add_vertex(self, vertex, edges=None):
        self.dict[vertex] = edges
        if edges:
            for i in edges:
                if self.dict[i] is None:
                    self.dict[i] = [vertex]
                else:
                    self.dict[i].append(vertex)

    def remove_vertex(self, vertex):
        if vertex in self.dict.keys():
            for k, v in self.dict.items():
                if v is not None:
                    for i in v:
                        if vertex == i:
                            self.dict[k].remove(vertex)
            del self.dict[vertex]

    def add_edge(self, vertex1, vertex2):
        if self.dict[vertex1] is None:
            self.dict[vertex1] = [vertex2]
        else:
            self.dict[vertex1].append(vertex2)
        if self.dict[vertex2] is None:
            self.dict[vertex2] = [vertex1]
        else:
            self.dict[vertex2].append(vertex1)

    def del_edge(self, vertex1, vertex2):
        self.dict[vertex1].remove(vertex2)
        self.dict[vertex2].remove(vertex1)

    def get_edges(self, vertex):
        return self.dict[vertex]

    def bfs(self, root):
        visited = [root]
        queue = self.get_edges(root).copy()

        while len(self.dict) != len(visited):
            visited.append(queue[0])
            for n in self.get_edges(queue[0]):
                if n not in visited and n not in queue:
                    queue.append(n)
            queue.pop(0)

        return visited

    def dfs(self, root):
        visited = [root]
        stack = self.get_edges(root).copy()
        while len(self.dict) != len(visited):
            visited.append(stack[-1])
            x = stack.pop()
            for n in self.get_edges(x):
                if n not in visited and n not in stack:
                    stack.append(n)

        return visited


g1 = Graph()

g1.add_vertex("c")
g1.add_vertex("l", ["c"])
g1.add_vertex("b", ["c"])
g1.add_vertex("d", ["b"])
g1.add_vertex("a",  ["l", "c"])

print("### graph:")
print(g1.dict)
print("### bfs")
print(g1.bfs("a"))
print("### dfs")
print(g1.dfs("a"))

