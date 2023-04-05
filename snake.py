STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
MOVE_DISTANCE = 20
from turtle import Turtle


class Snake:
    def __init__(self):
        self.all_segment = []
        self.create_snake()
        self.head = self.all_segment[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.extend(position)

    def extend(self, position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.all_segment.append(segment)

    def add_segment(self):
        self.all_segment[-1].position()

    def move(self):
        for seg in range(len(self.all_segment)-1, 0, -1):
            new_x = self.all_segment[seg - 1].xcor()
            new_y = self.all_segment[seg - 1].ycor()
            self.all_segment[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
