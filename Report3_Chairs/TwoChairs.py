from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def initialize_scene():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(700, 700)
    glutCreateWindow(b"HandsomeChairs")

    glutDisplayFunc(draw_main)
    glutIdleFunc(draw_main)
    glutMainLoop()


def draw_main():
    glLoadIdentity()
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1, 0.1, 50)
    gluLookAt(6, 5, 10, 0, -3, 0, 0, 1, 0)

    draw_back(-3)
    draw_base(-3)
    bunch_of_legs(-1)

    draw_back(3)
    draw_base(3)
    bunch_of_legs(1)

    glFlush()


def draw_back(x_coor):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0)
    glTranslate(x_coor, 0, 0)
    glScale(2, 2, 0.3)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()


def draw_base(x_coor):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0)
    glTranslate(x_coor, -1.7, 1.7)
    glScale(2, 0.3, 2)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()


def each_leg(x, y, z):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0)
    glTranslate(x, y, z)
    glScale(0.3, 2, 0.3)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()


def bunch_of_legs(x_value):
    each_leg(-4.7 * x_value, -3.4, 3.4)
    each_leg(-4.7 * x_value, -3.4, 0)
    each_leg(-1.3 * x_value, -3.4, 0)
    each_leg(-1.3 * x_value, -3.4, 3.4)


initialize_scene()
