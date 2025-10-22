import os
import time
import keyboard
import random

WORLD_SIZE = 10
UPDATE_TIME = 0.5
DIRECTIONS = {
        "w": (0, -1),
        "a": (-1, 0),
        "s": (0, 1),
        "d": (1, 0),
        }


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


class Snake:
    def __init__(self):
        self.input = (1,0)
        self.dir = (1,0)
        self.snake = [(5,4),(4,4),(3,4)]
        self.points = 0
        self.food = self.snake[0]
        self.is_active = True
        self.last_update_time = time.time()

        self.place_food()


    def place_food(self):
        while self.food in self.snake:
            self.food = (random.randrange(0,WORLD_SIZE),random.randrange(0,WORLD_SIZE))    


    def consume_food(self):
        self.snake.append(self.food)
        self.place_food()
        self.points += 1


    def process_input(self):
        for key, direction in DIRECTIONS.items():
            if keyboard.is_pressed(key) and self.dir != tuple(-x for x in direction):
                self.input = direction
                break


    def snake_gameloop(self):
        self.process_input()
        if (time.time() - self.last_update_time < UPDATE_TIME):
            pass
        else:
            self.last_update_time = time.time()
            self.update_snake()
            if self.snake[0] in self.snake[1:]:
                self.reset_snake()
            if self.snake[0] == self.food:
                self.consume_food()
            self.draw_snake()


    def update_snake(self):
        self.dir = self.input
        x = (self.snake[0][0] + self.dir[0]) % WORLD_SIZE
        y = (self.snake[0][1] + self.dir[1]) % WORLD_SIZE
        next_snake = [(x, y)]
        for i in range(1, len(self.snake)):
            next_snake.append(self.snake[i-1])
        self.snake = next_snake

     
    def draw_snake(self):
        out = "Points: " + str(self.points) + "\n"
        for y in range(WORLD_SIZE):
            out += "\n"
            for x in range(WORLD_SIZE):
                if (x,y) not in self.snake:
                    if self.food == (x,y):
                        out += " @ "
                    else:
                        out += "   "
                else:
                    if (x,y) == self.snake[0]:
                        out += " O "
                    else:
                        out += " # "      
        cls()         
        print(out)
    

    def reset_snake(self):
        self.input = (1,0)
        self.snake = [(5,4),(4,4),(3,4)]
        self.points = 0


def main():
    snake = Snake()
    while snake.is_active:
        snake.snake_gameloop()

        
if __name__ == "__main__":
    main()