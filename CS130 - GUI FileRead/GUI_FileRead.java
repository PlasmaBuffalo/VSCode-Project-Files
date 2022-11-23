//Create a .txt file and copy the following sequence of numbers into it, these will be the x,y coordinates of dots in the GUI you produce. 

//import statements
import java.awt.*;
import javax.swing.*;
import java.io.*;
import java.util.*;

//main class (extends Canvas)
public class GUI_FileRead extends Canvas{
    //main method
    public static void main(String[] args) {
        //instance of main class
        GUI_FileRead gfr = new GUI_FileRead();
        //create a new JFrame
        JFrame frame = new JFrame("GUI_FileRead");
        //create a new Canvas
        Canvas canvas = new GUI_FileRead();
        //set the size of the canvas
        canvas.setSize(400, 400);
        //add the canvas to the frame
        frame.add(canvas);
        //set the size of the frame
        frame.setSize(400, 400);
        //set the frame to visible
        frame.setVisible(true);

        Graphics g = canvas.getGraphics();
        //call coordinateRead method and pass to paint
        gfr.paint(g, gfr.coordinateRead());
        

    }

    //coordinateRead method
    public ArrayList<String> coordinateRead(){
        //create a new ArrayList
        ArrayList<String> coordinates = new ArrayList<String>();
        //try to read the file
        try{
            //create a new File object
            File file = new File("coords.txt");
            //create a new Scanner object
            Scanner scanner = new Scanner(file);
            //while the file has a next line
            while(scanner.hasNextLine()){
                //add the next line to the ArrayList
                coordinates.add(scanner.nextLine());
            }
            //close the scanner
            scanner.close();
        } catch (FileNotFoundException e){
            //if the file is not found, print the error
            System.out.println("File not found");
        }
        //return the ArrayList
        return coordinates;
    }

    //paint method
    public void paint(Graphics g, ArrayList<String> coords){
        //for each coordinate pair, draw a dot
        for(int i = 0; i < coords.size(); i++){
            //split the string into two parts
            String[] parts = coords.get(i).split(" ");
            //convert the parts into integers
            int x = Integer.parseInt(parts[0]);
            int y = Integer.parseInt(parts[1]);
            //draw a dot at the coordinates
            g.fillOval(x, y, 5, 5);
        }
    }
}