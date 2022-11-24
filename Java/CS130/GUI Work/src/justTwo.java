
//using JFrames, labels, and Canvas, draw some example points on a Canvas and label them with their coordinates.
//imports
import java.awt.Canvas;
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JLabel;

//class open
public class justTwo extends Canvas{
    //main method open
    public static void main(String[] args){
        //create a new JFrame
        JFrame frame = new JFrame("justTwo");
        //create a new Canvas
        Canvas canvas = new justTwo();
        //create a new JLabel
        JLabel label = new JLabel("justTwo");
        //set the size of the canvas
        canvas.setSize(400, 400);
        //add the canvas to the frame
        frame.add(canvas);
        //add the label to the frame
        frame.add(label);
        //set the size of the frame
        frame.setSize(400, 400);
        //set the frame to visible
        frame.setVisible(true);
    }//main method close

    //paint method open
    public void paint(Graphics g){
        System.out.println("paint method called");
        //set the color to red
        g.setColor(Color.red);
        //draw a dot at (100, 100)
        g.fillOval(100, 100, 5, 5);
        //draw a dot at (200, 200)
        g.fillOval(200, 200, 5, 5);
        //set the color to black
        g.setColor(Color.black);
        //draw a label at (100, 100)
        g.drawString("{100, 100}", 100, 100);
        //draw a label at (200, 200)
        g.drawString("{200, 200}", 200, 200);
    }//paint method close
}//class close
