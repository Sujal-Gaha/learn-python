from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math
import sys


# Window dimensions
WIDTH, HEIGHT = 800, 800
angle = 0  # Angle for orbiting body

# Initialize OpenGL window
def init():
    glClearColor(0, 0, 0, 1)  # Black background
    glEnable(GL_DEPTH_TEST)

def draw_black_hole():
    glColor3f(1, 1, 1)
    glutSolidSphere(0.2, 50, 50)  # Black hole at center

def draw_orbiting_body():
    global angle
    orbit_radius = 0.6
    x = orbit_radius * math.cos(angle)
    y = orbit_radius * math.sin(angle)
    glPushMatrix()
    glTranslatef(x, y, 0)
    glColor3f(1, 1, 0)
    glutSolidSphere(0.05, 30, 30)  # Celestial body
    glPopMatrix()
    angle += 0.02

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)
    draw_black_hole()
    draw_orbiting_body()
    glutSwapBuffers()

def idle():
    glutPostRedisplay()

def main():
    glutInit(sys.argv)  # Pass command-line arguments
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Black Hole Simulation")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    glutMainLoop()

if __name__ == "__main__":
    main()
