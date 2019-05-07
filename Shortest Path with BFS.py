 graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

def bfs_shortest_path(graph, start, goal):
    """Finds shortest path between 2 nodes in search space using BFS

        Args:
            graph (dict): Search space represented by a graph
            start (str): Starting state
            goal (str): Goal state

        Returns:
            new_path (list): List of the states that bring you from the start to
                the goal state, in the quickest way possible
        """

    # keep track of explored nodes
    explored = []

    # keep track of all paths to be checked
    queue = [start]

    # return path if start = goal
    if start == goal:
        checked =  print("That was easy! start = goal")
        return checked


    # keep looping until all possible paths have been checked
    while queue:

        # pop the first path from queue
        path = queue.pop(0)

        # get the last node from the path
        node = path[-1]
        if node not in explored:


            # get neighbours if node is present, otherwise default to empty
            neighbours = graph.get(node, [])

            #go through all nodes and build a new path,
            # and push into queue

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # return the path if equal the goal, here return the shortest paths
                if neighbour == goal:
                    return print(new_path)


            # marked the node as explored
            explored.append(node)
            #print(explored)

    # in case if there is no path between the 2 nodes
    print("the start = {}".format(start))
    print("the goal = {}".format(goal))
    return print("Sorry!! there is not pathes exist between theses two nodes")





bfs_shortest_path(graph, 'E', 'B')










