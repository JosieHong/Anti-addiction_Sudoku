<!--
 * @Date: 2022-10-26 15:11:27
 * @LastEditors: yuhhong
 * @LastEditTime: 2022-10-28 13:53:19
-->
# Solve All the Sudoku, Leave No Joy for Solving by Yourself

This is a Python implementation of a Sudoku solver and generator. 

So far the "hard" and "master" leveled puzzles can be solved. Hopefully, these codes will also solve my addiction to Sudoku. 

If you have a friend addicted to Sudoku, please share these codes to them. :)

## Running Example

```python
>>> from sudoku_super import Sudoku
>>> example = Sudoku(path='./hard_001.txt')
Init the Sudoku board from the file: ./puzzle010.txt
>>> example.show_board()
>>>
|-,3,-,8,7,-,-,-,-|
|8,-,-,-,-,4,-,9,-|
|-,-,4,-,6,-,-,1,-|
|-,-,-,4,5,-,-,2,7|
|-,1,-,7,-,-,-,4,6|
|-,-,3,6,-,-,-,-,-|
|9,-,-,-,-,-,-,-,2|
|-,4,-,-,1,-,-,-,-|
|-,-,1,-,-,5,-,-,-|
>>> example.solve()
Solving the Sudoku...
Done!
>>> example.show_board()
>>>
|1,3,2,8,7,9,4,6,5|
|8,5,6,1,2,4,7,9,3|
|7,9,4,5,6,3,2,1,8|
|6,8,9,4,5,1,3,2,7|
|2,1,5,7,3,8,9,4,6|
|4,7,3,6,9,2,5,8,1|
|9,6,8,3,4,7,1,5,2|
|5,4,7,2,1,6,8,3,9|
|3,2,1,9,8,5,6,7,4|
```

TODO: 

- [x] Solving the Soduku from a file using backtracking algorithm; 
- [x] Solving the Soduku from a file using constraint propagation (as Constraint Satisfaction Problem); 
- [ ] Modify the algorithm to solve "grandmaster" leveled puzzles; 
- [ ] Generating the Sudoku;
- [ ] Implement basic techniques (simulate human actions);

## Reference

```
@inproceedings{simonis2005sudoku,
  title={Sudoku as a constraint problem},
  author={Simonis, Helmut},
  booktitle={CP Workshop on modeling and reformulating Constraint Satisfaction Problems},
  volume={12},
  pages={13--27},
  year={2005},
  organization={Citeseer}
}
```