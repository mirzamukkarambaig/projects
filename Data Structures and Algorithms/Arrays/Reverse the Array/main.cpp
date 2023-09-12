#include <iostream>
using namespace std;

int main() {
    int array[3] = {1, 2, 3};
    int n = sizeof(array) / sizeof(array[0]);

    // Print original array
    cout << "Original array: ";
    for (int i = 0; i < n; ++i) {
        cout << array[i] << " ";
    }
    cout << endl;

    // Reverse the array
    for (int i = 0; i < n / 2; ++i) {
        int j = n - 1 - i;

        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    // Print reversed array
    cout << "Reversed array: ";
    for (int i = 0; i < n; ++i) {
        cout << array[i] << " ";
    }
    cout << endl;

    return 0;
}
