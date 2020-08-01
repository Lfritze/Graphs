"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import collections

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """         
        # add a node
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # enqueue our start node
        q.enqueue(starting_vertex)
        # make a set to track visited nodes
        visited = set()
        # while queue still has things in it..
        while q.size() > 0:
            # dequeue from front of the line, this is our current node
            current_node = q.dequeue()
        # check if we visited, if not:
            if current_node not in visited:
                # mark it as visited
                visited.add(current_node)
                print(current_node)
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # iterate over neighbors,
                for neighbor in neighbors:
                # add to queue
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push our starting node onto the stack
        s.push(starting_vertex)
        # Make a set to track the nodes we've visited
        visited = set()
        # As long as stack isn't empty
        while s.size() > 0:
            ## pop off the top, this is our current node
            current_node = s.pop()
            ## Check if we have visited this node before and if not:
            if current_node not in visited:
                ### mark it as visited
                visited.add(current_node)
                print(current_node)
                ### get its neighbors
                neighbors = self.get_neighbors(current_node)
                ### iterate over neighbors
                for neighbor in neighbors:
                ### add them to our stack
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # if visited == None:
        #     visited= set()
        # #Check if weve been visited
        # if vertex not in visited:
        #     visited.add(vertex)
        # #need base case: if no neighbors
        #     neighbors = self.get_neighbors(vertex)
        # # progress toward base case
        #     if len(neighbors) == 0:
        #         return visited
        # #if we dod have neighbors, iterate over them and recurse for each one
        #     for neighbor in neighbors:
        #         self.dft_recursive(neighbor, visited)





        if visited is None:
            # make a set to track visited nodes
            visited = set()
        ### mark it as visited
        visited.add(starting_vertex)
        print(starting_vertex)

        for path in self.vertices[starting_vertex]:
            if path not in visited:
                self.dft_recursive(path, visited)




        # # make a set to track visited nodes
        # visited = set()

        # def dft(cur_node):
        #     if cur_node in visited:
        #         return
        #     else:
        #         visited.add(cur_node)
        #         print(cur_node)
        #     neighbors = self.get_neighbors(cur_node)
        #     for neighbor in neighbors:
        #         dft(neighbor)
        # dft(starting_vertex)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
         # make a queue
        q = Queue()
        # make a set to track visited
        visited = set()
        # enqueue a PATH TO the starting vertex
        path = [starting_vertex]
        q.enqueue(path)
        ## as long as our queue isn't empty
        while q.size() > 0:
        ### dequeue from the front of the line, this is our current path: []
            current_path = q.dequeue()
        ### current_node is the last thing in the current path
            current_node = current_path[-1]
        ### check if this is the target node
            if current_node == destination_vertex:
        #### if so return
                return current_path
        ### check if we've visited yet, if not:
            if current_node not in visited:
        #### mark as visited
                visited.add(current_node)
        #### get the current node's neighbors
                neighbors = self.get_neighbors(current_node)
        #### iterate over the neighbors
                for neighbor in neighbors:
        #### add the neighbor to the path
                    neighbor_path = current_path.copy()
                    neighbor_path.append(neighbor)
        #### enqueue the neighbor's path





        # make a set to track visited nodes
        visited = set()
        # make a queue
        q = Queue()
        # enqueue our start node
        q.enqueue([starting_vertex])

        # while queue still has things in it..
        while q.size() > 0:
            # dequeue from front of the line, this is our current node
            current_node = q.dequeue()
            last_in_line = current_node[-1]

            if last_in_line in visited:
                continue
            else:
                # mark it as visited
                visited.add(last_in_line)
                print(last_in_line)
                 ### get its neighbors
                neighbors = self.get_neighbors(last_in_line)
                ### iterate over neighbors
            for neighbor in neighbors:
                next_path = current_node.copy()
                next_path.append(neighbor)

                if neighbor == destination_vertex:
                    return next_path
                 # add to queue
                q.enqueue(next_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # make a stack
        s = Stack()
        # make a set to track visited nodes
        visited = set()
        # push our starting node onto the stack
        s.push([starting_vertex])
        # As long as stack isn't empty
        while s.size() > 0:
            ## pop off the top, this is our current node
            current_node = s.pop()
            last_one = current_node[-1]

            if last_one in visited:
                continue
            else:
                ### mark it as visited
                visited.add(last_one)
                print(last_one)
            ### get its neighbors
            neighbors = self.get_neighbors(last_one)
            ### iterate over neighbors
            for neighbor in neighbors:
                next_path = current_node.copy()
                next_path.append(neighbor)

                if neighbor == destination_vertex:
                    return next_path
                ### add them to our stack
                s.push(next_path)

            

        
       

    def dfs_recursive(self, vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
​
        This should be done using recursion.
        """
        ## mark our node as visited
        visited.add(vertex)
        ## check if it's our target node, if so return
        if vertex == destination_vertex:
            return path
        if len(path) == 0:
            path.append(vertex)
        ## iterate over neighbors
        neighbors = self.get_neighbors(vertex)
        ### check if visited
        for neighbor in neighbors:
            if neighbor not in visited: 
        #### if not, recurse with a path
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)
        ##### if this recursion returns a path,
                if result is not None:
            ###### return from here
                    return result


        # visited = set()

        # def dft(path):
        #     last_one = path[-1]

        #     if last_one in visited:
        #         return None
        #     else:
        #         ### mark it as visited
        #         visited.add(last_one)
        #         print(last_one)

        #     if last_one == destination_vertex:
        #         return path

        #      ### get its neighbors
        #     neighbors = self.get_neighbors(last_one)
        #     for neighbor in neighbors:
        #         next_path = path.copy()
        #         next_path.append(neighbor)

        #         found = dft(next_path)
        #         if found:
        #             return found

        #     return None

        # return dft([starting_vertex])

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
