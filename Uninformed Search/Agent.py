import random

class Agent:

    name = ""
    pos_x = 0
    pos_y = 0
    world = None

    def __init__(self,name = "Alice", world = None, x=0, y=0):

        self.name = name
        self.world = world
        self.pos_x = x
        self.pos_y = y
        world.add(self)


    def walk(self, world):

        world.agent_list[self.name] = None
        self.pos_x += random.randint(-1,1)
        self.pos_y += random.randint(-1, 1)

        if self.pos_x< 0:
            self.pos_x = int(world.width)
        elif self.pos_x > world.width:
            self.pos_x = 0


        if self.pos_y< 0:
            self.pos_y = int(world.height)
        elif self.pos_y > world.height:
            self.pos_y = 0

        world.agent_list[self.name] = [self.pos_x, self.pos_y]


