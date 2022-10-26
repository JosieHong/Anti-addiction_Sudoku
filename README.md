<!--
 * @Date: 2022-10-26 15:11:27
 * @LastEditors: yuhhong
 * @LastEditTime: 2022-10-26 17:52:31
-->
# Sudoku Solvers and Generator

This is a Python implement of a Sudoku solver and generator. Hopefully, these codes will also solve my addiction to Sudoku. 

## Running Example

```python
>>> from sudoku import Sudoku
>>> example = Sudoku(path='./puzzle010.txt')
Init the Sudoku board from the file: ./puzzle010.txt
>>> example.show_board()
>>>
|4,-,-,8,9,3,2,-,-|
|-,2,-,1,-,4,-,3,-|
|-,9,-,-,2,6,4,-,5|
|-,-,8,-,-,9,-,5,4|
|-,-,-,3,-,1,7,2,8|
|3,7,-,-,-,5,1,-,-|
|-,3,9,-,-,-,-,1,7|
|-,8,6,-,-,-,-,-,-|
|-,-,1,-,-,-,9,-,2|
>>> example.solve()
Solving the Sudoku...
Done!
>>> example.show_board()
>>>
|4,6,5,8,9,3,2,7,1|
|8,2,7,1,5,4,6,3,9|
|1,9,3,7,2,6,4,8,5|
|6,1,8,2,7,9,3,5,4|
|9,5,4,3,6,1,7,2,8|
|3,7,2,4,8,5,1,9,6|
|5,3,9,6,4,2,8,1,7|
|2,8,6,9,1,7,5,4,3|
|7,4,1,5,3,8,9,6,2|
```

TODO: 

- [x] Solving the Soduku from a file using backtracking algorithm;
- [ ] Solving the Soduku from a file using constraint programming (as Constraint Satisfaction Problem);
- [ ] Generating the Sudoku;

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