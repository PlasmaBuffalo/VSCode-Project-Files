
public class Substrings {
    public static void main(String[] args) {
        //create instance of main class
        Substrings ss = new Substrings();
        //test the parenBit method
        System.out.println(ss.parenBit("xyz(abc)123"));
        System.out.println(ss.parenBit("x(hello)"));
        System.out.println(ss.parenBit("(xy)1"));
    }

    // given a string with a single pair of parentheses, compute recursively a new
    // string made of only of the parenthesis and their contents, so "xyz(abc)123"
    // yields "(abc)".
    public String parenBit(String str) {
        // base case: empty string ends recursion
        if (str.length() == 0) {
            return "";
        }
        // recursive case
        else {
            // if the first char is a parenthesis, add it to the string and call the method
            // again
            if (str.charAt(0) == '(') {
                return str.charAt(0) + parenBit(str.substring(1));
            }
            // if the first char is not a parenthesis, call the method again
            else {
                return parenBit(str.substring(1));
            }
        }
    }
}
