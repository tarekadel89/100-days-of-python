import time
import turtle
from snake import Snake
from food import Food
from score import Score

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

my_snake = Snake()  
my_food = Food()
my_score = Score()

def main():
    # initialize
    my_snake.reset()
    my_food.move()
    my_score.reset_score()
    
    # Keyboard bindings
    screen.listen()
    screen.onkey(my_snake.go_up, "Up")
    screen.onkey(my_snake.go_down, "Down")
    screen.onkey(my_snake.go_left, "Left")
    screen.onkey(my_snake.go_right, "Right")
   
    # Main game loop 
    game_on = True
    while game_on: 
        if(my_snake.detect_collision_food(my_food)):
            my_food.move()
            my_score.update_score()
        my_snake.move()    
        if(my_snake.detect_collision_wall() or my_snake.detect_collision_self()):
            game_on = False
            time.sleep(1)
            my_snake.hide_snake()
            my_food.hide_food()
        screen.update()
        time.sleep(my_snake.speed)
    my_score.game_over()
    screen.update()
    time.sleep(1)
    my_score.hide_score()
    screen.update()

another_game = "y"
while another_game == "y":
    main()
    another_game = screen.textinput("Another game", "Would you like another game (y/n): ").lower()
    
