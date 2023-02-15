def convert_maze(txt_maze):
   """Converte o arquivo de texto em matriz de caracteres"""
   mat_maze = []
   for line in txt_maze:
        mat_maze.append([i for i in line if i != '\n'])
   return mat_maze

def print_maze(maze):
   """Imprime a matriz de caracteres no formato de labirinto"""
   print
   for line in maze:
       print(''.join(line))


