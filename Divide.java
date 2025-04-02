import java.awt.*;
import javax.swing.*;

public class Divide extends JPanel {
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;

        
        // Set background color
        setBackground(Color.CYAN);
        
        // Get panel width and height
        int width = getWidth();
        int height = getHeight();
        
        // Draw lines to divide screen into four equal parts
        g.setColor(Color.BLACK);
        g.drawLine(width / 2, 0, width / 2, height);
        g.drawLine(0, height / 2, width, height / 2);
        //for rectangle in the firSt coordinate
        g2d.setColor(Color.GREEN);
        g2d.fillRect(50, 100, 150, 150);
        //for circle in second
        g2d.setColor(Color.RED);
        g2d.fillOval(350, 150, 100, 100);

        //for ellipse
        g2d.setColor(Color.YELLOW);
        g2d.fillOval(0, 350, 200, 100);

        //for line
        g2d.setColor(Color.ORANGE);
        g2d.setStroke(new BasicStroke(10));
        g2d.drawLine(350, 350, 450, 450); 

    }
    
    public static void main(String[] args) {
        JFrame frame = new JFrame("Screen Division");
        Divide panel = new Divide();
        
        frame.add(panel);
        frame.setSize(600, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}