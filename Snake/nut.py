from numpy import random
import json
from logging import log
from snake import snake


class nut:
    def __init__(self, snake):
        with open("config.json") as json_file:
            data = json.load(json_file)
            # print(data)
        occupy = True
        while(occupy):
            occupy = False
            self.x = random.randint(0, data['Width'])
            self.y = random.randint(0, data['Length'])
            if self.x == snake.headX[0] and self.y == snake.headY[0]:
                print("Nut is in Head(%d,%d)" % (self.x, self.y))
                occupy = True
                continue
            for i in range(snake.length):
                if self.x == snake.bodyX[i] and self.y == snake.bodyY[i]:
                    print("Nut is in Body(%d,%d)" % (self.x, self.y))
                    occupy = True
                    break
        print("Nut is in (", self.x, self.y,")")


if __name__ == "__main__":
    s = snake()
    for i in range(10000):
        n = nut(s)
