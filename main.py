from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Zaki442 Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    
    snake.wall_wdistense()
        # if snake.segments[i].xcor() < -280 :
        #     snake.segments[i].xcor(snake.segments[i].xcor() + 560)

        # if snake.segments[i].ycor() > 280 :
        #     snake.segments[i].ycor(snake.segments[i].ycor() - 560) 
        # if snake.segments[i].ycor() < -280 :
        #     snake.segments[i].ycor(snake.segments[i].ycor() + 560) 

    

    #Detect collision with wall.
    # if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
    #     game_is_on = False
    #     scoreboard.game_over()


    #Detect collision with Food.
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with tail.
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 9:
            game_is_on = False
            scoreboard.game_over()









screen.exitonclick()