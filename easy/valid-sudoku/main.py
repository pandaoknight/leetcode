# -*- coding: utf-8 -*-
# description: 数独判断输入是否有效，不用解
# 那么也就3个判断：横（row），竖（column），一个块儿（square）
# 3个判断的逻辑都是一样的，就是判断9个数是不是有重复。
# 那么，做3个迭代器，然后对结果进行检查。
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #squares = [[]*3]*3
        #return self.notDuplicated(['5', '5'])
        #return self.row(board, 0)
        #return self.col(board, 5)
        #return self.square(board, 6, 6)
        for i in xrange(0,9):
            #if not self.notDuplicated( self.row(board, i) ):
            if self.hasDuplicated( self.row(board, i) ):
                return False

        for i in xrange(0,9):
            if self.hasDuplicated( self.col(board, i) ):
                return False

        for x, y in [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]:
            if self.hasDuplicated( self.square(board, x, y) ):
                return False
        return True

    def notDuplicated(self, iter):
        elements = {}
        for item in iter:
            if '.' == item:
                continue
            if elements.get(item, False):
                return False
            elements[item] = 1
        return True

    def hasDuplicated(self, iter):
        return not self.notDuplicated(iter)

    def row(self, board, y):
        return board[y]

    def col(self, board, x):
        return [row[x] for row in board]

    def square(self, board, x, y):
        return board[y][x:x+3] + board[y+1][x:x+3] + board[y+2][x:x+3]

    def row_iter(self, board, y):
        return []

    def col_iter(self, board, x):
        return []

    def square_iter(self, board, x, y):
        return []

if "__main__" == __name__:
    s = Solution()

    board = [
                ['5', '3', '.',  '.', '7', '.',  '.', '.', '.'],
                ['6', '.', '.',  '1', '9', '5',  '.', '.', '.'],
                ['.', '9', '8',  '.', '.', '.',  '.', '6', '.'],

                ['8', '.', '.',  '.', '6', '.',  '.', '.', '3'],
                ['4', '.', '.',  '8', '.', '3',  '.', '.', '1'],
                ['7', '.', '.',  '.', '2', '.',  '.', '.', '6'],

                ['.', '6', '.',  '.', '.', '.',  '2', '8', '.'],
                ['.', '.', '.',  '4', '1', '9',  '.', '.', '5'],
                ['.', '.', '.',  '.', '8', '.',  '.', '7', '9'],
            ]
    print board
    print s.isValidSudoku(board)
    print "True is expected"

    # fail on row
    board = [
                ['5', '3', '.',  '.', '7', '.',  '.', '.', '.'],
                ['6', '.', '.',  '1', '9', '5',  '.', '.', '.'],
                ['.', '9', '8',  '.', '.', '.',  '.', '6', '.'],

                ['8', '.', '.',  '.', '6', '.',  '.', '.', '3'],
                ['4', '.', '.',  '8', '.', '3',  '.', '.', '1'],
                ['7', '.', '.',  '.', '2', '.',  '.', '.', '2'], # fail on row

                ['.', '6', '.',  '.', '.', '.',  '2', '8', '.'],
                ['.', '.', '.',  '4', '1', '9',  '.', '.', '5'],
                ['.', '.', '.',  '.', '8', '.',  '.', '7', '9'],
            ]
    print board
    print s.isValidSudoku(board)
    print "False is expected, fail on row"

    # fail on col
    board = [
                ['5', '3', '.',  '.', '7', '.',  '.', '.', '.'],
                ['6', '.', '.',  '1', '9', '5',  '.', '.', '.'],
                ['.', '9', '8',  '.', '.', '.',  '.', '6', '.'],

                ['8', '.', '.',  '.', '6', '.',  '.', '.', '3'],
                ['4', '.', '.',  '8', '.', '3',  '.', '.', '1'],
                ['7', '.', '.',  '.', '2', '.',  '.', '.', '9'], # fail on col

                ['.', '6', '.',  '.', '.', '.',  '2', '8', '.'],
                ['.', '.', '.',  '4', '1', '9',  '.', '.', '5'],
                ['.', '.', '.',  '.', '8', '.',  '.', '7', '9'],
            ]
    print board
    print s.isValidSudoku(board)
    print "False is expected, fail on col"

    # fail on square
    board = [
                ['5', '3', '.',  '.', '7', '.',  '.', '.', '.'],
                ['6', '.', '.',  '1', '9', '5',  '.', '.', '.'],
                ['.', '9', '8',  '.', '.', '.',  '.', '6', '.'],

                ['8', '.', '.',  '.', '6', '.',  '.', '.', '3'],
                ['4', '.', '.',  '8', '.', '3',  '.', '.', '1'],
                ['7', '.', '.',  '.', '2', '.',  '.', '.', '6'],

                ['.', '6', '.',  '.', '.', '.',  '2', '8', '.'],
                ['.', '.', '.',  '4', '1', '9',  '.', '.', '5'],
                ['.', '.', '.',  '.', '8', '.',  '.', '7', '2'], # fail on square
            ]
    print board
    print s.isValidSudoku(board)
    print "False is expected, fail on square"
