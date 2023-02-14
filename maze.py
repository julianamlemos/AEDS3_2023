from node import*
from typing import List

def convert_maze(txt_maze):
   list_maze = []
   for line in txt_maze:
        list_maze.append([i for i in line if i != '\n'])
   return list_maze

def print_maze(maze):
   print
   for line in maze:
       print(''.join(line))

def print_nodes_pos(nodes: List[Node]):
   for i in range(len(nodes)):
      print(nodes[i].pos)
