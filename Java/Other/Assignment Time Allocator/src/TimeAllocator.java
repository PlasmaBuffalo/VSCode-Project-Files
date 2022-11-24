//a program that helps with time allocation
//import scanner to read user input
import java.util.Scanner;
//import date/time to get current date/time
import java.time.LocalDateTime;

//open class
public class TimeAllocator {
    //open main method
    public static void main(String[] args) {

        //take in number of assignments from user (int)
        Scanner input = new Scanner(System.in);
        System.out.println("How many assignments do you have?");
        int numAssignments = input.nextInt();
        //close scanner
        input.close();

        //read current time from system (int)
        LocalDateTime now = LocalDateTime.now();
        //calculate number of minutes to spend on each assignment by dividing minutes left by number of assignments (int)
        int minutesLeft = 1440 - (now.getHour() * 60 + now.getMinute());

        //print out number of minutes to spend on each assignment (int)
        System.out.println("You have " + minutesLeft + " minutes left to complete " + numAssignments + " assignments.");
        System.out.println("You should spend " + minutesLeft / numAssignments + " minutes on each assignment.");
    }//close main method
}
