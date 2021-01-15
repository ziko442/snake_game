from turtle import Turtle, Screen
import time

screen = Screen()
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def wall_distance(self, func):
        # detect snake dispense with wall
        if self.head.xcor() > 280:
            for seg_item in self.segments:
                seg_item.goto(seg_item.xcor() - 560, seg_item.ycor())
                func()
                screen.update()
                time.sleep(0.1)
                self.move()
        if self.head.xcor() < -280:
            for seg_item in self.segments:
                seg_item.goto(seg_item.xcor() + 560, seg_item.ycor())
                func()
                screen.update()
                time.sleep(0.1)
                self.move()

        if self.head.ycor() > 280:
            for seg_item in self.segments:
                seg_item.goto(seg_item.xcor(), seg_item.ycor() - 560)
                func()
                screen.update()
                time.sleep(0.1)
                self.move()

        if self.head.ycor() < -280:
            for seg_item in self.segments:
                seg_item.goto(seg_item.xcor(), seg_item.ycor() + 560)
                func()
                screen.update()
                time.sleep(0.1)
                self.move()
