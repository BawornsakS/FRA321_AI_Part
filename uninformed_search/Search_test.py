from Node import Node
from Graph import Graph
from Search import *
from SquareGrid import *
from implementation import *
a = Node("A" , 5, 5)
b = Node("B")

#create dictionary of graph A
graphA = Graph()
graphA.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}



g = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS # long list, [(21, 0), (21, 2), ...]
#draw_grid(g)

#test cases for graph A
#s = Search.breadth_first_search(graphA,'A','E')
#d = Search.depth_first_search(graphA, 'A', 'E')
#Search.print_path(s,'A','E')
#Search.print_path(d,'A','E')


cost_so_far = Search.a_star_search(diagram, (1, 4), (7, 8))
print()
draw_grid(diagram, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8))

