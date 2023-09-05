#include <iostream>

int main()
{
    // Initialize an array with both positive and negative integers
    int array[9] = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };

    // Calculate the length of the array
    int n = sizeof(array) / sizeof(int);

    // Initialize variables to keep track of the maximum subarray sum and the current subarray sum
    int maximum_sum = 0;
    int current_sum = 0;

    // Iterate through each element in the array
    for (int i = 0; i < n; ++i) {
        // Add the current element to the current subarray sum
        current_sum += array[i];

        // Update the maximum subarray sum if the current sum is greater
        if (current_sum > maximum_sum) {
            maximum_sum = current_sum;
        }

        // Reset the current sum if it becomes negative
        if (current_sum < 0) {
            current_sum = 0;
        }
    }

    // Output the maximum subarray sum
    std::cout << maximum_sum << std::endl;

    return 0;
}
