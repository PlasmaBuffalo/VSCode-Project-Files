/*
 * Code to create a fractal triangle using recursion
 * Draws a downward-pointing triangle to start, and recursively draws upwards triangles inscribed in the previous triangle
 * Recursively draws triangles to the upper left, upper right, and below the previous triangle.
 */

//import necessary libraries
import java.awt.*;
import javax.swing.*;
import java.util.*;
import java.awt.event.*;

public class RecursiveArt extends Canvas {
    // main method
    public static void main(String[] args) {
        // create 2d array of points to pass into recursive method
/*         int[][] initial = new int[][] { { 500, 250 }, { 250, 750 }, { 750, 750 } };
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of levels of recursion: ");
        int levels = input.nextInt();
        input.close(); */

        // create a new frame
        JFrame frame = new JFrame("Recursive Art");
        // set the size of the frame
        frame.setSize(1000, 1000);
        // set the frame to exit when closed
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // create a new canvas
        RecursiveArt canvas = new RecursiveArt();
        // add the canvas to the frame
        frame.add(canvas);
        // make the frame visible
        frame.setVisible(true);

    }

    // paint method
    public void paint(Graphics g) {
        // start with a downward-pointing triangle:
        int[][] initial = new int[][] { { 500, 750 }, { 250, 250 }, { 750, 250 } };
        g.setColor(Color.black);
        // draw the initial triangle given the initial array of points
        g.fillPolygon(new int[] { initial[0][0], initial[1][0], initial[2][0] },
                new int[] { initial[0][1], initial[1][1], initial[2][1] }, 3);
        // given initial triangle, three recursive calls to paint new triangles to the
        // upper left, upper right, and below
        // recursive method takes in the coordinates of the initial triangle, graphics
        // object, and the current level of recursion.
        // if base case == 0, then stop recursion.
        // call recursive method
        recursiveTriangle(g, initial, 2);
    }

    // recursive method to draw triangles
    public void recursiveTriangle(Graphics g, int[][] lastTri, int level) {
        // base case
        if (level == 1) {
            return;
        }
        // recursive case
        else {
            // change the color based on the level
            g.setColor(new Color(0, level * 15, 255 - level*10));
            // calculate the coordinates of the new triangles
            // 2D array indicates three pairs of 2 coordinates
            // upper left
            int[][] upLeft = new int[3][2];
            upLeft[0][0] = lastTri[0][0];
            upLeft[0][1] = lastTri[0][1];
            upLeft[1][0] = (lastTri[0][0] + lastTri[1][0]) / 2;
            upLeft[1][1] = (lastTri[0][1] + lastTri[1][1]) / 2;
            upLeft[2][0] = (lastTri[0][0] + lastTri[2][0]) / 2;
            upLeft[2][1] = (lastTri[0][1] + lastTri[2][1]) / 2;
            // upper right
            int[][] upRight = new int[3][2];
            upRight[0][0] = lastTri[1][0];
            upRight[0][1] = lastTri[1][1];
            upRight[1][0] = (lastTri[1][0] + lastTri[0][0]) / 2;
            upRight[1][1] = (lastTri[1][1] + lastTri[0][1]) / 2;
            upRight[2][0] = (lastTri[1][0] + lastTri[2][0]) / 2;
            upRight[2][1] = (lastTri[1][1] + lastTri[2][1]) / 2;
            // below
            int[][] below = new int[3][2];
            below[0][0] = lastTri[2][0];
            below[0][1] = lastTri[2][1];
            below[1][0] = (lastTri[2][0] + lastTri[0][0]) / 2;
            below[1][1] = (lastTri[2][1] + lastTri[0][1]) / 2;
            below[2][0] = (lastTri[2][0] + lastTri[1][0]) / 2;
            below[2][1] = (lastTri[2][1] + lastTri[1][1]) / 2;
            // draw the new triangles
            g.fillPolygon(new int[] { upLeft[0][0], upLeft[1][0], upLeft[2][0] },
                    new int[] { upLeft[0][1], upLeft[1][1], upLeft[2][1] }, 3);

            g.fillPolygon(new int[] { upRight[0][0], upRight[1][0], upRight[2][0] },
                    new int[] { upRight[0][1], upRight[1][1], upRight[2][1] }, 3);

            g.fillPolygon(new int[] { below[0][0], below[1][0], below[2][0] },
                    new int[] { below[0][1], below[1][1], below[2][1] }, 3);

            // call recursive method on each new triangle
            recursiveTriangle(g, upLeft, level - 1);
            recursiveTriangle(g, upRight, level - 1);
            recursiveTriangle(g, below, level - 1);
        }

    }
}