//in-class array practice

public class arrayPractice {
    // main class
    public static void main(String[] args) {
        // instance of main class
        arrayPractice ap = new arrayPractice();
        // call swap method with test cases for the String array and two indeces
        ap.swap(new String[] { "a", "b", "c", "d", "e" }, 0, 4);
        //test all methods listed below
        //create r/d array and save using method 2
        char[][] rdArray = ap.createRDArray();
        //print out the random array we just created
        ap.printCharArray(rdArray);
        //print outcome of countRs method using rdArray
        System.out.println("Highest Rs row: " + ap.countRs(rdArray));
        //print outcome of countDs method using rdArray
        System.out.println("Lowest Rs column: " + ap.countDs(rdArray));
        //print outcome of diagonal method using rdArray
        System.out.println("Diagonal print: " + ap.diagonal(rdArray));
        //print outcome of navigate method using rdArray, starting at 0,0
        System.out.println("Navigating: " + ap.navigate(rdArray, 0, 0));

        

    }
    //create method to print out a char array using some nice formatting
    public void printCharArray(char[][] array) {
        //for loop to go through each row
        for (int i = 0; i < array.length; i++) {
            //for loop to go through each column
            for (int j = 0; j < array[i].length; j++) {
                //print out the character at the current row and column
                System.out.print(array[i][j] + " ");
            }
            //print out a new line after each row
            System.out.println();
        }
    }

    // method 1: method that takes in an array of strings and two integer values,
    // 'first' and 'last'.
    // if first is not in range, set first to 0. if last is not in range, set last
    // to the length of the array - 1.
    // else, try to swap the values at the indices first and last and return the
    // string array.
    public String[] swap(String[] array, int first, int last) {
        if (first < 0 || first >= array.length) {
            first = 0;
        }
        if (last < 0 || last >= array.length) {
            last = array.length - 1;
        }
        String temp = array[first];
        array[first] = array[last];
        array[last] = temp;
        return array;
    }

    //method 2: method that creates a 2D array of characters and randomly assigns each place to either an 'r' or 'd'.
    //return the 2D array.
    public char[][] createRDArray() {
        char[][] array = new char[5][8];
        //for testing, print the length of array and length of array[0]
        // System.out.println(array.length);
        // System.out.println(array[0].length);
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                if (Math.random() < 0.5) {
                    array[i][j] = 'r';
                } else {
                    array[i][j] = 'd';
                }
            }
        }
        return array;
    }

    //method 3: takes in the above 2D array and returns the row with highest count of 'r's in the form of a string.
    //If a tie occurs, return the last row with the highest count.
    public String countRs(char[][] array) {
        int max = 0;
        int maxRow = 0;
        for (int i = 0; i < array.length; i++) {
            int count = 0;
            for (int j = 0; j < array[i].length; j++) {
                if (array[i][j] == 'r') {
                    count++;
                }
            }
            if (count > max) {
                max = count;
                maxRow = i;
            }
        }
        return "Row " + maxRow + " has the most Rs with " + max + " Rs.";
    }

    //method 4: takes in the above 2D array and returns the column with highest count of 'd's in the form of a string.
    //If a tie occurs, return the first column with the highest count.
    public String countDs(char[][] array) {
        int max = 0;
        int maxCol = 0;
        for (int i = 0; i < array[0].length; i++) {
            int count = 0;
            for (int j = 0; j < array.length; j++) {
                if (array[j][i] == 'd') {
                    count++;
                }
            }
            if (count > max) {
                max = count;
                maxCol = i;
            }
        }
        return "Column " + maxCol + " has the most Ds with " + max + " Ds.";
    }

    //method 5: a method that returns a string of concatenated chars from the diagonal across a char array.
    public String diagonal(char[][] array) {
        String str = "";
        for (int i = 0; i < array.length; i++) {
            str += array[i][i];
        }
        return str;
    }

    //method 6: a recursive method that navigates the char array.
    //input: the char array, the current row, and the current column.
    //start at 0,0. If current is a 'd', move down and recurse. If current is an 'r', move right and recurse.
    //if current char is neither, return "middle".
    //if current is 'd' but out of bounds, return "bottom".
    //if current is 'r' but out of bounds, return "right".
    public String navigate(char[][] array, int row, int col) {
        //print current row and column
        System.out.println("Now at row " + row + " and column " + col);
        if (row >= array.length || col >= array[0].length) {
            return "bottom";
        }
        if (row < 0 || col < 0) {
            return "top";
        }
        if (array[row][col] == 'd') {
            return navigate(array, row + 1, col);
        }
        if (array[row][col] == 'r') {
            return navigate(array, row, col + 1);
        }
        return "middle";
    }

}