class Agent:

    pos_x = 0
    pos_y = 0
    world = None

    def __init__(self, world = None, x=0, y=0):

        self.world = world
        self.pos_x = x
        self.pos_y = y
        #world.add(self)


    def neighbor(self):

        neighbors = []

        if self.pos_x - 1 != -1:
            neighbors.append((self.pos_x - 1,self.pos_y))

        if self.pos_x != self.world.width:
            neighbors.append((self.pos_x + 1,self.pos_y))

        if self.pos_y - 1 != -1:
            neighbors.append((self.pos_x, self.pos_y - 1))

        if self.pos_y != self.world.width:
            neighbors.append((self.pos_x, self.pos_y + 1))

        return neighbors



    def walk(self, pos):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
