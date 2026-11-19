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
TITLE = "Merge Sort"

def merge_steps(arr, lo, hi):
    if lo >= hi:
        return
    mid = (lo + hi) // 2
    yield from merge_steps(arr, lo, mid)
    yield from merge_steps(arr, mid + 1, hi)

    left = arr[lo:mid + 1]
    right = arr[mid + 1:hi + 1]
    i = j = 0
    k = lo
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        yield {k}
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        yield {k}
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        yield {k}
        k += 1

def draw(pen, arr, active, title, done=False):
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
    pen.goto(-460, 300)
    pen.pencolor("white")
    pen.write(title, font=("Arial", 20, "bold"))

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
    draw(pen, arr, set(), TITLE)
    screen.update()
    time.sleep(1)

    for active in merge_steps(arr, 0, len(arr) - 1):
        draw(pen, arr, active, TITLE)
        screen.update()
        time.sleep(ANIM_DELAY)

    draw(pen, arr, set(), TITLE, done=True)
    screen.update()
    screen.exitonclick()
