from typing import List
from node import Node

class Graph:
    def __init__(self, nodes: List[Node], adj_list: List[List[Node]]= []) -> None:
        self.nodes = nodes
        self.adj_list = adj_list
        if adj_list == []:
            for _ in range(len(self.nodes)):
                self.adj_list.append([])
        for i in range(len(self.nodes)):
                for j in range(len(self.nodes)):
                    if self.nodes[j] in self.nodes[i].vizinhos:
                        self.adj_list[i].append(self.nodes[j])
                    else:
                        self.adj_list[i].append([])

    def dfs(self, entrada: Node, saida: Node):
        """Busca em profundidade para achar o saída do labirinto"""
        S = [entrada]
        entrada.desc = 1
        while len(S) != 0:
            u = S[-1] 
            v = self.dfs_aux(u)
            if v != None:
                S.append(v)
                v.desc = 1
                if v == saida:
                    return S
            else:
                S.pop(-1)

    def dfs_aux(self, r: Node):
        for v in r.vizinhos:
            if v.desc == 0:
                return v
        return None

    def no_entrada(self):
        """Retorna o nó de entrada do labirinto"""
        entrada: Node
        for i in range(len(self.nodes)):
            if self.nodes[i].tipo == 'S':
                entrada = self.nodes[i]
        return entrada
    
    def no_saida(self):
        """Retorna o nó de saída do labirinto"""
        saida: Node
        for i in range(len(self.nodes)):
            if self.nodes[i].tipo == 'E':
                saida = self.nodes[i]
        return saida

  
def convert_maze_in_graph(mat):
    """Converte a matriz de caracteres em grafo (nós)"""
    nodes = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            nodeAux = Node()
            nodeAux.pos = i,j
            nodeAux.tipo = mat[i][j]
            nodes.append(nodeAux)
        for no in nodes:
            noX, noY = no.pos
            if no.tipo != '#':
                for neighbor in nodes:
                    neighborX, neighborY = neighbor.pos
                    if noX - 1 == neighborX and noY == neighborY and neighbor.tipo != '#':
                        no.vizinhos.append(neighbor)
                    elif noX + 1 == neighborX and noY == neighborY and neighbor.tipo != '#':
                        no.vizinhos.append(neighbor)
                    elif noX == neighborX and noY - 1 == neighborY and neighbor.tipo != '#':
                        no.vizinhos.append(neighbor)
                    elif noX == neighborX and noY + 1 == neighborY and neighbor.tipo != '#':
                        no.vizinhos.append(neighbor)
    return nodes

def print_pos(nodes: List[Node]):
   """Imprime a posição dos nós de um lista de nós"""
   for i in range(len(nodes)):
      print(nodes[i].pos)
