import turtle

INITIAL_LENGTH = 2
class Snake():
    def __init__(self):
        # Speed screen refreshes
        self.speed = 0
        # Snake body
        self.segments = []
        # Snake head
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("green")
        self.head.penup()

    def reset(self):
        self.segments.clear()
        self.speed = 0.1
        self.head.goto(0, 0)
        self.head.direction = "right"
        self.add_segments(INITIAL_LENGTH)
        self.segments[0].goto(self.head.xcor()-20, 0)
        self.segments[1].goto(self.head.xcor()-40, 0)
        #self.move()
        
    def add_segments(self, num_segments):
        for i in range(num_segments):
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            self.segments.append(new_segment)
    
    def move(self):
        headx = self.head.xcor()
        heady = self.head.ycor()

        if self.head.direction == "up":
            self.head.sety(heady + 20)
        elif self.head.direction == "down":
            self.head.sety(heady - 20)
        elif self.head.direction == "left":
            self.head.setx(headx - 20)
        elif self.head.direction == "right":
            self.head.setx(headx + 20)

        for i in range(len(self.segments)-1, -1, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)
        
        self.segments[0].goto(headx,heady)
        
    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"
    
    def detect_collision_food(self, food):
        if self.head.distance(food.x_coord, food.y_coord) < 17.5:
            self.speed -= self.speed * .05
            self.add_segments(1)
            return True
        else:
            return False
    
    def detect_collision_self(self):
        for segment in self.segments:
            if self.head.distance(segment.xcor(), segment.ycor()) < 17.5:
                return True
        return False
    def detect_collision_wall(self):
        if self.head.xcor() > 280 or self.head.xcor() < -300 or self.head.ycor() > 300 or self.head.ycor() < -280:
            return True
        else:
            return False
    
    def hide_snake(self):
        self.head.goto(1000, 1000)
        for segment in self.segments:
            segment.goto(1000, 1000)