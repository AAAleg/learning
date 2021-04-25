class Queue:
    def __init__(self):
        self.items = []
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, item):
        self.items.insert(0, item)
        self._size += 1

    def dequeue(self):
        if not self.isEmpty():
            self._size -= 1
            return self.items.pop()
        return None 

    def size(self):
        return self._size

    def rotate(self, n):
        if not self.isEmpty():
            for _ in range(n):
                self.enqueue(self.dequeue())


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

    def BreadthFirstSearch(self, VFrom, VTo):
        self.clear_vertices()

        queue = Queue()
        current = VFrom
        route = {}
        self.visit(VFrom)

        while True:
            for vertex in self.get_unvisited_vertices(current):
                self.visit(vertex)
                route[vertex] = current

                if vertex == VTo:
                    return self.build_route(route, VFrom, VTo)

                queue.enqueue(vertex)

            if queue.size() != 0:
                current = queue.dequeue()
                continue
            
            return []

    def WeakVertices(self):
        self.clear_vertices()

        result = []

        for v in range(self.max_vertex):
            if self.is_visited(v):
                continue

            triangles = self.get_triangles(v)

            if not triangles:
                result.append(v)

            else:
                self.visit(*(v for triangle in triangles for v in triangle))

        return [self.vertex[index] for index in result]

    def get_index(self, v):
        return self.vertex.index(v)

    def clear_vertices(self):
        for vertex in self.vertex:
            if vertex is not None:
                vertex.Hit = False

    def visit(self, *vertices):
        for vertex in vertices:
            self.vertex[vertex].Hit = True

    def get_edges(self, v):
        return {v2 for v2 in range(self.max_vertex) if self.IsEdge(v, v2)}

    def is_visited(self, v):
        return self.vertex[v].Hit

    def get_unvisited_vertices(self, v):
        return [v for v in self.get_edges(v) if not self.is_visited(v)]

    def build_route(self, route, VFrom, VTo):
        current = VTo
        path = [current]
        while current != VFrom:
            current = route[current]
            path.append(current)
        return [self.vertex[index] for index in reversed(path)]

    def get_triangles(self, v):
        edges = self.get_edges(v)
        for v1 in edges:
            v1_edges = self.get_edges(v1)
            intersection = set(v1_edges).intersection(edges)
            if intersection:
                return [(v, v1, v2) for v2 in intersection]

        return []
