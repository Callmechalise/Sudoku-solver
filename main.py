import numpy as np
sudoku=[]
print('Enter numbers in ordered form.Use 0 for black space')
#Try except for error handlling
try:
    for i in range(0,9):
        row=list(input(f"Enter numbers in row {i+1} Without spaces and commas:"))
        row=[int(i)for i in row]
        sudoku.append(row)
    print(np.matrix(sudoku))
except ValueError:
    print('Oops int only')

def possible(row,column,value):#function for value checks
    global sudoku
    for i in range(0,9):
        if sudoku[row][i]==value:#Input garya value column ma vaye reutrns false
            return False
    for i in range(0,9):
        if sudoku[i][column]==value:#Input garya value row ma vaye reutrns false
            return False
    box_row=(row // 3) * 3#section divided
    box_column = (column // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[box_row+i][box_column+j]==value:
                return False
    return True


def solve():#Function for solving the puzzle
    for row in range(0,9):
        for column in range(0,9):
            if sudoku[row][column]==0:
                for value in range(1,10):#1,10 cause values in sudoku is 1-9
                    if possible(row,column, value):
                        sudoku[row][column]=value
                        solve()
                        sudoku[row][column]=0
                return
    print(np.matrix(sudoku))

if __name__=="__main__":
    solve()