package Factoring.src;
import java.util.Scanner;
import java.util.ArrayList;

public class Factoring {
    public static void main(String[] args) {
        // enter a number to get its factors
        Factoring fct = new Factoring();
        Scanner kbd = new Scanner(System.in);

        System.out.println("Enter a number to get factors");
        double numInput = kbd.nextDouble();
        System.out.println(fct.getFactors(numInput));
        kbd.close();
    }

    // This method takes in a single integer number and outputs a list of its
    // factors
    public ArrayList<Integer> getFactors(double number) {
        ArrayList<Integer> factors = new ArrayList<Integer>();
        for (int i = 1; i <= number; i++) {
            if (number / i % 1 != 0) {
                //Has decimal, not a factor
            }
            else{
                factors.add(i);
            }
        }
        return factors;
    }
}
