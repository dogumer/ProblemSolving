INF = 9999999

graph = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

vertices = len(graph)

selected = [False for _ in range(vertices)]
selected[0] = True

while sum(selected) != vertices:
    minimum = INF # initial comparison

    for i in range(vertices):
        if selected[i]:
            for j in range(vertices):
                if (not selected[j]) and graph[i][j]: # not selected and path exists
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(str(x) + "-" + str(y) + ":" + str(graph[x][y]))
    selected[y] = True