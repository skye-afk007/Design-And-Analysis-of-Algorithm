import javax.swing.*;
import java.awt.*;

public class DrawShapes extends JPanel {

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;

        int width = getWidth();
        int height = getHeight();
        int centerX = width / 2;
        int centerY = height / 2;

        // --- Quadrant 1: Circle (Red) ---
        g2d.setColor(Color.RED);
        g2d.fillOval(centerX / 2 - 50, centerY / 2 - 50, 100, 100);

        // --- Quadrant 2: Arc (Yellow) ---
        g2d.setColor(Color.YELLOW);
        g2d.setStroke(new BasicStroke(5));
        g2d.drawArc(centerX / 2 - 80, centerY + centerY / 2 - 40, 160, 60, 0, 180);

        // --- Quadrant 3: Ellipse (Blue) ---
        g2d.setColor(Color.BLUE);
        g2d.fillOval(centerX + centerX/ 2 - 60, centerY / 2 - 60, 190, 120);

        // --- Quadrant 4: Rectangle (Green) ---
        g2d.setColor(Color.GREEN);
        g2d.fillRect(centerX / 2 - 50, centerY / 2 - 50, centerX / 2, centerY / 2);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Draw Shapes");
        DrawShapes panel = new DrawShapes();

        frame.add(panel);
        frame.setSize(500, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}

