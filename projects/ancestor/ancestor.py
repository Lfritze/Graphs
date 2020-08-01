
import collections

# traversing from the child up to the earliest ancestor

def earliest_ancestor(ancestors, starting_node):
    # make a graph from the input data, to get the parent nodes
    # make a dictionary of parents - because they have children, 
    parentNodes = {}
    # loop through ancestors with parent and child - if in parentNodes:
        ## append the parent in ancestors
        ## else child = parent
    for parent, child in ancestors:
        if child in parentNodes:
            parentNodes[child].append(parent)
        else:
            parentNodes[child] = [parent]

    # if starting node lacks parents
    if starting_node not in parentNodes:
        return -1

    # find longest path with BFT and return the last path in the queue 
    # deque() list-like container with fast appends and pops on either end
    path_queue = collections.deque() 

    # save the last path dequeued
    last_path = [starting_node] 

    path_queue.append(last_path)

    while len(path_queue) > 0:
        # popleft() removes an element from the left side of the deque and returns the value
        last_path = path_queue.popleft()
        oldest_ancestor = last_path[-1]

        if oldest_ancestor in parentNodes:
            # lowest id goes in queue last
            parentNodes[oldest_ancestor].sort(reverse=True) 
            for parent in parentNodes[oldest_ancestor]:
                new_path = last_path.copy()
                new_path.append(parent)

                path_queue.append(new_path)

    return last_path[-1]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print((earliest_ancestor(test_ancestors, 1), 10))
print((earliest_ancestor(test_ancestors, 11), -1))
print((earliest_ancestor(test_ancestors, 7), 8))



