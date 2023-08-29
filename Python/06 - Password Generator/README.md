# Password Generator in Python

## Overview

This is a simple Python script to generate a random password. The password includes a mix of uppercase and lowercase alphabets, numbers, and special characters. The script provides an interactive command-line interface to specify the number of each type of character.

## Prerequisites

- Python 3.x

## How to Use

1. Clone this repository or download the Python script.
2. Open a terminal and navigate to the folder containing the Python script.
3. Run the Python script using the command `python main.py`.
4. Follow the on-screen instructions to generate your password.

## Code Structure

- The code uses Python's built-in `random` library for generating random characters.
- The character sets for uppercase and lowercase alphabets, numbers, and symbols are predefined.
- The user is prompted to input the number of each type of character they want in their password.
- The password is then generated and displayed.

## Features

- Generates a strong password including uppercase and lowercase alphabets, numbers, and symbols.
- Allows the user to specify the number of each type of character in the password.
- The generated password is shuffled to ensure a random distribution of characters.

## Sample Usage

After running the script, you will be prompted to enter the number of letters, symbols, and numbers you want in your password.

```bash
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
2
How many numbers would you like?
2
```

The script will then generate a password based on your input and display it.

```bash
Your password: g^2jk8&P
```