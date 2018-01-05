import pygame
import math



class World:
    agent_list = {}
    width = 0
    height = 0
    cell_size = 0


    def __init__(self, width, height,cell_size):

        self.width = width/cell_size -1
        self.height = height/cell_size -1
        self.cell_size = cell_size


    def add(self, agent):
        x = agent.pos_x
        y = agent.pos_y

        self.agent_list[agent.name] = [x,y]

    def draw_agent(self, screen, color = pygame.Color(0,255,0)):
        i = 0
        for a,p in self.agent_list.items():
            print("Agent " + str(a) , end = "   ")
            print("[" + str(p[0]) + "," + str(p[1]) + "]")
            pygame.draw.rect(screen,color, (p[0]*self.cell_size +1, p[1]*self.cell_size +1, self.cell_size -1, self.cell_size -1))
            pygame.display.flip()


