#!/usr/bin/env python3
"""Hungarian algorithm — optimal assignment in bipartite graphs."""
import sys

def hungarian(cost):
    n = len(cost); m = len(cost[0])
    u = [0]*(n+1); v = [0]*(m+1); p = [0]*(m+1); way = [0]*(m+1)
    for i in range(1, n+1):
        p[0] = i; j0 = 0
        minv = [float('inf')]*(m+1); used = [False]*(m+1)
        while True:
            used[j0] = True; i0 = p[j0]; delta = float('inf'); j1 = 0
            for j in range(1, m+1):
                if not used[j]:
                    cur = cost[i0-1][j-1] - u[i0] - v[j]
                    if cur < minv[j]: minv[j] = cur; way[j] = j0
                    if minv[j] < delta: delta = minv[j]; j1 = j
            for j in range(m+1):
                if used[j]: u[p[j]] += delta; v[j] -= delta
                else: minv[j] -= delta
            j0 = j1
            if p[j0] == 0: break
        while j0:
            p[j0] = p[way[j0]]; j0 = way[j0]
    assignment = [0]*n
    for j in range(1, m+1):
        if p[j]: assignment[p[j]-1] = j-1
    total = sum(cost[i][assignment[i]] for i in range(n))
    return assignment, total

if __name__ == "__main__":
    cost = [[9,2,7,8],[6,4,3,7],[5,8,1,8],[7,6,9,4]]
    assignment, total = hungarian(cost)
    print("Cost matrix:")
    for row in cost: print(f"  {row}")
    print(f"\nOptimal assignment: {assignment}")
    print(f"Assignments: {[(i, assignment[i], cost[i][assignment[i]]) for i in range(len(cost))]}")
    print(f"Total cost: {total}")
