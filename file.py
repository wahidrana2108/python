graph = [[None]] # for node 0, there is nothing


def graph_input():
    N, E = None, None
    # taking input n and e here
    l = input() # input function in python
    l = l.split(' ') # making a split based on spaces for a line
    N, E = int(l[0]), int(l[1]) # storing the N and E, after converting them to integer 
    # taking input the graph here
    # return N, E and graph
    return N, E, graph # will return number of nodes, number of edges and the adjacent list


def print_graph(N, graph):
    # print the graph in the form of adjacent matrix
    # if there is an edge between node U an V, print 1, else print 0
    for i in range(1, N+1, 1):
        graph[i].sort()  # sorting all the nodes 1: 3, 5, 4 -> 3, 4, 5
    for i in range(1, N+1, 1):
        # if you have a list something like 1: 2 4 6, where N=6
        # then for node 1, you need to print 0 1 0 1 0 1
        # printing 1 where there is an edge, printing 0 where there is no edge
        for j in range(0, len(list[i])): # to traverse the adjacent list of a particular node i
            """
            # write your logic here
            """
            pass
    return


if __name__ == "__main__":
    N, E, graph = graph_input()
    print_graph(N, graph)