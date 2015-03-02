
import math
from OpenGL.raw.GLUT import glutSolidSphere
import pygame

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from random import randint


verticies = (
    (1,     -1, -1),
    (1,     1,  -1),
    (-1,    1,  -1),
    (-1,    -1, -1),
    (1,     -1, 1),
    (1,     1,  1),
    (-1,    -1, 1),
    (-1,    1,  1)
)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1)
)

def Cube():
    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])

    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def Sphere(radius):

    sphere = gluNewQuadric()
    gluQuadricDrawStyle(sphere,GLU_LINE);
    gluSphere(sphere,radius,20,20)
    #glutWireSphere(2,100,20)

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 200.0)

    glTranslatef(0,0, -50)

    glRotatef(25, 2, 1, 0)
    glTranslatef(5,1,0.0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,0.5,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-0.5,0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)
                if event.button == 5:
                    glTranslatef(0,0,-1.0)


        glTranslatef(-10,0,0)
        glRotatef(0.5, 0, 0, 1)
        glTranslatef(10,0,0.0)

        glPushMatrix()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glColor3f(0, 0, 1)
        Sphere(1)
        glColor3f(1, 1, 0)
        glTranslatef(-10, 0, 0)
        Sphere(2)
        glPopMatrix()

        """glPushMatrix()
        glRotatef(-0.5, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Sphere()
        glColor3f(0, 0, 1)
        glPopMatrix()"""

        pygame.display.flip()
        pygame.time.wait(10)

main()