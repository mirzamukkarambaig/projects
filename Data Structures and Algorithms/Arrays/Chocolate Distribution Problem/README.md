# Chocolate Distribution Problem

Given that an `array of intergers` of `n` elements. Each element represent the `number of choclates` in a packet. The problem is to distribute the packets in `m` students such that:
    - Every students gets atleast `one` choclate
    - The difference between the `maximum chocolate packet` and `minimum chocolate packet` is minimum.

## Variables

- `n` : Number of elements in the array
- `m` : Number of students
- `my_list` : Array of integers
- `min_diff` : Minimum difference between the maximum and minimum chocolate packet

## Solution

The solution is to sort the array and then find the minimum difference between the `m` consecutive elements in the array.
