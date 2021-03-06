import random

from graph import Graph

class Main:
    @staticmethod
    def createRandomUnweightedGraph(n):
        graph = Graph()
        nums = list(range(n))
        for num in nums:
            graph.addNode(num)
        random.shuffle(nums)
        for node in graph.getAllNodes():
            numEdges = random.randint(0, n - 1) // random.randint(1, n//2)
            random.shuffle(nums)
            for num in nums[:numEdges]:
                if num != node:
                    graph.addUndirectedEdge(node, num)
        return graph

    @staticmethod
    def createLinkedList(n):
        linkedListGraph = Graph()
        nums = list(range(n))
        for num in nums:
            linkedListGraph.addNode(num)
        for i in range(0, len(nums) - 1):
            linkedListGraph.addUndirectedEdge(nums[i], nums[i + 1])
        return linkedListGraph

    @staticmethod
    def BFTRecLinkedList(graph):
        from graphSearch import GraphSearch
        return GraphSearch.BFTRec(graph)

    @staticmethod
    def BFTIterLinkedList(graph):
        from graphSearch import GraphSearch
        return GraphSearch.BFTIter(graph)


if __name__ == "__main__":
    m = Main
    print()
    print('3 b -------------------- Random Unweighted Graph')
    print(m.createRandomUnweightedGraph(10))
    print()
    print('3 c -------------------- Linked List Graph')
    print(m.createLinkedList(10))
    print()
