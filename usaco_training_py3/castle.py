"""
ID: jeremy.11
LANG: PYTHON3
TASK: castle
"""
fi = open("castle.in")
with open("castle.out", "w") as fo:
    m, n = [int(s) for s in fi.readline().split()]  # grid is n x m
    graph = [[[]]] * n

    # calculate neighbors of (a, b)
    def neighbors(a, b, enc):
        ns = []
        if enc % 2 != 1:
            ns.append((a, b - 1))
        enc //= 2
        if enc % 2 != 1:
            ns.append((a - 1, b))
        enc //= 2
        if enc % 2 != 1:
            ns.append((a, b + 1))
        enc //= 2
        if enc != 1:
            ns.append((a + 1, b))
        return ns

    for i in range(n):
        row = [int(s) for s in fi.readline().split()]
        graph[i] = [neighbors(i, j, row[j]) for j in range(m)]

    graph_fill = [[False] * m for i in range(n)]  # whether vertices have been visited
    num_rooms = 0  # number of rooms
    rep_vertex = [[(-1, -1)] * m for i in range(n)]  # representative vertex for each room
    sizes = [[0] * m for i in range(n)]  # room sizes

    # BFS starting from (a, b)
    def bfs(a, b):
        graph_fill[a][b] = True
        next_vertices = [(a, b)]
        room_size = 0
        while next_vertices:
            cur_vertices = next_vertices
            next_vertices = []
            for ca, cb in cur_vertices:
                rep_vertex[ca][cb] = (a, b)
                room_size += 1
                for na, nb in graph[ca][cb]:
                    if not graph_fill[na][nb]:
                        graph_fill[na][nb] = True
                        next_vertices.append((na, nb))
        sizes[a][b] = room_size

    # BFS until entire grid is filled
    max_size = 0
    for i in range(n):
        for j in range(m):
            if not graph_fill[i][j]:
                num_rooms += 1
                bfs(i, j)
                max_size = max(max_size, sizes[i][j])
            else:
                ri, rj = rep_vertex[i][j]
                sizes[i][j] = sizes[ri][rj]

    # try removing each wall
    wall_size = 0
    best_wall = None

    for j in range(m):
        for i in reversed(range(n)):
            # horizontal walls between (i - 1, j) and (i, j)
            if i > 0 and rep_vertex[i - 1][j] != rep_vertex[i][j]:
                new_size = sizes[i - 1][j] + sizes[i][j]
                if new_size > wall_size:
                    wall_size = new_size
                    best_wall = (str(i + 1), str(j + 1), 'N')  # add 1 for indexing

            # vertical walls between (i, j) and (i, j + 1)
            if j < m - 1 and rep_vertex[i][j] != rep_vertex[i][j + 1]:
                new_size = sizes[i][j] + sizes[i][j + 1]
                if new_size > wall_size:
                    wall_size = new_size
                    best_wall = (str(i + 1), str(j + 1), 'E')  # add 1 for indexing

    fo.write(str(num_rooms) + '\n')
    fo.write(str(max_size) + '\n')
    fo.write(str(wall_size) + '\n')
    fo.write(' '.join(best_wall) + '\n')
