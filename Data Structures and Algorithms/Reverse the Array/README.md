# README for Array/List Reversal Scripts

## Overview

This repository contains scripts for reversing an array or list in-place using different programming languages: Python, Java, and C++. Each script iterates over the first half of the array or list and swaps each element with its corresponding element from the end of the array or list.

## Prerequisites

- Python 3.x for the Python script
- Java Development Kit (JDK) for the Java script
- C++ compiler (e.g., g++) for the C++ script

## How to Run

### Python

1. The Python script is saved as `main.py`.
2. Run the script using the following command:

    ```bash
    python main.py
    ```

### Java

1. The Java script is saved as `Main.java`.
2. Compile the Java file:

    ```bash
    javac Main.java
    ```

3. Run the compiled Java program:

    ```bash
    java Main
    ```

### C++

1. The C++ script is saved as `main.cpp`.
2. Compile the C++ file:

    ```bash
    g++ main.cpp -o main
    ```

3. Run the compiled C++ program:

    ```bash
    ./main
    ```

## Code Explanation

### Core Logic for Reversing Array/List

The core logic for reversing the array or list is similar across all three languages and is encapsulated in a loop.

- The loop iterates through the first half of the array or list.
  - `i`: Current index in the first half of the array or list.
  - `j = n - 1 - i`: Calculates the corresponding index from the end of the array or list.
  - Swaps the elements at indices `i` and `j`.

### Output

Finally, the reversed array or list is printed to the console.

## Example

For an initial array or list of `[1, 2, 3]`, running any of these scripts will output the reversed array or list `[3, 2, 1]`.

## Complexity

- Time Complexity: O(n) 
- Space Complexity: O(1) 

## Limitations

- The array or list is hardcoded, so you'll need to modify the code to reverse a different array or list.
- The scripts work with arrays or lists that contain integers. For other data types, minor adjustments may be needed.

## License

This project is open source and available under the MIT License.