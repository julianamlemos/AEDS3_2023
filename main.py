import time
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



tempo_final = (time.time()) 
print("Tempo: " , tempo_final - tempo_inicial)

file.close
