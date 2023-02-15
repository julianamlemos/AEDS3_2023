import time
from node import*
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
    #print(mat_maze)
    #print_maze(mat_maze)
    g1 = Graph(nodes, adj_list=[])
    entrada = g1.no_entrada()
    saida = g1.no_saida()
    caminho = g1.dfs(entrada=entrada, saida=saida)
    print_pos(caminho)

    file.close

tempo_final = (time.time()) 
print("Tempo: " , tempo_final - tempo_inicial)
#maze\toy.txt