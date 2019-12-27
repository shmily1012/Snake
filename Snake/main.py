# Snake Game Version 1.0 
# Author : Alex
# Time : 12/26/2019
import numpy as np
from matplotlib import pyplot as plt
from snake import snake
from nut import nut

WindowWidth = 100
WindowLength = 100

if __name__ == "__main__":
    # example = np.zeros((WindowWidth, WindowLength))
    # print(example)
    snake = snake()
    n = nut(snake)

    plt.ion()
    plt.connect('key_press_event',snake.on_click)
    while True:
        if snake.direction == 1:
            status = snake.Left()
        elif snake.direction == 2:
            status = snake.Right()
        elif snake.direction == 3:
            status = snake.Up()
        elif snake.direction == 4:
            status = snake.Down()
        else:
            status = False
        if status == False:
            break
        if snake.headX[0] == n.x and snake.headY[0] == n.y:
            snake.eat()
            n = nut(snake)
        plt.axis([0, WindowWidth, 0, WindowLength])
        plt.plot(snake.bodyX, snake.bodyY, 'ro')
        plt.plot(snake.headX, snake.headY, 'yo')
        plt.plot(n.x, n.y, 'go')
        plt.draw()
        plt.pause(0.01)
        plt.clf()
    print("Done.")
