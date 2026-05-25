class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        m = len(matrix)
        n = len(matrix[0])

        self.p = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                top = self.p[i-1][j] if i > 0 else 0

                left = self.p[i][j-1] if j > 0 else 0

                d = self.p[i-1][j-1] if i > 0 and j > 0 else 0

                self.p[i][j] = matrix[i][j] + top + left - d


    def sumRegion(self, row1: int, col1: int,
                  row2: int, col2: int) -> int:

        ans = self.p[row2][col2]

        if row1 > 0:
            ans -= self.p[row1-1][col2]

        if col1 > 0:
            ans -= self.p[row2][col1-1]

        if row1 > 0 and col1 > 0:
            ans += self.p[row1-1][col1-1]

        return ans