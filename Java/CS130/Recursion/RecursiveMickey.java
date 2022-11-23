package CS130.Recursion;
/*
 * @PlasmaBuffalo, kgormley
 * Thanks to Java for having thread-unsafe drawing.
 * 
 */
import java.awt.Canvas;
import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class RecursiveMickey extends Canvas {
    public static void main(String[] args) {
        JFrame frame = new JFrame("My Drawing");// create frame
        frame.setSize(400, 400);// sizes the frame to fit everything
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);// end program when frame closed
        frame.setAlwaysOnTop(true);// keep frame on top of other windows

        // create a panel to hold the canvas
        JPanel panel = new JPanel();
        panel.setBackground(Color.white);// set panel background color

        RecursiveMickey rm = new RecursiveMickey();// instance of class, which is a canvas
        rm.setSize(400, 400);// size of canvas
        rm.setBackground(Color.white);// set canvas background color

        panel.add(rm);// add canvas to panel
        frame.add(panel);// add panel to frame
        frame.setVisible(true);// make frame visible

        //wait for the frame to be visible before drawing
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        Graphics g = rm.getGraphics();// get graphics object from canvas
        System.out.println(g);// print rm's graphics object
        // notice it is now not null because we added it to the frame and made it
        // visible before printing

        // call paint method
        rm.paint(g, 200, 200, 100, 3);
    }

    public void paint(Graphics g, int midX, int midY, int size, int rec) {// using midpoints for easier math, rec is the
        if (rec == 0) {// stop recursion if rec is 0
            return;
        }
        // change color based on recursion level
        g.setColor(Color.BLACK);
        int drawX = midX - (size / 2);
        int drawY = midY - (size / 2);// go from mid point to upper left corner(point needed to draw)
        g.fillOval(drawX, drawY, size, size);
        paint(g, drawX, drawY, size / 2, rec - 1);// recurse left
        paint(g, drawX + size, drawY, size / 2, rec - 1);// recurse right
    }
}