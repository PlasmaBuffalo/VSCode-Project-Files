package StreetsTime.src;
import java.util.Scanner;

public class Streets {
    public static void main(String[] args) throws Exception {
        System.out.println("Enter a length of time in HH:MM:SS format to convert to number of streets 1:12 runs");

        // Get the time from the user
        Scanner scanner = new Scanner(System.in);
        String time = scanner.nextLine();

        //close the scanner for fun and profit
        scanner.close();

        //if time is exactly equal to 00:01:13, then it is not a valid time and should be rejected
        if (time.equals("00:01:13")) {
            System.out.println("I've never seen a 1:13 and I never ####ing will");
            return;
        }

        // Split the time into hours, minutes, and seconds
        String[] timeParts = time.split(":");
        int hours = Integer.parseInt(timeParts[0]);
        int minutes = Integer.parseInt(timeParts[1]);
        int seconds = Integer.parseInt(timeParts[2]);

        // Convert the time to seconds

        // 1 hour = 3600 seconds
        // 1 minute = 60 seconds
        // 1 second = 1 second

        int totalSeconds = (hours * 3600) + (minutes * 60) + seconds;

        // Convert the time to streets, or units of 72 seconds since 00:01:12 = 1 street

        // 1 street = 72 seconds

        int totalStreets = totalSeconds / 72;

        // Print the result

        System.out.println("The time " + time + " is equal to " + totalStreets + " runs of streets: 1:12");
    }
}
