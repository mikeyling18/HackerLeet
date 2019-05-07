OBSTACLE = -1
ALREADY_EXPLORED = 2
DIAMOND = 1


class Solution:
    def __init__(self):
        self.num_diamonds = 0

    def max_diamonds(self, mat, row, col):

        # use 2 to show you've explored something
        length = len(mat)-1
        width = len(mat[0])-1

        if row < 0 or col < 0 or col > width or row > length or mat[row][col] == OBSTACLE or mat[row][col] == ALREADY_EXPLORED:
            return
        if mat[row][col] == DIAMOND:
            self.num_diamonds += 1
        mat[row][col] = ALREADY_EXPLORED

        # explore the rest of the current path
        self.max_diamonds(mat, row, col + 1)
        self.max_diamonds(mat, row, col - 1)
        self.max_diamonds(mat, row + 1, col)
        self.max_diamonds(mat, row - 1, col)
        return


def main():
    m = [[0,1],
         [-1,1]]

    sol = Solution()
    sol.max_diamonds(m, 0, 0)
    print(sol.num_diamonds)


if __name__ == '__main__':
    main()
