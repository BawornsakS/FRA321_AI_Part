from World import World
from Agent import Agent
import pygame
import math
#---------------------------------- Philosophy --------------------------------------------
'''
The supreme cost function: as a race, survive as long as possible



Actions available: eat, breed, (more to come)
--- each action impacts life span
--- hidden actions: Agents don't know the action until it performs by itself


'''
#---------------------------------- Set up screen -----------------------------------------

print ("Setting up screen")
width = 400
height = 400
cell_size = 10
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

running  = 1

for i in range(1, math.floor(width / cell_size) + 1):
    pygame.draw.line(screen, (0, 0, 0), (i * cell_size, 0), (i * cell_size, height))
    pygame.display.flip()

for i in range(1, math.floor(height / cell_size) + 1):
    pygame.draw.line(screen, (0, 0, 0), (0, i * cell_size), (width, i * cell_size))
    pygame.display.flip()


#---------------------------------- Set up World ------------------------------------------
print ("Conjuring the Matrix")

w = World(width, height,cell_size)
a = Agent("Blink",w,3,3)

#---------------------------------- Simulation --------------------------------------------

print ("Activating the Matrix")
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    w.draw_agent(screen,pygame.Color(255,255,255))
    a.walk(w)
    w.draw_agent(screen)
    pygame.time.delay(50)