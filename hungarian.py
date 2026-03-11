#!/usr/bin/env python3
"""Hungarian Algorithm — optimal assignment in O(n³)."""
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
    result = [0]*n
    for j in range(1, m+1):
        if p[j]: result[p[j]-1] = j-1
    return result, -v[0]

if __name__ == "__main__":
    cost = [[82,83,69,92],[77,37,49,92],[11,69,5,86],[8,9,98,23]]
    assignment, total = hungarian(cost)
    print(f"Assignment: {assignment}")
    print(f"Total cost: {total}")
    for i, j in enumerate(assignment): print(f"  Worker {i} → Job {j} (cost {cost[i][j]})")
