import pygame
import random

class World:
    agent_list = {}
    width = 0
    height = 0
    cell_size = 0


    def __init__(self, width, height,cell_size):

        self.width = width/cell_size -1
        self.height = height/cell_size -1
        self.cell_size = cell_size


    def draw_rec(self, screen, pos, color = pygame.Color(0,255,0)):
        pygame.draw.rect(screen,color, (pos[0]*self.cell_size +1, pos[1]*self.cell_size +1, self.cell_size -1, self.cell_size -1))
        pygame.display.flip()

    def random_wall(self, num):
        walls = []
        for i in range(int(num/100 * (self.width*self.height))):
            x = int(random.random()*self.width)
            y = int(random.random()*self.height)
            if x != 0 and y != 0:
                walls.append((x,y))
        return walls