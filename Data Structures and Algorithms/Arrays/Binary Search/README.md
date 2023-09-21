# Binary Search Implementation

This repository contains a simple implementation of the binary search algorithm in Python.

## Description

The function `binary_search` takes in a sorted list and a key. It returns the index of the key in the list if it exists, otherwise it returns `-1`.

## How it Works

1. Start by setting two pointers at the start and end of the list.
2. Calculate the midpoint of the list.
3. Check if the element at the midpoint is the key.
    - If it is, return the midpoint.
    - If the key is smaller than the midpoint, adjust the end pointer to be one less than the midpoint.
    - If the key is larger than the midpoint, adjust the start pointer to be one more than the midpoint.
4. Continue this process until the key is found or the start pointer exceeds the end pointer.

## Example

Given the list `[0, 1, 2, 4, 5, 6, 7]` and the key `1`, the function returns `1` which is the index of the key in the list.

```python
my_list = [0, 1, 2, 4, 5, 6, 7]
key = 1
result = binary_search(my_list, key)
print(result)  # Outputs: 1
```

## Usage

To use the function:

```python
from binary_search_module import binary_search

my_list = [0, 1, 2, 4, 5, 6, 7]
key = 5
result = binary_search(my_list, key)
print(result)  # Outputs: 4
```

Replace `binary_search_module` with the actual module name if saved in a different filename.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.