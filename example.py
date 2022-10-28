'''
Date: 2022-10-26 15:13:54
LastEditors: yuhhong
LastEditTime: 2022-10-28 14:31:47
'''
from sudoku import Sudoku

if __name__ == "__main__":
    example = Sudoku(path='./master_001.txt')

    example.show_board()

    example.solve()

    example.show_board()
