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

}