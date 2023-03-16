
import turtle
import math

t = turtle.Turtle()
t.speed(0)

corners = [(100, 100, 100),
           (100, -100, 100),
           (-100, -100, 100),
           (-100, 100, 100),
           (100, 100, -100),
           (100, -100, -100),
           (-100, -100, -100),
           (-100, 100, -100)]

edges = [(0, 1), (1, 2), (2, 3), (3, 0),         (4, 5), (5, 6), (6, 7), (7, 4),         (0, 4), (1, 5), (2, 6), (3, 7)]


def rotate_x(theta):
    theta = theta * math.pi / 180
    for i in range(len(corners)):
        x, y, z = corners[i]
        y = int(y * math.cos(theta) - z * math.sin(theta))
        z = int(y * math.sin(theta) + z * math.cos(theta))
        corners[i] = (x, y, z)

def rotate_y(theta):
    theta = theta * math.pi / 180
    for k in range(len(corners)):
        x, y, z = corners[k]
        x = int(x * math.cos(theta) + z * math.sin(theta))
        z = int(-x * math.sin(theta) + z * math.cos(theta))
        corners[k] = (x, y, z)
        
def rotate_z(theta):
    theta = theta * math.pi / 180
    for l in range(len(corners)):
        x, y, z = corners[l]
        x_new = int(x * math.cos(theta) - y * math.sin(theta))
        y_new = int(x * math.sin(theta) + y * math.cos(theta))
        corners[l] = (x_new, y_new, z)
def project(coords):
    distance = 500
    factor = distance / (distance - coords[2])
    x = coords[0] * factor
    y = coords[1] * factor
    return (x, y)

def draw_cube():
    for edge in edges:
        x1, y1 = project(corners[edge[0]])
        x2, y2 = project(corners[edge[1]])
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)

for j in range(360):
    t.clear()
    rotate_x(j)
    rotate_y(j)
    draw_cube()

turtle.done()