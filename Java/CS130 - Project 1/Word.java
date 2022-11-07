//class to define a Word object
//create class Word with 3 fields: word string, compound index, and compound boolean
public class Word{
    //create private fields
    private String word;
    private int index;
    private boolean compound;

    // create constructor for 
    public Word(String word, int index, boolean compound) {
        this.word = word;
        this.index = index;
        this.compound = compound;
    }

    //create getters and setters
    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }

    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    public boolean isCompound() {
        return compound;
    }

    public void setCompound(boolean compound) {
        this.compound = compound;
    }

    //create toString method
    @Override
    public String toString() {
        return "Word{" +
                "word='" + word + '\'' +
                ", index=" + index +
                ", compound=" + compound +
                '}';
    }

}