#include <iostream>
#include <algorithm>
#include <climits>
#include <vector>

using namespace std;

int main() {
    // Approach 1: Manual Iteration

    // Initialize the list of numbers
    vector<int> myVector = {5, 15, 50, 3, 67, 100};

    // Initialize variables to hold the minimum and maximum values
    int minimum = INT_MAX;
    int maximum = INT_MIN;

    // Loop through each element in the vector to find the minimum and maximum
    for (const auto& i : myVector) {
        if (minimum > i) {
            minimum = i;
        }
        if (maximum < i) {
            maximum = i;
        }
    }

    // Display the calculated maximum and minimum values
    cout << "Maximum: " << maximum << ", Minimum: " << minimum << endl;

    // Approach 2: Using Sorting

    // Sort the vector in ascending order
    sort(myVector.begin(), myVector.end());

    // The last element is the maximum and the first element is the minimum
    maximum = myVector.back();
    minimum = myVector.front();

    // Display the calculated maximum and minimum values
    cout << "Maximum: " << maximum << ", Minimum: " << minimum << endl;

    // Approach 3: Using Built-in Functions

    // Use C++'s built-in min_element() and max_element() functions to find the minimum and maximum
    minimum = *min_element(myVector.begin(), myVector.end());
    maximum = *max_element(myVector.begin(), myVector.end());

    // Display the calculated maximum and minimum values
    cout << "Maximum: " << maximum << ", Minimum: " << minimum << endl;

    return 0;
}
