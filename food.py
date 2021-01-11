from turtle import Turtle
import random

FOOD_COORD = [x for x in range(-260, 261, 10)]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        
        random_x = random.choice(FOOD_COORD)
        random_y = random.choice(FOOD_COORD)
        self.goto(random_x, random_y)