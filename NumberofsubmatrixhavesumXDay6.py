from typing import List

class Solution:
    def countSquare(self, mat: List[List[int]], x: int) -> int:
        n = len(mat)
        m = len(mat[0]) if n else 0
        if n == 0 or m == 0:
            return 0

        ps = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            row_sum = 0
            for j in range(m):
                row_sum += mat[i][j]
                ps[i+1][j+1] = ps[i][j+1] + row_sum

        def square_sum(i: int, j: int, s: int) -> int:
            r2, c2 = i + s, j + s
            return ps[r2][c2] - ps[i][c2] - ps[r2][j] + ps[i][j]

        ans = 0
        lim = min(n, m)
        for s in range(1, lim + 1):
            ni = n - s + 1
            nj = m - s + 1
            for i in range(ni):
                for j in range(nj):
                    if square_sum(i, j, s) == x:
                        ans += 1
        return ans