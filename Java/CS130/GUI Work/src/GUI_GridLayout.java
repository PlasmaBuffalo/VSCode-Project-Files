//create a sample of a grid layout
import java.awt.*;
import javax.swing.*;

//open class, extends JFrame
public class GUI_GridLayout extends JFrame
{
    //declare variables
    private JButton button1, button2, button3, button4, button5, button6;
    private JPanel panel1, panel2;

    //constructor
    public GUI_GridLayout()
    {
        //set title
        setTitle("Grid Layout");

        //set layout
        setLayout(new BorderLayout());

        //create buttons
        button1 = new JButton("Button 1");
        button2 = new JButton("Button 2");
        button3 = new JButton("Button 3");
        button4 = new JButton("Button 4");
        button5 = new JButton("Button 5");
        button6 = new JButton("Button 6");
        //make all the buttons different colors
        button1.setBackground(Color.red);
        button2.setBackground(Color.blue);
        button3.setBackground(Color.green);
        button4.setBackground(Color.yellow);
        button5.setBackground(Color.orange);
        button6.setBackground(Color.pink);

        //create panels
        panel1 = new JPanel();
        panel2 = new JPanel();

        //set layout for panel1
        panel1.setLayout(new GridLayout(2,3));

        //add buttons to panel1
        panel1.add(button1);
        panel1.add(button2);
        panel1.add(button3);
        panel1.add(button4);
        panel1.add(button5);
        panel1.add(button6);

        //add panel1 to panel2
        panel2.add(panel1);

        //add panel2 to frame
        add(panel2, BorderLayout.CENTER);
    }

    //main method
    public static void main(String[] args)
    {
        //create frame
        GUI_GridLayout frame = new GUI_GridLayout();

        //set size
        frame.setSize(400, 200);

        //set location
        frame.setLocationRelativeTo(null);

        //set close operation
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //set visible
        frame.setVisible(true);
    }
}