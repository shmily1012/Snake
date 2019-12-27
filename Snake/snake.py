import numpy as np
import json


class snake:
    def __init__(self):
        with open("config.json") as json_file:
            data = json.load(json_file)
            self.WidnowWidth = data["Width"]
            self.WindowsLength = data['Length']
        self.length = 3
        self.bodyX = [1, 2, 3]
        self.bodyY = [1, 1, 1]
        self.footprintX = self.bodyX[0]
        self.footprintY = self.bodyY[0]
        self.headX = [4]
        self.headY = [1]
        self.direction = 2    # 1: Left 2: Right 3: Up 4: Down

    def follow(self):
        self.footprintX = self.bodyX[0]
        self.footprintY = self.bodyY[0]
        self.bodyX = self.bodyX[1:]
        self.bodyY = self.bodyY[1:]
        self.bodyX.append(self.headX[0])
        self.bodyY.append(self.headY[0])
        # print("self.bodyX=",self.bodyX)
        # print("self.bodyY=",self.bodyY)

    def eat(self):
        self.bodyX.insert(0, self.footprintX)
        self.bodyY.insert(0, self.footprintY)
        self.length += 1

    def Left(self):
        self.follow()
        self.headX[0] -= 1
        if self.headX[0] == 0:
            print("Hit the windows.")
            return False
        elif self.headX[0] in self.bodyX:
            print("Hit the body.")
            return False
        return True

    def Right(self):
        self.follow()
        # self.bodyX += 1
        self.headX[0] += 1
        if self.headX[0] == self.WidnowWidth:
            print("Hit the windows.")
            return False
        elif self.headX[0] in self.bodyX:
            print("Hit the body.")
            return False
        return True

    def Up(self):
        self.follow()
        # self.bodyY += 1
        self.headY[0] += 1
        if self.headY[0] == self.WindowsLength:
            print("Hit the windows.")
            return False
        elif self.headY[0] in self.bodyY:
            print("Hit the body.")
            return False
        return True

    def Down(self):
        self.follow()
        # self.bodyY -= 1
        self.headY[0] -= 1
        if self.headY[0] == 0:
            print("Hit the windows.")
            return False
        elif self.headY[0] in self.bodyY:
            print("Hit the body.")
            return False
        return True

    def on_click(self, event):
        print('you pressed', event.key)
        if event.key == 'up':
            if self.direction != 4:
                self.direction = 3
        elif event.key == 'down':
            if self.direction != 3:
                self.direction = 4
        elif event.key == 'left':
            if self.direction != 2:
                self.direction = 1
        elif event.key == 'right':
            if self.direction != 1:
                self.direction = 2


if __name__ == "__main__":
    s = snake()
    s.Right()
    print(s.bodyX)
