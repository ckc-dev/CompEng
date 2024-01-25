import random
from pathlib import Path

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

DISPLAY = (800, 800)
CLOCK = pygame.time.Clock()
FACES_PATH = Path(__file__).parent / "faces.txt"
VERTICES_PATH = Path(__file__).parent / "vertices.txt"

PAINTS = [
    (255, 0, 0),      # red
    (255, 255, 0),    # yellow
    (0, 255, 0),      # green
    (255, 0, 255),    # magenta
    (0, 255, 255),    # cyan
    (255, 165, 0),    # orange
    (255, 20, 147),   # deep pink
    (0, 128, 255),    # deep sky blue
    (255, 255, 255),  # white
]

BASE_COLOR = random.randint(0, len(PAINTS) - 1)


def get_list(file, scale_factor=1):
    list_ = []
    with open(file) as f:
        for line in f:
            line = line.rstrip(",\r\n").replace("(", "").replace(")", "").replace(" ", "")
            row = list(line.split(","))
            list_.append(row)
    list_ = [[float(j) * scale_factor for j in i] for i in list_]
    return list_


FACES = get_list(FACES_PATH)
VERTICES = get_list(VERTICES_PATH)


def draw_faces():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    for face in FACES:
        color = BASE_COLOR
        for vertex in face:
            color = color + 1 if color < len(PAINTS) - 1 else color - len(PAINTS)
            glColor3fv(PAINTS[color])
            glVertex3fv(VERTICES[int(vertex)])
    glEnd()


def main():
    pygame.init()
    pygame.display.set_caption("render.py")
    pygame.display.set_mode(DISPLAY, DOUBLEBUF | OPENGL)
    gluPerspective(60, (DISPLAY[0] / DISPLAY[1]), 0.01, 1000.0)
    glTranslate(0, 0, -1)
    glRotate(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                global BASE_COLOR
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    BASE_COLOR = random.randint(0, len(PAINTS) - 1)
                elif pygame.K_1 <= event.key <= pygame.K_9:
                    BASE_COLOR = event.key - pygame.K_1

        glRotate(.1, 0, .1, 0)
        pygame.display.flip()
        draw_faces()
        CLOCK.tick(60)


if __name__ == "__main__":
    main()
