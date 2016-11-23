from uninformed_search.Search import *
from uninformed_search.Graph import *
from uninformed_search.Problem import *

romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)

search = breadth_first_search(romania_problem)

search2 = astar_search(romania_problem)



print (search.solution())
print (search2.solution())
