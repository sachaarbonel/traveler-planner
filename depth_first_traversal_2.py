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
                	if len(newpath) == len(graph):
                		paths.append(newpath)
        return paths