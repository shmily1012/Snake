# Snake Game Version 1.1
# Author : Alex
# Time : 12/27/2019
import numpy as np
import os
from matplotlib import pyplot as plt
from snake import snake
from nut import nut
import json
from methods import method

if __name__ == "__main__":
    cycle = 0
    while True:
        print(os.path.abspath)
        with open("config.json") as json_file:
            data = json.load(json_file)
            WindowWidth = data["Width"]
            WindowLength = data['Length']
            TimesPerSecond = data['TimesPerSecond']
        s = snake()
        n = nut(s)

        plt.ion()
        plt.connect('key_press_event', snake.on_click)
        while True:
            m = method(s, WindowWidth, WindowLength, n.x, n.y)
            s.direction = m.decide()
            print("snake.steps=",s.steps)
            if s.direction == 1:
                status = s.Left()
            elif s.direction == 2:
                status = s.Right()
            elif s.direction == 3:
                status = s.Up()
            elif s.direction == 4:
                status = s.Down()
            else:
                print("Give Up!")
                status = False
            if status == False:
                plt.axis([0, WindowWidth, 0, WindowLength])
                plt.plot(s.bodyX, s.bodyY, 'ro')
                plt.plot(s.headX, s.headY, 'yo')
                plt.plot(n.x, n.y, 'go')
                plt.draw()
                plt.pause(5)  # When failure happens pause 5 sec
                plt.clf()
                break
            if s.headX[0] == n.x and s.headY[0] == n.y:
                s.eat()
                n = nut(s)
            plt.axis([0, WindowWidth, 0, WindowLength])
            plt.plot(s.bodyX, s.bodyY, 'ro')
            plt.plot(s.headX, s.headY, 'yo')
            plt.plot(n.x, n.y, 'go')
            plt.draw()
            plt.pause(1/TimesPerSecond)
            plt.clf()
        print("Done.")
        cycle+=1
        dataInput = {}
        dataInput['Length'] = s.length
        dataInput['Xfact'] = m.Xfact
        dataInput['Yfact'] = m.Yfact
        if dataInput['Length'] > 10:
            with open('Data\\cycle-%d.json'%cycle, 'w') as outfile:
                json.dump(dataInput, outfile)
