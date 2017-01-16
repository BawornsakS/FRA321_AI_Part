from Node import Node
from Graph import Graph
from Search import *
from SquareGrid import *
from implementation import *

#Examples of how you can create a node. You may or may not use this.
a = Node("A" , 5, 5)
b = Node("B")

#Create a map called graphA. The data structured used here is a dictionary.
graphA = Graph()
graphA.edges = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['A'],
    'D': ['E'],
    'E': ['B']
}

###This section is for Lab 1

###test cases for graph A
s = Search.breadth_first_search(graphA,'A','E')
#d = Search.depth_first_search(graphA, 'A', 'E')
Search.print_path(s,'A','E')
#Search.print_path(d,'A','E')



###This section is for Lab 2.

###How to set up a Square Grid
#g = SquareGrid(30, 15)
#g.walls = DIAGRAM1_WALLS # long list, [(21, 0), (21, 2), ...]
#draw_grid(g)

### A* Algorithm
#cost_so_far = Search.a_star_search(diagram, (1, 4), (7, 8))
#draw_grid(diagram, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8))

