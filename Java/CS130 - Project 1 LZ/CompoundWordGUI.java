//import awt and swing
import java.awt.*;
import javax.swing.*;

public class CompoundWordGUI {
    //create a window to take difficulty from radio buttons and topics from checkboxes
    public static void main(String[] args){
        //create a window
        JFrame window = new JFrame("Compound Word Game");
        window.setSize(1000, 1000);
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setLayout(new FlowLayout());
        //size the window according to the components
        

        //create a panel
        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());
        //create radio buttons
        JRadioButton easy = new JRadioButton("Easy");
        JRadioButton medium = new JRadioButton("Medium");
        JRadioButton hard = new JRadioButton("Hard");
        //create a button group
        ButtonGroup difficulty = new ButtonGroup();
        difficulty.add(easy);
        difficulty.add(medium);
        difficulty.add(hard);
        //create checkboxes
        JCheckBox animal = new JCheckBox("Animal");
        JCheckBox food = new JCheckBox("Food");
        JCheckBox thing = new JCheckBox("Thing");
        JCheckBox people = new JCheckBox("People");
        //create a button
        JButton letsGo = new JButton("Let's Go!");
        //add radio buttons to panel
        panel.add(easy);
        panel.add(medium);
        panel.add(hard);
        //add checkboxes to panel
        panel.add(animal);
        panel.add(food);
        panel.add(thing);
        panel.add(people);
        //add button to panel
        panel.add(letsGo);
        //add panel to window
        window.add(panel);
        //make window visible
        window.pack();
        window.setVisible(true);

        //create an action listener for the button to start the game when clicked and get the difficulty and topics selected
        letsGo.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                //get the difficulty selected
                String difficulty = "";
                if(easy.isSelected()){
                    difficulty = "easy";
                }
                else if(medium.isSelected()){
                    difficulty = "medium";
                }
                else if(hard.isSelected()){
                    difficulty = "hard";
                }
                //get the topics selected
                String topics = "";
                if(animal.isSelected()){
                    topics += "animal ";
                }
                if(food.isSelected()){
                    topics += "food ";
                }
                if(thing.isSelected()){
                    topics += "thing ";
                }
                if(people.isSelected()){
                    topics += "people ";
                }
                
                //print out the difficulty and topics selected
                System.out.println(difficulty);
                System.out.println(topics);
            }
        });
    }
}