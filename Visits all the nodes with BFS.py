graph={
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}


def bfs_connected_component(graph, start):
    """Visits all the nodes of a search space (connected component) using BFS

        Args:
            graph (dict): Search space represented by a graph
            start (str): Starting state

        Returns:
            explored (list): List of the explored nodes
        """
    #List to keep track all visited nodes:
    explored = []

    #Keep track for nodes to be checked:
    queue = [start] #start: it`s a initial node, from parameter

    #keep looping until all nodes are checked
    while queue:

        #Pop first node from queue:
        node = queue.pop(0)

        if node not in explored:
            explored.append(node)

            #get neighbours if node is present, otherwise default is empty
            neighbours = graph.get(node, [])

            #add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)

    return explored


Reuslt = bfs_connected_component(graph, 'B')
print(Reuslt)

"""
You are welcome to python AI club, don`t miss your gift.
Ali Qadomy, CEO of BUS-UNI 

"""