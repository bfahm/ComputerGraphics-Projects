from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def initialize_scene():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1, 0.1, 50)
    gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)  # eye, center, up
    glClearColor(1, 0.78, 0.39, 1)


def car(start, z):
    # attributes tba
    global x
    global x1
    global x2
    global x3
    global xroad
    global flag
    global flag1
    global flag2
    global myAngle

    glMatrixMode(GL_MODELVIEW)  # defines how objects are transformed(translation, rotation, scaling)

    # road outline
    glLoadIdentity()
    glBegin(GL_LINES)
    glVertex3d(-50, 0, -7)
    glVertex3d(40, 2, -7)
    glEnd()
    glLoadIdentity()
    glBegin(GL_LINES)
    glVertex3d(-40, 2, 7)
    glVertex3d(40, 5, 7)
    glEnd()

    # road base
    glColor3d(1, 1, 1)
    glLoadIdentity()
    glBegin(GL_POLYGON)
    glVertex3d(-50, 0, -6.9)
    glVertex3d(-40, 2, 6.9)
    glVertex3d(40, 5, 7)
    glVertex3d(40, 2, -7)
    glEnd()  # road

    delta = 8   # space between lanes

    # car lower body
    glColor3f(0.1, 0.6, 0.5)
    glLoadIdentity()
    glTranslate(x + start, 0, z)
    glScale(0.75, 0.25, 0.5)
    glutSolidCube(5)
    # car upper body
    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(x + start, 1, z)
    glScale(0.4, 0.15, 0.5)
    glutWireCube(5)
    # four wheels
    glColor(0, 0, 0)

    glLoadIdentity()
    glTranslate(1.5 + x + start, -0.625, 1.3 + z)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)  # inner radius, outer radius, number of lines, number of circles
    glLoadIdentity()
    glTranslate(-1.5 + x + start, -0.625, 1.3 + z)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)
    glLoadIdentity()
    glTranslate(1.5 + x + start, -0.625, -1.5 + z)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)
    glLoadIdentity()
    glTranslate(-1.5 + x + start, -0.625, -1.5 + z)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)  # four wheels  # first car (with x)

    # car lower body
    glColor3f(0.1, 0.9, 0.5)
    glLoadIdentity()
    glTranslate(- x1 - start, 0, z + delta)
    glScale(0.75, 0.25, 0.5)
    glutSolidCube(5)
    # car upper body
    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(- x1 - start, 1, z + delta)
    glScale(0.4, 0.15, 0.5)
    glutWireCube(5)
    # four wheels
    glColor(0, 0, 0)

    glLoadIdentity()
    glTranslate(1.5 - x1 - start, -0.625, 1.3 + z + delta)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)  # inner radius, outer radius, number of lines, number of circles
    glLoadIdentity()
    glTranslate(-1.5 - x1 - start, -0.625, 1.3 + z + delta)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)
    glLoadIdentity()
    glTranslate(1.5 - x1 - start, -0.625, -1.5 + z + delta)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)
    glLoadIdentity()
    glTranslate(-1.5 - x1 - start, -0.625, -1.5 + z + delta)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)  # four wheels  # second car (with x1)

    # car lower body
    glColor3f(0.5, 0.6, 0.5)
    glLoadIdentity()
    glTranslate(-x2 - start, 0, z + delta)
    glScale(0.75, 0.25, 0.5)
    glutSolidCube(5)
    # car upper body
    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(-x2 - start, 1, z + delta)
    glScale(0.4, 0.15, 0.5)
    glutWireCube(5)
    # four wheels
    glColor(0, 0, 0)

    glLoadIdentity()
    glTranslate(1.5 - x2 - start, -0.625, 1.3 + z + delta)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)  # inner radius, outer radius, number of lines, number of circles
    glLoadIdentity()
    glTranslate(-1.5 - x2 - start, -0.625, 1.3 + z + delta)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)
    glLoadIdentity()
    glTranslate(1.5 - x2 - start, -0.625, -1.5 + z + delta)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)
    glLoadIdentity()
    glTranslate(-1.5 - x2 - start, -0.625, -1.5 + z + delta)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)  # four wheels  # third car (with x2)

    # car lower body
    glColor3f(0.6, 0.6, 0.5)
    glLoadIdentity()
    glTranslate(x3 + start, 0, z)
    glScale(0.75, 0.25, 0.5)
    glutSolidCube(5)
    # car upper body
    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(x3 + start, 1, z)
    glScale(0.4, 0.15, 0.5)
    glutWireCube(5)
    # four wheels
    glColor(0, 0, 0)

    glLoadIdentity()
    glTranslate(1.5 + x3 + start, -0.625, 1.3 + z)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)  # inner radius, outer radius, number of lines, number of circles
    glLoadIdentity()
    glTranslate(-1.5 + x3 + start, -0.625, 1.3 + z)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)
    glLoadIdentity()
    glTranslate(1.5 + x3 + start, -0.625, -1.5 + z)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)
    glLoadIdentity()
    glTranslate(-1.5 + x3 + start, -0.625, -1.5 + z)
    glRotate(myAngle, 0, 0, 1)
    glutWireTorus(0.14, 0.35, 15, 10)  # four wheels# first car (with x)  # final car (with x3)

    # road middle lines
    for i in range(-30, 70, 6):
        glLoadIdentity()
        glTranslate(i + xroad, 0, 0)
        glBegin(GL_POLYGON)
        glVertex3d(0, 0, -2)
        glVertex3d(3, 0, -2)
        glVertex3d(3, 0, -1.3)
        glVertex3d(0, 0, -1.3)
        glEnd()  # road slicer

    # animation
    speed_factor = 0.01
    x += speed_factor * -flag
    myAngle -= (speed_factor / 0.022) * flag
    if xroad > -55:
        xroad -= 0.004
    if x2 >= 6:
        x2 -= speed_factor * flag2
        myAngle -= (speed_factor / 0.022) * flag2
    else:
        x1 += 0.003 * -flag1
        x2 -= 0.002 * flag2
    x3 -= 0.007  # animation

    glFlush()


def main():
    glClear(GL_COLOR_BUFFER_BIT)
    car(-8, -6)


x = 25
x1 = 0
x2 = 20
x3 = 50
xroad = 0
flag = 1
flag1 = 1
flag2 = 1
myAngle = 0

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(700, 700)
glutCreateWindow(b"AnimationCar")
initialize_scene()
glutDisplayFunc(main)
glutIdleFunc(main)
glutMainLoop()
