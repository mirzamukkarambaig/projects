# Roman to Integer Converter

## Overview

This Python script contains a class `Solution` with a method `romanToInt` that converts a Roman numeral string to its integer value.

## Requirements

- Python 3.x

## Usage

First, import the `Solution` class from the script.

```python
from your_script import Solution
```

Create an instance of the `Solution` class.

```python
converter = Solution()
```

Call the `romanToInt` method with a Roman numeral string as an argument.

```python
result = converter.romanToInt("III")
print(result)  # Output will be 3
```

## Method Details

### `romanToInt(self, s: str) -> int`

This method takes a Roman numeral string `s` and returns its integer representation.

#### Parameters

- `s (str)`: The Roman numeral string to be converted.

#### Returns

- `int`: The integer representation of the given Roman numeral.

## Algorithm

1. The method uses a dictionary `decoder` to map each Roman numeral to its integer value.
2. It initializes `sum` to 0 and `prev_value` to 0 for keeping track of the sum and the previous numeral value respectively.
3. A for loop iterates through the string `s` in reverse.
    - For each Roman numeral, it retrieves its integer value from `decoder`.
    - If the current numeral's value is smaller than the previous numeral's value (`prev_value`), it subtracts the current value from `sum`.
    - Otherwise, it adds the current value to `sum`.
    - Updates `prev_value` with the current value for the next iteration.

