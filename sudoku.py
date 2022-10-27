'''
Date: 2022-10-26 15:09:29
LastEditors: yuhhong
LastEditTime: 2022-10-26 23:36:52
'''
import sys
sys.setrecursionlimit(5000)

class Sudoku: 

    def __init__(self, path=None):
        self.board = []
        self.blank_idx = []
        self.sq_len = 9
        self.sub_sq_len = 3
        
        if path: # read the board from a file
            print('Init the Sudoku board from the file: {}'.format(path))
            with open(path, 'r') as f:
                data = f.readlines()
            for row in data:
                self.board += row.split()
            
            for i, item in enumerate(self.board):
                if item == '-':
                    self.blank_idx.append(i)

        else: # generate a new board
            print('Init the Sudoku board by generating')
            raise Exception('Not implement yet!')

        if len(self.board) == 0: # make sure the board is not empty
            raise ValueError('Empty board!')
        
        self.potential_values = self._init_potential_values(self.board)
        self.track_indexes = {k:-1 for k in self.blank_idx}
        # print(self.potential_values, self.track_indexes)

    # -------------------------------------
    # External functions
    # -------------------------------------

    def show_board(self):
        list_board = []
        for item in self.board:
            list_board.append(str(item))
        print('>>>')
        for i in range(self.sq_len):
            print('|{}|'.format(','.join(list_board[int(i*self.sq_len): int((i+1)*self.sq_len)])))
        # print('blank indexes: {}'.format(self.blank_idx))

    def solve(self):
        print('Solving the Sudoku...')
        self.board = self._fill_board(self.board, 0)
        print('Done!')

    # -------------------------------------
    # Internal functions
    # -------------------------------------
    
    def _init_potential_values(self, board):
        values = {}
        for i in self.blank_idx:
            values[i] = set([*range(1, self.sq_len+1)])

        # look in row
        for i in range(self.sq_len):
            item_list = [int(board[int(i*self.sq_len+j)]) for j in range(self.sq_len) if board[int(i*self.sq_len+j)] != '-']
            item_set = set(item_list)
            # remove exsist values in potential values
            for k, v in values.items():
                if k in [int(i*self.sq_len+j) for j in range(self.sq_len)]:
                    values[k] = v - item_set

        # look in column
        for i in range(self.sq_len):
            item_list = [int(board[int(j*self.sq_len+i)]) for j in range(self.sq_len) if board[int(j*self.sq_len+i)] != '-']
            item_set = set(item_list)
            # remove exsist values in potential values
            for k, v in values.items():
                if k in [int(j*self.sq_len+i) for j in range(self.sq_len)]:
                    values[k] = v - item_set

        # look in square
        for i in range(self.sq_len):
            item_list = []
            idx_list = []
            for j in range(self.sub_sq_len): 
                start_idx = (i // self.sub_sq_len) * self.sq_len * self.sub_sq_len + (i % self.sub_sq_len) * self.sub_sq_len + j * self.sq_len
                sub_item_list = board[start_idx: start_idx+self.sub_sq_len]
                idx_list.append([*range(start_idx,start_idx+self.sub_sq_len)])
                for item in sub_item_list:
                    if item != '-':
                        item_list.append(int(item))

            item_set = set(item_list)
            # remove exsist values in potential values
            for k, v in values.items():
                if k in idx_list:
                    values[k] = v - item_set
        
        for k, v in values.items(): 
            values[k] = list(v)
        return values

    def _fill_board(self, board, i): 
        if i == len(self.blank_idx): # complete!
            return board
        pos = self.blank_idx[i]

        # print(pos, board[pos], self.track_indexes[pos], self.potential_values[pos])
        if board[pos] == '-':
            self.track_indexes[pos] = 0
            board[pos] = self.potential_values[pos][self.track_indexes[pos]]
        elif self.track_indexes[pos] < len(self.potential_values[pos]) - 1: 
            self.track_indexes[pos] += 1
            board[pos] = self.potential_values[pos][self.track_indexes[pos]]
        else: 
            self.track_indexes[pos] = -1
            board[pos] = '-'
            return self._fill_board(board, i-1)

        # check validation
        val = self._check_board(board)
        if val:
            return self._fill_board(board, i+1)
        else:
            return self._fill_board(board, i)

    def _check_board(self, board):
        # check row
        for i in range(self.sq_len):
            item_list = [int(board[int(i*self.sq_len+j)]) for j in range(self.sq_len) if board[int(i*self.sq_len+j)] != '-']
            item_set = set(item_list)
            if len(item_set) != len(item_list):
                # print('ROW({}): {}, {}'.format(i, item_list, item_set))
                return False

        # check column
        for i in range(self.sq_len):
            item_list = [int(board[int(j*self.sq_len+i)]) for j in range(self.sq_len) if board[int(j*self.sq_len+i)] != '-']
            item_set = set(item_list)
            if len(item_set) != len(item_list):
                # print('COLUMN({}): {}, {}'.format(i, item_list, item_set))
                return False
                
        # check square
        for i in range(self.sq_len):
            item_list = []
            for j in range(self.sub_sq_len):
                start_idx = (i // self.sub_sq_len) * self.sq_len * self.sub_sq_len + (i % self.sub_sq_len) * self.sub_sq_len + j * self.sq_len
                sub_item_list = board[start_idx: start_idx+self.sub_sq_len]
                for item in sub_item_list:
                    if item != '-':
                        item_list.append(int(item))

            item_set = set(item_list)
            if len(item_set) != len(item_list):
                # print('SQUARE({}): {}, {}'.format(i, item_list, item_set))
                return False
        return True