from typing import List
from node import Node

class Graph:
    def __init__(self, nodes: List[Node], adj_list: List[List[Node]]= []) -> None:
        self.nodes = nodes
        self.adj_list = adj_list
        if adj_list == []:
            for _ in range(len(self.nodes)):
                self.adj_list.append([])
        for no in self.nodes:
            noX, noY = no.pos
        if no.tipo != '#':
            for neighbor in self.nodes:
                neighborX, neighborY = neighbor.pos
                if noX - 1 == neighborX and noY == neighborY and neighbor.tipo != '#':
                    no.vizinhos.append(neighbor)
                if noX + 1 == neighborX and noY == neighborY and neighbor.tipo != '#':
                    no.vizinhos.append(neighbor)
                if noX == neighborX and noY - 1 == neighborY and neighbor.tipo != '#':
                    no.vizinhos.append(neighbor)
                if noX == neighborX and noY + 1 == neighborY and neighbor.tipo != '#':
                    no.vizinhos.append(neighbor)
  
def convert_maze_in_graph(mat):
    nodes = []
    for j in range(len(mat)):
        for i in range(len(mat[0])):
            nodeAux = Node()
            nodeAux.pos = j,i
            nodeAux.tipo = mat[j][i]
            nodes.append(nodeAux)
    return nodes
