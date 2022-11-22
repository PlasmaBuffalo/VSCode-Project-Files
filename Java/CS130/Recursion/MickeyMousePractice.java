import java.awt.Canvas;
import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;

public class MickeyMousePractice extends Canvas {
    public static void main(String[] args) {
        JFrame frame = new JFrame("My Drawing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Canvas canvas = new MickeyMousePractice();
        canvas.setSize(400, 400);
        frame.add(canvas);
        frame.pack();
        frame.setVisible(true);
    }

    public void paint(Graphics g) {
        g.setColor(Color.black);
        // draw main head for mickey mouse
        // asume we have coordinates x and y, we know size of head
        int x = 200;
        int y = 200;
        int size = 100;
        // draw a circle at x, y with size = size
        g.fillOval(x, y, size, size);
        // decrease size for ears by half
        size = size / 2;
        // draw ears above head to the left and right sides so that they touch the head
        // circle
        g.fillOval(x - size / 2, y - size / 2, size, size);
        g.fillOval(x + size / 2 + size, y - size / 2, size, size);
    }

    //part 3: recursive method on ears
    //draws ears recursively, given a number of steps and the original size and position.
    public void drawEars(Graphics g, int steps, int x, int y, int size){
        //base case: if steps is 0, do nothing
        if(steps == 0){
            return;
        }
        //draw the ear
        g.fillOval(x, y, size, size);
        //decrease size by half
        size = size / 2;
        //draw the left ear
        drawEars(g, steps - 1, x - size / 2, y - size / 2, size);
        //draw the right ear
        drawEars(g, steps - 1, x + size / 2 + size, y - size / 2, size);
    }



}