import java.util.HashSet;
import java.util.Set;

public class main {
    public static void main(String[] args) {
        int[] myArray = {1, 2, 3};
        Set<Integer> mySet = new HashSet<>();  // Changed type to Integer
        boolean duplicates = false;  // Corrected the spelling

        for (int num : myArray) {
            if (mySet.contains(num)) {
                duplicates = true;  // Set to true directly
                break;  // Exit the loop as we've found a duplicate
            } else {
                mySet.add(num);
            }
        }

        System.out.println("Duplicates found: " + duplicates);
    }
}
