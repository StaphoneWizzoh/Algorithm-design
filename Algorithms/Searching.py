from collections import deque
import random


# unordered linear search

def unordered_linear(unordered_list, item):
    list_size = len(unordered_list)
    for i in range(list_size):
        if item == unordered_list[i]:
            return i
    return None


# Ordered linear search

def ordered_linear(ordered_list, item):
    list_size = len(ordered_list)
    for i in range(list_size):
        if item == ordered_list[i]:
            return i
        elif ordered_list[i] > item:
            return None
    return None

# Binary search
def binary(ordered_list,item):
    list_size = len(ordered_list) - 1
    index_of_first_element = 0
    index_of_last_element = list_size
    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element) // 2
        if ordered_list[mid_point] == item:
            return mid_point
        if item > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1
            
    if index_of_first_element > index_of_last_element:
        return None

# BFS
def breadth_first_search(graph, root):
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root
    
    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adj_nodes = graph[node]
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)
                
    return visited_vertices  
    

        
test_list = []
for i in range(100):
    test_list.append(i)
    
search_item = random.randint(0, 99)

print(f" search item is {search_item} and result is {binary(test_list,search_item)}")