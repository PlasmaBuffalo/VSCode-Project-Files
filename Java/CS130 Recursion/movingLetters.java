public class movingLetters {

    //recursive method to move all lowercase x chars to the end of a given string
    public String endX(String input){
        //base case
        if(input.length() == 0){
            return "";
        }
        //recursive case
        else{
            //if the first char is an x, move it to the end of the string
            if(input.charAt(0) == 'x'){
                return endX(input.substring(1)) + "x";
            }
            //if the first char is not an x, move it to the front of the string
            else{
                return input.charAt(0) + endX(input.substring(1));
            }
        }
    }
}
