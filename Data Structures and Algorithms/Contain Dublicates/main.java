import java.util.HashSet;
import java.util.Set;

public class Main{
    public static void main(String[] args){
        int[] myArray = {1, 2, 3};
        Set<String> mySet = new HashSet<>();
        boolean dublicates = false;

        for (int num : myArray){
            if (mySet.contains(num)){
                dublicates = !dublicates;
            }
            else{
                mySet.add(num)
            }
        }
    }
}