import time
from node import Node
from maze import* 
from graph import*


print("Informe o arquivo: (0 para sair): " )
nameFile = input()

tempo_inicial = (time.time())

if nameFile == "0":
    print("\nEncerrando...")
else:
    print("\nProcessando...") 
    file = open(nameFile, "r")
    mat_maze = convert_maze(file)
    nodes: Node = convert_maze_in_graph(mat_maze)
    #print(mat_maze) #descomentar para imprimir matriz de caracteres
    #print_maze(mat_maze) # descomentar para imprimir labirinto
    g1 = Graph(nodes)
    entrada = g1.no_entrada()
    caminho = g1.dfs(entrada=entrada)

    print("Caminho: ", end="")
    print_pos(caminho)

    file.close

tempo_final = (time.time()) 
print("\nTempo: " , tempo_final - tempo_inicial)