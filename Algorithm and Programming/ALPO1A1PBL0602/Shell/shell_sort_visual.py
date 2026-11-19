import turtle
import time
import colorsys

def read_numbers(filename):
    with open(filename) as f:
        return [int(line) for line in f if line.strip()]

SIZE = 100000  # use the full file; set to 50 to watch the animation at a readable speed
NUMBERS = read_numbers("random100K.txt")[:SIZE]

ANIM_DELAY = 0.02
LEFT, BASE, MAX_H = -460, -260, 480
TITLE = "Shell Sort"

def shell_steps(arr):
    # Each step yields (bars to highlight, status text)
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                yield {j, j - gap}, f"Gap {gap}, Index {j}"
                j -= gap
            arr[j] = temp
            yield {j}, f"Gap {gap}, Index {j}"
        gap //= 2

def draw(pen, arr, active, title, status="", done=False):
    pen.clear()
    maxv = max(arr)
    w = 900 / len(arr)
    for i, v in enumerate(arr):
        h = v / maxv * MAX_H
        if done:
            color = (0.2, 1.0, 0.4)
        elif i in active:
            color = (1.0, 1.0, 1.0)
        else:
            color = colorsys.hsv_to_rgb(v / maxv * 0.8, 0.85, 1.0)
        pen.penup()
        pen.goto(LEFT + i * w, BASE)
        pen.setheading(0)
        pen.pendown()
        pen.pencolor(color)
        pen.fillcolor(color)
        pen.begin_fill()
        for _ in range(2):
            pen.forward(w * 0.8)
            pen.left(90)
            pen.forward(h)
            pen.left(90)
        pen.end_fill()
    pen.penup()
    pen.pencolor("white")
    pen.goto(-460, 300)
    pen.write(title, font=("Arial", 20, "bold"))
    pen.goto(-460, -320)
    pen.write(status, font=("Arial", 16, "normal"))

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(1000, 650)
    screen.bgcolor("black")
    screen.title(TITLE)
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    arr = NUMBERS[:]
    draw(pen, arr, set(), TITLE, "Starting")
    screen.update()
    time.sleep(1)

    for active, status in shell_steps(arr):
        draw(pen, arr, active, TITLE, status)
        screen.update()
        time.sleep(ANIM_DELAY)

    draw(pen, arr, set(), TITLE, "Done", done=True)
    screen.update()
    screen.exitonclick()
