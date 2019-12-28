
import random


class method:
    def __init__(self, snake,
                 wallx, wally,
                 nutx, nuty):
        self.snake = snake
        self.headx = snake.headX[0]
        self.heady = snake.headY[0]
        self.bodyx = snake.bodyX
        self.bodyy = snake.bodyY
        self.wallx = wallx
        self.wally = wally
        self.nutx = nutx
        self.nuty = nuty

        self.score = 0  # score

        self.Xfact = random.randint(10, 100)
        self.Yfact = random.randint(1, 10000)

    def getSorce(self, x, y):
        score = 0

        SqDistance2TopWall = (y - self.wally)**2
        SqDistance2BottonWall = y ** 2
        SqDistance2LeftWall = x ** 2
        SqDistance2RightWall = (x - self.wallx)**2
        if SqDistance2TopWall * SqDistance2BottonWall * SqDistance2LeftWall * SqDistance2RightWall == 0:
            return 0
        sum = SqDistance2TopWall + SqDistance2BottonWall + \
            SqDistance2LeftWall+SqDistance2RightWall
        for i in range(self.snake.length):
            if self.bodyx[i] == x and self.bodyy[i] == y:
                return 0
            sum += ((self.bodyx[i] - x) ** 2 + (self.bodyy[i]-y)**2)
        SqDistance2Nut = (self.nutx - x) ** 2 + (self.nuty-y)**2
        if SqDistance2Nut == 0:
            SqDistance2Nut = 0.1
        print('sum =', sum, 'SqDistance2Nut=', SqDistance2Nut)
        score = sum*self.Xfact + self.wallx*self.wally * \
            self.Yfact/SqDistance2Nut*(200/self.snake.steps)
        return score

    def goUp(self):
        headx = self.headx
        heady = self.heady+1
        return self.getSorce(headx, heady)

    def goDown(self):
        headx = self.headx
        heady = self.heady-1
        return self.getSorce(headx, heady)

    def goLeft(self):
        headx = self.headx-1
        heady = self.heady
        return self.getSorce(headx, heady)

    def goRight(self):
        headx = self.headx+1
        heady = self.heady
        return self.getSorce(headx, heady)

    def decide(self):
        Up = self.goUp()
        Down = self.goDown()
        Left = self.goLeft()
        Right = self.goRight()
        print(Up, Down, Left, Right)
        if Up == max([Up, Down, Left, Right]):
            return 3
        elif Down == max([Up, Down, Left, Right]):
            return 4
        elif Left == max([Up, Down, Left, Right]):
            return 1
        elif Right == max([Up, Down, Left, Right]):
            return 2
