public class Main {
    public static void main(String[] args) {
        int[] myArray = {1, 2, 3};

        System.out.println("Original Array:");
        for (int i : myArray) {
            System.out.print(i + " ");
        }
        System.out.println();

        int n = myArray.length;
        for (int i = 0; i < n / 2; i++) {
            int j = n - 1 - i;

            int temp = myArray[i];
            myArray[i] = myArray[j];
            myArray[j] = temp;
        }

        System.out.println("Reversed Array:");
        for (int i : myArray) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
