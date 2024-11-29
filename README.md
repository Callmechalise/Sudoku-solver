# Sudoku-solver-I
 
This repository contains a Python-based Sudoku solver that accepts user input for an unsolved Sudoku puzzle, validates the input, and solves the puzzle using a backtracking algorithm. The program utilizes NumPy for matrix representation and provides robust error handling to ensure valid input.

# Features:
1.User-Friendly Input: Accepts a 9x9 Sudoku grid as user input, with 0 representing blank spaces.
2.Error Handling: Includes a try-except block to handle invalid input (non-integer values).
3.Validation Function: Checks the validity of placing a number in a specific cell by ensuring:
4.The number does not already exist in the same row or column.
5.The number is not repeated in the respective 3x3 sub-grid.
6.Backtracking Algorithm: Implements a recursive approach to solve the puzzle efficiently.
7.Matrix Visualization: Displays the grid in a structured matrix format for better readability.

# Requirements:
1.Python 3.x   
2.NumPy (pip install numpy)   

# How to Use:

# Clone the repository:
bash
git clone <repository_url>

# Navigate to the project directory:
bash
cd sudoku-solver

# Run the program:
bash
python main.py

Input the Sudoku puzzle row by row as a sequence of 9 digits. Use 0 for blank spaces.

# Example Input:

Enter numbers in row 1 Without spaces and commas: 530070000  
Enter numbers in row 2 Without spaces and commas: 600195000   
Enter numbers in row 3 Without spaces and commas: 098000060
...

# Example Output:

Initial Puzzle:
[[5 3 0 0 7 0 0 0 0]
 [6 0 0 1 9 5 0 0 0]
 [0 9 8 0 0 0 0 6 0]
 ...]

Solved Puzzle:
[[5 3 4 6 7 8 9 1 2]
 [6 7 2 1 9 5 3 4 8]
 [1 9 8 3 4 2 5 6 7]
 ...]

# Additional Notes:
Ensure the input is valid (9 digits per row) for the program to function correctly.  
This implementation can be extended to include a graphical interface or more robust input handling.   
Contributions and feedback are welcome! 🚀    







