# Matrix Calculator

This Matrix Calculator is a Python program developed using 2D lists. It allows you to perform basic matrix operations such as addition, subtraction, and multiplication. The program provides a user-friendly interface and includes features to improve the user experience, such as input validation and clear error messages.

## Features

1. **Matrix Addition**: Adds two matrices of the same dimensions.
2. **Matrix Subtraction**: Subtracts one matrix from another. It allows the user to choose between `A-B` and `B-A`.
3. **Matrix Multiplication**: Multiplies two matrices if the number of columns in the first matrix matches the number of rows in the second matrix.
4. **User-Friendly Interface**: Provides current time-based greetings and clear prompts for user inputs.
5. **Input Validation**: Checks for valid matrix dimensions and elements.
6. **Persistent Storage**: Optionally saves and retrieves matrices from a previous session.
7. **Clear and Styled Output**: Presents matrices and results in a formatted manner for better readability.
8. **Exit Option**: Allows the user to exit the program gracefully.

## Functions

### `wishMe()`
Wishes the user according to the current time and welcomes them to the Matrix Calculator.

### `changeToInt(matrixx)`
Converts all elements of the given matrix to integers.

### `changeToStr(matrixx)`
Converts all elements of the given matrix to strings and formats them for better display.

### `takeMatrix(_)`
Prompts the user to input a matrix, ensuring the input is valid.

### `mat_3(a, operator, b, r)`
Displays the matrices and the result of the operation in a formatted manner.

### `matAdd(a, b)`
Adds two matrices and returns the result.

### `matSub(a, b)`
Subtracts one matrix from another based on user choice and returns the result.

### `matMul(a, b)`
Multiplies two matrices and returns the result.

### `bye()`
Asks the user if they want to exit and handles the exit process.

### `start()`
Main function to start the program. Handles matrix input, operation selection, and calling the appropriate functions based on user input.

## How to Use

1. **Start the Program**: Run the Python script. The program will greet you based on the current time.
2. **Input Matrices**: You will be prompted to input the dimensions and elements of two matrices.
3. **Choose Operation**: Select the operation you want to perform (`+`, `-`, `*`, or `Q` to quit).
4. **View Result**: The program will display the matrices and the result of the operation.
5. **Exit or Continue**: You can choose to exit the program or continue performing more operations.

## Example

Here's a step-by-step example of using the Matrix Calculator:

1. Run the script.
2. Input the dimensions and elements of Matrix A.
3. Input the dimensions and elements of Matrix B.
4. Select the operation (e.g., `+` for addition).
5. View the result displayed in a formatted manner.
6. Choose to exit or perform another operation.

## Dependencies

- Python standard libraries: `time`, `os`

## Notes

- Ensure that the matrices are compatible for the chosen operations.
- The program does not support matrix division.
- The program saves matrices to `storeValues.txt` for potential reuse in the next session.

## Author

- Developed by: 22233-CS-004

Enjoy using the Matrix Calculator! If you have any questions or feedback, feel free to reach out.
