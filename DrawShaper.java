import javax.swing.*;
import java.awt.*;

public class DrawShaper extends JPanel {

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;

        // Draw a line (Blue)
        g2d.setColor(Color.BLUE);
        g2d.setStroke(new BasicStroke(5));
        g2d.drawLine(50, 50, 450, 50);

        // Draw a filled rectangle (Green)
        g2d.setColor(Color.GREEN);
        g2d.fillRect(50, 100, 150, 200);

        // Draw a filled circle (Red)
        g2d.setColor(Color.RED);
        g2d.fillOval(300, 150, 100, 100);

        // Draw a filled ellipse (Cyan)
        g2d.setColor(Color.CYAN);
        g2d.fillOval(390, 350, 200, 100);

        // Draw a filled polygon (Magenta)
        int[] xPoints = { 300, 400, 350, 250, 200 };
        int[] yPoints = { 300, 350, 450, 450, 350 };
        g2d.setColor(Color.MAGENTA);
        g2d.fillPolygon(xPoints, yPoints, 5);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Graphics Primitives");
        DrawShaper panel = new DrawShaper();

        frame.add(panel);
        frame.setSize(500, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}