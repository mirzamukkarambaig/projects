import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // Approach 1: Manual Iteration
        int INT_MAX = Integer.MAX_VALUE;
        int INT_MIN = Integer.MIN_VALUE;

        // Initialize the list of numbers
        int[] myArray = {5, 15, 50, 3, 67, 100};

        // Initialize variables to hold the minimum and maximum values
        int minimum = INT_MAX;
        int maximum = INT_MIN;

        // Loop through each element in the array to find the minimum and maximum
        for (int i : myArray) {
            if (minimum > i) {
                minimum = i;
            }
            if (maximum < i) {
                maximum = i;
            }
        }

        // Display the calculated maximum and minimum values
        System.out.println("Maximum: " + maximum + ", Minimum: " + minimum);

        // Approach 2: Using Sorting
        Arrays.sort(myArray);
        maximum = myArray[myArray.length - 1];
        minimum = myArray[0];

        // Display the calculated maximum and minimum values
        System.out.println("Maximum: " + maximum + ", Minimum: " + minimum);

        // Approach 3: Using Java Built-in Functions
        minimum = Arrays.stream(myArray).min().getAsInt();
        maximum = Arrays.stream(myArray).max().getAsInt();

        // Display the calculated maximum and minimum values
        System.out.println("Maximum: " + maximum + ", Minimum: " + minimum);
    }
}
