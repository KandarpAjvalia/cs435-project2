from main import Main


class GraphSearch:

    @staticmethod
    def DFSRec(graph, start, end, path=None, visited=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        path.append(start)
        visited.add(start)
        if start == end:
            return True
        for node in graph.nodes[start]:
            if node not in visited:
                found = GraphSearch.DFSRec(graph, node, end, path, visited)
                if found:
                    return path
        return None

    @staticmethod
    def DFSIter(graph, start, end):
        stackSim = []
        visited = set()
        path = [start]
        for node in graph.nodes[start]:
            if node not in visited:
                visited.add(node)
                stackSim.append(node)
                while stackSim:
                    curr = stackSim.pop()
                    path.append(curr)
                    if curr == end:
                        return path
                    for nestedNode in graph.nodes[curr]:
                        if nestedNode not in visited:
                            visited.add(nestedNode)
                            stackSim.append(nestedNode)

        return None

    @staticmethod
    def BFTRec(graph):

        path = []
        queue = []
        visited = set()
        GraphSearch.BFTRecHelper(graph, path, queue, visited)
        for node in graph.nodes:
            if node not in visited:
                visited.add(node)
                queue.append(node)
                GraphSearch.BFTRecHelper(graph, path, queue, visited)
        return path

    @staticmethod
    def BFTRecHelper(graph, path, queue, visited):
        if not queue:
            return
        curr = queue.pop(0)
        path.append(curr)
        for node in graph.nodes[curr]:
            if node not in visited:
                visited.add(node)
                queue.append(node)
        GraphSearch.BFTRecHelper(graph, path, queue, visited)

    @staticmethod
    def BFSIter():
        pass


# graph = Main.createLinkedList(10)
graph = Main.createRandomUnweightedGraph(10)

print('\nGraph representation:--------------------')
print(graph)

print('3 d -------------------- DFS Recursive on above graph')
print(GraphSearch.DFSRec(graph, 3, 0))
print()
print('3 e -------------------- DFS Iterative on above graph')
print(GraphSearch.DFSIter(graph, 3, 0))
print()
print('3 f -------------------- BFT Recursive on above graph')
print(GraphSearch.BFTRec(graph))
print('\n')
