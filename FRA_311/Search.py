import queue
from implementation import *

class Search:

    def breadth_first_search(graph, start,goal):
        frontier = queue.Queue()
        frontier.put(start)
        came_from = {}
        came_from[start] = None

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in graph.neighbors(current):
                if next not in came_from:
                    frontier.put(next)
                    came_from[next] = current

        return came_from


    def depth_first_search(graph,start,goal):

        came_from = []

        return came_from


    def print_path(dict, start, goal):

        list = []
        list.insert(0,goal)
        parent = dict.get(goal)

        while parent != None:
            list.insert(0,parent)
            parent = dict.get(parent)

        print(list)


    def heuristic(a, b):

        return 0



    def a_star_search(graph, start, goal):

        cost = []

        return cost


