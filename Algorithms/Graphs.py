from collections import deque

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

def depth_first_search(graph,root):
    visited_vertices = list()
    graph_stack = list()
    graph_stack.append(root)
    node = root
    
    while len(graph_stack) > 0:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes = graph[node]
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                node = graph_stack[-1]
            continue
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        
        first_adj_node = sorted(remaining_elements)[0]
        graph_stack.append(first_adj_node)
        node = first_adj_node
    return visited_vertices


graph = dict()
graph['A'] = ['B', 'S'] 
graph['B'] = ['A']
graph['S'] = ['A','G','C']
graph['D'] = ['C'] 
graph['G'] = ['S','F','H'] 
graph['H'] = ['G','E'] 
graph['E'] = ['C','H'] 
graph['F'] = ['C','G'] 
graph['C'] = ['D','S','E','F']

# print(depth_first_search(graph, 'A'))