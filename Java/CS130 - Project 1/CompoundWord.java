
/*For your first project you will be creating a tool to help kids learn about compound words (ex. starfish and toothbrush) while practicing String Methods and other Java programming essentials like methods, if statements, and loops.
 * Liam Zalubas
 */

//import statements
import java.util.Scanner;

public class CompoundWord {
    public static void main(String[] args) {
        // create one compound word and one simple word
        Word word1 = new Word("compound", 1, true);
        Word word2 = new Word("simple", 2, false);
        // call whetherCompound method
        // call whereCompound method
    }

    // method interacting with the user asking if a word is compound or not
    public void whetherCompound(Word w) {
        // ask the user if the word passed in is compound using a scanner
        System.out.println("Is the word " + w.getWord() + " a compound word? (y/n)");
        Scanner input = new Scanner(System.in);
        String answer = input.nextLine();
        // if the word was compound, congratulate the user on their correct answer
        if (answer.equals("y")) {
            System.out.println("Congratulations! You are correct!");
            //call the whereCompound method with the current Word object
            whereCompound(w);
        }
        // if the word was not compound, tell the user they are incorrect
        else if (answer.equals("n")) {
            System.out.println("Sorry, you are incorrect.  The word " + w.getWord() + " is a compound word.");
        }

    }

    public void whereCompound(Word w) {

    }
}
