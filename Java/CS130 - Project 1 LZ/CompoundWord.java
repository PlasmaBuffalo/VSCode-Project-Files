
/*For your first project you will be creating a tool to help kids learn about compound words (ex. starfish and toothbrush) while practicing String Methods and other Java programming essentials like methods, if statements, and loops.
 * Liam Zalubas
 */

//import statements
import java.util.Scanner;


//import arraylist
import java.util.ArrayList;

public class CompoundWord {
    public static void main(String[] args) {
        // create instance of main class
        CompoundWord cw = new CompoundWord();
        // create some compound words and some simple words
        Word word1 = new Word("starfish", 4, true, 1, new String[] {"animals", "ocean"});
        Word word2 = new Word("toothbrush", 5, true, 1, new String[] {"hygiene", "tooth"});
        Word word3 = new Word("cat", -1, false, 1, new String[] {"animals", "pets"});
        Word word4 = new Word("dog", -1, false, 1, new String[] {"animals", "pets"});

        // print an explanation of what a compound word is
        System.out.println(
                "A compound word is a word that is made up of two or more words. For example, the word 'starfish' is a compound word because it is made up of the words 'star' and 'fish'.");

        // Call the whetherCompound method with one of your instances of the word method
        // as the parameter
        cw.whetherCompound(word1);

        // encourage the user to try again with a second word

        // call the whetherCompound method with a different instance of the word method
        // as the parameter
        cw.whetherCompound(word2);
    }

    // method interacting with the user asking if a word is compound or not
    public void whetherCompound(Word w) {
        // ask the user if the word passed in as a parameter is a compound word and read
        // in the user's answer
        System.out.println("Is the word " + w.getWord() + " a compound word? (y/n)");
        Scanner input = new Scanner(System.in);
        String answer = input.nextLine();

        //switch for each case if the word was compound or not and if the user said it was or not
        switch (answer) {
            case "y":
                if (w.isCompound()) {
                    //if word is compound and user said it was, print a message saying they were correct
                    System.out.println("Correct!");
                } else {
                    //correct the user
                    System.out.println("Incorrect. The word " + w.getWord() + " is not a compound word.");
                }
                //call whereCompound method with the word as a parameter
                whereCompound(w);
                break;
            case "n":
                if (w.isCompound()) {
                    //correct the user if they said the word was not compound when it is
                    System.out.println("Incorrect! The word " + w.getWord() + " is a compound word!");
                } else {
                    //if word was not compound and user said it was not, print a message saying they were correct
                    System.out.println("Correct!");
                }
                break;
            //in case the user does something stupid
            default:
                System.out.println("Invalid input!");
                break;
        }
    }

    public void whereCompound(Word w) {
        //print out the w.getWord() print a number under each letter of w.getWord()
        System.out.println(w.getWord());
        for (int i = 0; i < w.getWord().length(); i++) {
            System.out.print(i);
        }
        //ask the user which number the second word starts with
        System.out.println("Which number does the second word start with in this compound word?");
        //use a scanner to take user input for an int
        Scanner input = new Scanner(System.in);
        int answer = input.nextInt();
        //if the answer is correct, print a message saying they were correct
        if (answer == w.getIndex()) {
            System.out.println("Correct!");
            //*END CASE
        } else {
            //if the answer is incorrect, print a message saying they were incorrect and what the correct answer was
            System.out.println("Incorrect! The correct answer was " + w.getIndex() + ".");
        }
    }
}