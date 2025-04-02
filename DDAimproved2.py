from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def dda_algorithm(x1, y1, x2, y2):
    # Calculate differences
    dx = x2 - x1
    dy = y2 - y1

    # Determine the number of steps
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Calculate increments
    x_increment = dx / steps
    y_increment = dy / steps

    # Generate the points and draw them
    x, y = x1, y1
    glBegin(GL_POINTS)  # Start drawing points
    for _ in range(int(steps) + 1):
        glVertex2i(int(x + 0.5), int(y + 0.5))  # Round manually
        x += x_increment
        y += y_increment
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(1.0, 0.0, 0.0)  # Set the drawing color to red
    dda_algorithm(50, 100, 300, 400)  # Draw a line
    glFlush()  # Force execution of GL commands

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set the background color to white
    glColor3f(0.0, 0.0, 0.0)  # Set the drawing color to black
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, 500, 0, 500)  # Set up a 2D orthographic projection

# Main function
def main():
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Single buffer, RGB mode
    glutInitWindowSize(500, 500)  # Set the window size
    glutInitWindowPosition(100, 100)  # Set the window position
    glutCreateWindow("DDA Line Drawing in OpenGL")  # Create the window
    init()  # Initialize settings
    glutDisplayFunc(display)  # Set the display callback
    glutMainLoop()  # Enter the GLUT event processing loop

if __name__ == "__main__":
    main()