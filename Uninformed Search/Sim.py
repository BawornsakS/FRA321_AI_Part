from Agent import Agent
from World import World
import pygame
import math

#---------------------------------- Set up screen -----------------------------------------

print ("Setting up screen")
width = 400
height = 400
cell_size = 40                                                  #Change this to change grid size
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

end = (5, 5)                                                        # Goal State

w = World(width, height,cell_size)
#wall_pos = [(0,5),(1,5),(2,5),(3,5),(4,5),(6,7)]
wall_pos = w.random_wall(40)                                        # Percentage of Walls in Grid

if end in wall_pos:
    wall_pos.remove(end)


#---------------------------------- Simulation --------------------------------------------

print ("Activating the Matrix")


#---------------------------------- Setting Up the World ----------------------------------


agent = Agent(w, 0, 0)                                              # State State
neighbors = agent.neighbor()
visited = [(0,0)]
current = (agent.pos_x,agent.pos_y)


#---------------------------------- Drawing Walls------------------------------------------

for wall in wall_pos:
    w.draw_rec(screen, wall, pygame.Color(0, 0, 0))
w.draw_rec(screen, end, pygame.Color(0, 255, 0))

#---------------------------------- Searching ---------------------------------------------

print(wall_pos)
for n in agent.neighbor():
    if n not in visited and n not in neighbors and n not in wall_pos:
        neighbors.append(n)



while(1):

    ################################## Pygame Stuff #######################################
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    w.draw_rec(screen, (agent.pos_x, agent.pos_y), pygame.Color(255, 0, 0))
    w.draw_rec(screen, current, pygame.Color(100, 100, 100))

    #######################################################################################

    ################################## Algorithm ##########################################

    if len(neighbors) != 0:

        current = neighbors.pop(0)
        visited.append(current)
        agent.walk(current)

        ################################## Pygame Stuff #######################################
        w.draw_rec(screen, current, pygame.Color(0, 255, 255))
        pygame.display.flip()
        #######################################################################################

        if current == end:
            break

        for n in agent.neighbor():
            if n not in visited and n not in neighbors and n not in wall_pos:
                neighbors.append(n)

                ################################## Pygame Stuff ###############################
                if n != end:
                    w.draw_rec(screen, n, pygame.Color(175, 175, 175))
                else:
                    w.draw_rec(screen, n, pygame.Color(0, 175, 0))
                ###############################################################################

        pygame.time.delay(200)
    
pygame.time.delay(5000)                                 #Delay after completion