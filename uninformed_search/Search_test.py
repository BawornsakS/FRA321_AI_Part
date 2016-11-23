from Search import *
from Graph import *
from Problem import *

romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)

search = breadth_first_search(romania_problem)

search2 = astar_search(romania_problem)



print (search.solution())
print (search2.solution())
