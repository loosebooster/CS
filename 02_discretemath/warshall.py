# 04-3. Warshall Algorithm
# cf) https://www.youtube.com/watch?v=hw-SvAR3Zqg&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=32

INF = int(1e9)

n = int(input("n: "))
m = int(input("m: "))

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# self -> self : 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# A -> B : C
for _ in range(m):
    a, b, c = map(int, input("a, b, c: ").split())
    graph[a][b] = c

# comparing with (a -> b) & (a -> k, k -> b) : update the minimum
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# output
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("Inf", end = " ")
        else:
            print(graph[a][b], end = " ")
    print()
