from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time

# CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVE_DISTANCE = 20
STARTING_Y_POSITION = -280
FINISH_Y_POSITION = 280

# game loop

# screen setup
my_screen = Screen()
my_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
my_screen.tracer(0)
my_screen.title("Turtle Crossing Game")

# create player and car manager
my_player = Player(STARTING_Y_POSITION)
my_car_manager = CarManager()
my_scoreboard = ScoreBoard()
my_screen.update()

# key listner
my_screen.listen()
my_screen.onkey(my_player.move_up, "Up")
my_screen.onkey(my_player.move_down, "Down")
my_screen.onkey(my_player.move_right, "Right")
my_screen.onkey(my_player.move_left, "Left")

# game loop
while not my_player.detect_collision(my_car_manager.cars):
    my_car_manager.add_car()
    my_car_manager.move_cars()
    if my_player.completed_level():
        my_scoreboard.update_score()
        my_player.reset_position(STARTING_Y_POSITION)
        my_car_manager.reset_cars()
    time.sleep(my_scoreboard.speed)
    my_screen.update()

my_scoreboard.game_over()
my_screen.update()
time.sleep(1.5)