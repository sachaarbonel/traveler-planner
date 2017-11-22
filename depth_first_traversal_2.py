graph = {'MADRID': ['GRECE','LISBONNE'],
             'GRECE': ['LISBONNE'],
             'LISBONNE': ['GRECE','MADRID']}


key1=["MADRID","LISBONNE","GRECE"]


def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


def find_all_paths2(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
        	return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths2(graph, node, end, path)
                for newpath in newpaths:
                	#print("test",newpath)
                	if len(newpath) == len(graph):
                		paths.append(newpath)

        return paths



def cyclic(g):
    """Return True if the directed graph g has a cycle.
    g must be represented as a dictionary mapping vertices to
    iterables of neighbouring vertices. For example:

    >>> cyclic({1: (2,), 2: (3,), 3: (1,)})
    True
    >>> cyclic({1: (2,), 2: (3,), 3: (4,)})
    False

    """
    path = set()

    def visit(vertex):
        path.add(vertex)
        for neighbour in g.get(vertex, ()):
            if neighbour in path or visit(neighbour):
                return True
        path.remove(vertex)
        return False

    return any(visit(v) for v in g)






# print(find_all_paths2(graph,key1[0],key1[2]))
# print(find_all_paths2(graph,key1[0],key1[1]))
#print("LISBONNE" in graph["GRECE"])
#print(cyclic(graph))

# def find_all_paths3(graph, start, end, path=[]):
#         path = path + [start]
#         if start == end:
#             return [path]
#         if start not in graph:
#         	return []
#         paths = []
#         for node in graph[start]:
#             if node not in path:
#                 newpaths = find_all_paths2(graph, node, end, path)
#                 for newpath in newpaths:
#                 	if len(newpath) == len(graph):
#                 		paths.append(newpath)
#         return paths