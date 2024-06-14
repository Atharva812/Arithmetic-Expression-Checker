# Arithmetic Expression Checker

This project is a simple GUI-based arithmetic expression checker written in Python using the `tkinter` library. It tokenizes, parses, and evaluates arithmetic expressions and displays the result along with a message indicating whether the syntax is valid. Additionally, it shows the number of tokens generated during the lexing process.

## Features

- Tokenizes arithmetic expressions
- Parses and evaluates arithmetic expressions
- Displays the result of the expression
- Checks and indicates if the syntax is valid
- Displays the number of tokens generated

## Requirements

- Python 3.x
- `tkinter` library (usually included with standard Python installations)

## How to Run

1. **Clone the repository or download the script:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Run the script:**

    ```bash
    python arithmetic_checker.py
    ```

## Usage

1. Enter an arithmetic expression in the provided input field.
2. Click the "Check Syntax" button.
3. The result of the expression, the syntax validation message, and the token count will be displayed.

## Examples

- Input: `2 + 3`
  - Output: 
    - Result: `5`
    - Syntax is valid.
    - Token count: 3

- Input: `5 * (2 - 3)`
  - Output:
    - Result: `-5`
    - Syntax is valid.
    - Token count: 7

- Input: `4 / 2 + 6`
  - Output:
    - Result: `8.0`
    - Syntax is valid.
    - Token count: 5

- Input: `2 +`
  - Output:
    - Syntax Error: Invalid syntax
    - Token count: 2

## Code Overview

### Lexer

The `Lexer` class is responsible for converting the input string into a sequence of tokens. It supports integer numbers and the operators `+`, `-`, `*`, `/`, as well as parentheses `(` and `)`.

### Parser

The `Parser` class takes the sequence of tokens produced by the `Lexer` and generates an abstract syntax tree (AST) based on the grammar rules of arithmetic expressions.

### Code Generator

The `CodeGenerator` class takes the AST produced by the `Parser` and evaluates it to produce the final result.

### GUI Application

The `ArithmeticInterpreterApp` class creates a simple GUI using `tkinter`. It includes:
- An entry widget for inputting arithmetic expressions.
- A button to check the syntax and evaluate the expression.
- Labels to display the result, syntax validation message, and token count.

### Main

The `main` function initializes and runs the `tkinter` application.


## Acknowledgements

This project was created using the `tkinter` library for the GUI and basic principles of compiler construction for lexing, parsing, and code generation.

