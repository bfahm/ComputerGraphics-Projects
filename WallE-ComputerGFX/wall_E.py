from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import *


def draw1():
    # background
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    # shoulder circles
    glColor(1, 0.5, 0)
    glBegin(GL_POLYGON)
    r = 0.05
    for u in arange(0, 2 * pi, 0.01):
        q = r * cos(u) + 0.09
        w = r * sin(u) + 0.33
        glVertex2d(q, w)
    glEnd()
    glColor(1, 0.5, 0)
    glBegin(GL_POLYGON)
    t = 0.05
    for u in arange(0, 2 * pi, 0.01):
        g = t * cos(u) - 0.09
        b = t * sin(u) + 0.33
        glVertex2d(g, b)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_POINTS)
    r = 0.05
    for u in arange(0, 2 * pi, 0.01):
        q = r * cos(u) + 0.09
        w = r * sin(u) + 0.33
        glVertex2d(q, w)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_POINTS)
    r = 0.05
    for u in arange(0, 2 * pi, 0.01):
        q = r * cos(u) - 0.09
        w = r * sin(u) + 0.33
        glVertex2d(q, w)
    glEnd()  # Shoulders
    glColor(0, 0, 0)
    glBegin(GL_POINTS)
    r = 0.07
    for u in arange(0, 2 * pi, 0.01):
        q = r * cos(u) + 0.11
        w = r * sin(u) + 0.56
        glVertex2d(q, w)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_POINTS)
    r = 0.07
    for u in arange(0, 2 * pi, 0.01):
        q = r * cos(u) - 0.11
        w = r * sin(u) + 0.56
        glVertex2d(q, w)
    glEnd()  # Eyes add On


    # Orange Body
    glColor(1, 0.5, 0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.4, 0.34)      # topLine Vertex1
    glVertex2d(0.4, 0.34)       # topLine Vertex2
    glVertex2d(0.4, -0.4)
    glVertex2d(-0.4, -0.4)
    glEnd()  # Orange Body
    # Orange Body_Outline
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(-0.4, 0.34)
    glVertex2d(0.4, 0.34)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(0.4, 0.34)
    glVertex2d(0.4, -0.4)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(0.4, -0.4)
    glVertex2d(-0.4, -0.4)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(-0.4, -0.4)
    glVertex2d(-0.4, 0.34)
    glEnd()  # Orange Body_Outline
    # Gray neck
    glColor(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex2d(-0.075, 0.34)
    glVertex2d(0.075, 0.34)
    glVertex2d(0.075, 0.7)          # topline v1
    glVertex2d(-0.075, 0.7)         # topline v2
    glEnd()
    # Left Eye
    glColor(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex2d(0.008, 0.57)
    glVertex2d(0.3, 0.48)
    glVertex2d(0.3, 0.7)
    glVertex2d(0.008, 0.79)
    glEnd()
    # Right Eye
    glColor(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex2d(-0.008, 0.57)
    glVertex2d(-0.3, 0.48)
    glVertex2d(-0.3, 0.7)
    glVertex2d(-0.008, 0.79)
    glEnd()  # UpperBody without eyes
    # Right Eye
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    r = 0.08
    for theta in arange(0, 2*pi, 0.01):
        x=r*cos(theta)+0.15
        y=r*sin(theta)+0.64
        glVertex2d(x, y)
    glEnd()
    glColor(0.28, 0.75, 1)
    glBegin(GL_POLYGON)
    r = 0.068
    for theta in arange(0, 2 * pi, 0.01):
        x = r * cos(theta) + 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()
    glColor(0.24, 0.13, 1)
    glBegin(GL_POLYGON)
    r = 0.05
    for theta in arange(0, 2 * pi, 0.01):
        x = r * cos(theta) + 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()
    glColor(0.5, 0.82, 1)
    glBegin(GL_POLYGON)
    r = 0.03
    for theta in arange(0, 2 * pi, 0.01):
        x = r * cos(theta) + 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()
    # Left Eye
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    r = 0.08
    for theta in arange(0, 2 * pi, 0.01):
        x = r * cos(theta) - 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()
    glColor(0.28, 0.75, 1)
    glBegin(GL_POLYGON)
    r = 0.068
    for theta in arange(0, 2 * pi, 0.01):
        x = r * cos(theta) - 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()
    glColor(0.24, 0.13, 1)
    glBegin(GL_POLYGON)
    r = 0.05
    for theta in arange(0, 2 * pi, 0.01):
        x = r * cos(theta) - 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()
    glColor(0.5, 0.82, 1)
    glBegin(GL_POLYGON)
    r = 0.03
    for theta in arange(0, 2 * pi, 0.01):
        x = r * cos(theta) - 0.15
        y = r * sin(theta) + 0.64
        glVertex2d(x, y)
    glEnd()  # Eyes
    # Right Leg
    glColor(0.25, 0.25, 0.25)
    glBegin(GL_POLYGON)
    glVertex2d(0.39, -0.07)   # topLine Vertex1
    glVertex2d(0.7, -0.07)   # topLine Vertex2
    glVertex2d(0.7, -0.7)
    glVertex2d(0.39, -0.7)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(0.39, -0.2)  # topLine Vertex1
    glVertex2d(0.7, -0.2)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(0.39, -0.3)  # topLine Vertex1
    glVertex2d(0.7, -0.3)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(0.39, -0.4)  # topLine Vertex1
    glVertex2d(0.7, -0.4)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(0.39, -0.5)  # topLine Vertex1
    glVertex2d(0.7, -0.5)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(0.39, -0.6)  # topLine Vertex1
    glVertex2d(0.7, -0.6)
    glEnd() # Black Wheel Line

    # Left Leg
    glColor(0.25, 0.25, 0.25)
    glBegin(GL_POLYGON)
    glVertex2d(-0.39, -0.07)  # topLine Vertex1
    glVertex2d(-0.7, -0.07)  # topLine Vertex2
    glVertex2d(-0.7, -0.7)
    glVertex2d(-0.39, -0.7)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(-0.4, -0.2)  # topLine Vertex1
    glVertex2d(-0.7, -0.2)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(-0.4, -0.3)  # topLine Vertex1
    glVertex2d(-0.7, -0.3)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(-0.4, -0.4)  # topLine Vertex1
    glVertex2d(-0.7, -0.4)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(-0.4, -0.5)  # topLine Vertex1
    glVertex2d(-0.7, -0.5)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(-0.4, -0.6)  # topLine Vertex1
    glVertex2d(-0.7, -0.6)
    glEnd()
    # Right Hand
    glColor(0.35, 0.35, 0.35)
    glBegin(GL_POLYGON)
    glVertex2d(0.39, 0.3)
    glVertex2d(0.63, 0.3)
    glVertex2d(0.63, 0.03)
    glVertex2d(0.39, 0.03)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(0.51, 0.29)
    glVertex2d(0.51, 0.03)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(0.62, 0.2)
    glVertex2d(0.39, 0.2)
    glEnd()
    # Left Hand
    glColor(0.35, 0.35, 0.35)
    glBegin(GL_POLYGON)
    glVertex2d(-0.39, 0.3)
    glVertex2d(-0.63, 0.3)
    glVertex2d(-0.63, 0.03)
    glVertex2d(-0.39, 0.03)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(-0.51, 0.29)
    glVertex2d(-0.51, 0.03)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(-0.62, 0.2)
    glVertex2d(-0.39, 0.2)
    glEnd()  # Hands

    # BlackWhite Strip
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2d(0.389, -0.32)
    glVertex2d(-0.389, -0.32)
    glVertex2d(-0.389, -0.18)
    glVertex2d(0.389, -0.18)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.39, -0.18)    #1
    glVertex2d(-0.29, -0.32)    #2
    glVertex2d(-0.09, -0.32)    #4
    glVertex2d(-0.19, -0.18)    #3
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(0.01, -0.18)  # 1
    glVertex2d(0.11, -0.32)  # 2
    glVertex2d(0.31, -0.32)  # 4
    glVertex2d(0.21, -0.18)  # 3
    glEnd()  # black white strip
    # blueBox
    glColor(0.33, 0.22, 0.83)
    glBegin(GL_POLYGON)
    glVertex2d(0.1, 0.3)  # topLine Vertex1
    glVertex2d(0.3, 0.3)  # topLine Vertex2
    glVertex2d(0.3, 0.1)
    glVertex2d(0.1, 0.1)
    glEnd()
    # circleInBox
    glColor(1, 0.78, 0.27)
    glBegin(GL_POLYGON)
    rr = 0.04
    for gamma in arange(0, 2*pi, 0.01):
        p=rr*cos(gamma)+0.15
        l=rr*sin(gamma)+0.15
        glVertex2d(p, l)
    glEnd()
    # line in box
    glColor(1, 0.78, 0.27)
    glBegin(GL_LINES)
    glVertex2d(0.25, 0.1)
    glVertex2d(0.25, 0.3)
    glEnd()
    glColor(1, 0.78, 0.27)
    glBegin(GL_LINES)
    glVertex2d(0.27, 0.1)
    glVertex2d(0.27, 0.3)
    glEnd()  # blue box and Stuff
    # Left and right triangle
    glColor(0.4, 0.4, 0.4)
    glBegin(GL_POLYGON)
    glVertex2d(0.39, -0.4)
    glVertex2d(0.39, -0.6)
    glVertex2d(0.29, -0.4)
    glEnd()
    glColor(0.4, 0.4, 0.4)
    glBegin(GL_POLYGON)
    glVertex2d(-0.39, -0.4)
    glVertex2d(-0.39, -0.6)
    glVertex2d(-0.29, -0.4)
    glEnd()  # triangles at bottom
    # rectang yellows
    glColor(1, 0.001, 0.02)
    glBegin(GL_POLYGON)
    glVertex2d(-0.02, 0.08)  # topLine Vertex1
    glVertex2d(0.02, 0.08)  # topLine Vertex2
    glVertex2d(0.02, -0.13)
    glVertex2d(-0.02, -0.13)
    glEnd()
    glColor(1, 0.001, 0.02)
    glBegin(GL_POLYGON)
    glVertex2d(-0.2, 0.08)  # topLine Vertex1
    glVertex2d(-0.24, 0.08)  # topLine Vertex2
    glVertex2d(-0.24, -0.13)
    glVertex2d(-0.2, -0.13)
    glEnd()
    glColor(1, 0.001, 0.02)
    glBegin(GL_POLYGON)
    glVertex2d(0.2, 0.08)  # topLine Vertex1
    glVertex2d(0.24, 0.08)  # topLine Vertex2
    glVertex2d(0.24, -0.13)
    glVertex2d(0.2, -0.13)
    glEnd()  # body yellows
    # neck oranges
    glColor(1, 0.5, 0)
    glBegin(GL_POLYGON)
    glVertex2d(0.02, 0.34)
    glVertex2d(0.029, 0.34)
    glVertex2d(0.029, 0.56)  # topline v1
    glVertex2d(0.02, 0.56)  # topline v2
    glEnd()
    glColor(1, 0.5, 0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.02, 0.34)
    glVertex2d(-0.029, 0.34)
    glVertex2d(-0.029, 0.56)  # topline v1
    glVertex2d(-0.02, 0.56)  # topline v2
    glEnd()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Wall.E")
glutInitWindowSize(1000, 1000)  # Set the window's initial width & height
glutDisplayFunc(draw1)
glutMainLoop()
