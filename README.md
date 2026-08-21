# logic-box
# Pattern Generator and Number Analyzer

## Description

The **Pattern Generator and Number Analyzer** is a simple Python console application that provides users with three options:

1. Generate a star pattern.
2. Analyze a range of numbers to determine whether each number is even or odd and calculate their sum.
3. Exit the program.

## Features

### 1. Generate a Pattern

The program asks the user to enter the number of rows and then generates a right-angled star pattern.

**Example:**

```text
Enter the number of rows for the pattern: 5

Pattern:
*
**
***
****
*****
```

### 2. Analyze a Range of Numbers

The program asks for a starting and ending number. It then:

* Checks whether each number is **Even** or **Odd**.
* Displays the result for every number.
* Calculates the sum of all numbers in the given range.

**Example:**

```text
Enter the start of the range: 1
Enter the end of the range: 5

Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd

Sum of all numbers from 1 to 5 is: 15
```

### 3. Exit

Selecting option `3` exits the program.

```text
Exiting the program. Goodbye!
```

## Requirements

* Python 3.x

No external libraries are required.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Save the program as:

```text
pattern_generator.py
```

3. Open a terminal in the folder containing the file.
4. Run:

```bash
python pattern_generator.py
```

## Program Flow

```text
Start
  |
  v
Display Menu
  |
  +---- 1 ----> Generate Star Pattern
  |
  +---- 2 ----> Analyze Number Range
  |
  +---- 3 ----> Exit
  |
  +---- Other -> Invalid Choice
  |
  v
Display Menu Again
```

## Concepts Used

This project demonstrates several basic Python programming concepts:

* `while` loops
* `for` loops
* `if`, `elif`, and `else` statements
* `range()`
* User input with `input()`
* Type conversion with `int()`
* Modulus operator `%`
* f-strings
* `break`
* String multiplication

## Author

Created as a beginner-friendly Python programming project.
