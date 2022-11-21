//objective: read in the coords.txt file and plot the points in a JFrame window

//imports
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;
import java.util.*;

//method to read in a set of points from a file and return an array of points
public class GUI_FileRead
{
    //main method
    public static void main(String[] args)
    {
        //create a new JFrame
        JFrame frame = new JFrame("GUI_FileRead");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setLocation(200, 200);
        frame.setVisible(true);
        
        //create a new JPanel
        JPanel panel = new JPanel();
        panel.setBackground(Color.white);
        frame.add(panel);
        
        //
        //call method to read in text file

    }
}