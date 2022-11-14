
public class arrayPractice {
    // main class
    public static void main(String[] args) {
        // instance of main class
        arrayPractice ap = new arrayPractice();
        // call swap method with test cases for the String array and two indeces
        ap.swap(new String[] { "a", "b", "c", "d", "e" }, 0, 4);
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
