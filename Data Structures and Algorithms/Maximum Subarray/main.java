public class Main {  // Note: Renamed class to 'Main' to follow Java naming conventions.
    public static void main(String[] args) {
        // Input array containing both positive and negative numbers.
        int[] array = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };

        // Approach 1: Using explicit if-statements for comparisons.
        
        // Get the length of the array.
        int n = array.length;
        
        // Initialize variables to store the maximum subarray sum and the current subarray sum.
        int maximum_sum = 0;
        int current_sum = 0;
    
        // Iterate over the array using indices.
        for (int i = 0; i < n; i++) {
            // Add the current element to the current sum.
            current_sum += array[i];
            
            // If the current sum is greater than the maximum sum, update the maximum sum.
            if (current_sum > maximum_sum) {
                maximum_sum = current_sum;
            }

            // If the current sum becomes negative, reset it to 0.
            if (current_sum < 0) {
                current_sum = 0;
            }
        }

        // Display the result from Approach 1.
        System.out.println(maximum_sum);

        // Approach 2: Using Java's Math.max() for cleaner comparisons.

        // Note: You missed declaring 'maxSum' and 'currentSum' for this approach. 
        // We'll include them here for completeness.
        int maxSum = 0;
        int currentSum = 0;

        // Use enhanced for-loop to iterate over each element in the array.
        for (int num : array) {
            // Add the current element to the current sum.
            currentSum += num;

            // Update maxSum to be the maximum of maxSum and currentSum.
            maxSum = Math.max(maxSum, currentSum);

            // Reset currentSum to zero if it becomes negative.
            currentSum = Math.max(currentSum, 0);
        }

        // Display the result from Approach 2.
        System.out.println(maxSum);
    }
}
