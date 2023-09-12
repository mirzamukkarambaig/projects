#include <iostream>
#include <set>
using namespace std;

int main() {
    int myArray[3] = { 1, 2, 3 };
    set<int> mySet;
    bool duplicates = false;  // Added missing semicolon
    int n = sizeof(myArray) / sizeof(int);  // Added 'int' before 'n'

    for (int i = 0; i < n; i++) {
#if __cplusplus >= 202002L  // If C++20 or later
        if (mySet.contains(myArray[i])) {
#else
        if (mySet.find(myArray[i]) != mySet.end()) {
#endif
            duplicates = true;  // Set to true directly
            break;
        }
        else {
            mySet.insert(myArray[i]);  // Changed 'add' to 'insert'
        }
        }

    cout << "Duplicates found: " << duplicates << endl;  // Added missing semicolon
    return 0;
    }
