class Node:
    tipo: str
    vizinhos = []
    pos: int
    desc = 0

    def __init__(self):
        self.tipo = None
        self.vizinhos = []
        self.desc = 0