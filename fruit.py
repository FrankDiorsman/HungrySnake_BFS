import random

import numpy as np



class Fruit:
    def __init__(self, config):
        self.config = config
        self.width = int(int(config['window-width']) / int(config['block-size']))
        self.height = int(int(config['window-height']) / int(config['block-size']))
        self.list_generate = []
        self.shortestfruit = None
        self.Number =2

    def generate(self):
        while(len(self.list_generate) != self.config['fruit-number']):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.list_generate.append((x,y))
            if(len(self.list_generate) == self.config['fruit-number']):
                break;
        print("list_generateeeeeeeeeeeeeee")
        print(self.list_generate)
        return self.list_generate

    # def generate(self):
    #     x = random.randint(0, self.width - 1)
    #     y = random.randint(0, self.height - 1)
    #     self.last_generate = (x,y)
    #     return (x,y)

    def remove_fruit(self,pos):
        if(len(self.list_generate)>0):
            for i in range(len(self.list_generate)):
                if(self.list_generate[i-1][0] == pos[0]):
                    if(self.list_generate[i-1][1] == pos[1]):
                        self.list_generate.remove(self.list_generate[i-1])
                        print(self.list_generate)
                        print("------------")
        