//class to define a Word object
//create class Word with 3 fields: word string, compound index, and compound boolean
public class Word{
    //create private fields
    private String word;
    private int index;
    private boolean compound;
    private int difficulty;
    private String[] topics;

    //create constructor
    public Word(String word, int index, boolean compound, int difficulty, String[] topics){
        this.word = word;
        this.index = index;
        this.compound = compound;
        this.difficulty = difficulty;
        this.topics = topics;
    }

    //create getters and setters
    public String getWord(){
        return word;
    }

    public int getIndex(){
        return index;
    }

    public boolean isCompound(){
        return compound;
    }

    public int getDifficulty(){
        return difficulty;
    }

    public String[] getTopics(){
        return topics;
    }

    public void setWord(String word){
        this.word = word;
    }

    public void setIndex(int index){
        this.index = index;
    }

    public void setCompound(boolean compound){
        this.compound = compound;
    }

    public void setDifficulty(int difficulty){
        this.difficulty = difficulty;
    }

    public void setTopics(String[] topics){
        this.topics = topics;
    }

    //create toString method
    public String toString(){
        return word + " " + index + " " + compound + " " + difficulty + " " + topics;
    }

}