'''
Date: 2022-10-26 15:13:54
LastEditors: yuhhong
LastEditTime: 2022-10-26 17:41:54
'''
from sudoku import Sudoku

if __name__ == "__main__":
    example = Sudoku(path='./puzzle010.txt')

    example.show_board()

    example.solve()

    example.show_board()
