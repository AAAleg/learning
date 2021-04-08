class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
  
class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        index = self.vertex.index(None)
        self.vertex[index] = Vertex(v)

    def RemoveVertex(self, v):
        self.vertex[v] = None
        for i in range(0, self.max_vertex):
            self.m_adjacency[v][i] = 0
            self.m_adjacency[i][v] = 0

    def IsEdge(self, v1, v2):
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom, VTo):
        self.clear_vertices()
        path = []
        current = VFrom

        while True:
            self.visit(current)
            path.append(current)

            if self.IsEdge(current, VTo):
                self.visit(VTo)
                path.append(VTo)
                return [self.vertex[v] for v in path]

            unvisited = self.get_unvisited_vertices(current)
            if unvisited:
                current = unvisited[0]
                continue

            path.pop()
            if path:
                current = path.pop()
            else:
                return []

    def clear_vertices(self):
        for vertex in self.vertex:
            if vertex is not None:
                vertex.Hit = False

    def visit(self, v):
        self.vertex[v].Hit = True

    def get_edges(self, v):
        return {v2 for v2 in range(self.max_vertex) if self.IsEdge(v, v2)}

    def is_visited(self, v):
        return self.vertex[v].Hit

    def get_unvisited_vertices(self, v):
        return [v for v in self.get_edges(v) if not self.is_visited(v)]
