"""
Node class for A* Algorithm

Authors:
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import a_star_algo

# 3D array with (x,y,theta) as index
visited_nodes = np.zeros((600,400,12))
    
class Node():
  # Constructor for Node class
  def __init__(self, start_node, parent_node, index, clearance):
    self.current_node = start_node
    self.parent_node = parent_node
    self.index = index
    self.clearance = clearance
    
  # Defining action set and graph generation
  def move1(self,node):
    angle = (node[2] + 60)%360
    new_node = [node[0] + 0.5*math.cos(math.radians(angle)), node[1] + 0.5*math.sin(math.radians(angle)), angle]
    return new_node
    
  def move2(self,node):
    angle = (node[2] + 30)%360
    new_node = [node[0] + 0.5*math.cos(math.radians(angle)), node[1] + 0.5*math.sin(math.radians(angle)), angle]
    return new_node
    
  def move3(self,node):
    angle = (node[2] + 0)%360
    new_node = [node[0] + 0.5*math.cos(math.radians(angle)), node[1] + 0.5*math.sin(math.radians(angle)), angle]
    return new_node
    
  def move4(self,node):
    angle = (node[2] -30)%360
    new_node = [node[0] + 0.5*math.cos(math.radians(angle)), node[1] + 0.5*math.sin(math.radians(angle)),angle]
    return new_node
    
  def move5(self,node):
    angle = (node[2] -60)%360
    new_node = [node[0] + 0.5*math.cos(math.radians(angle)), node[1] + 0.5*math.sin(math.radians(angle)), angle]
    return new_node
    
  # Method to generate index given a node
  def index(self, node):
    return node[0] + node[1]*100
    
  # Method that generates valid children given a node
  def child_generator(self, node):
    # List to store all valid children
    valid_children = []
    # Generating the children
    n1 = self.move1(node)
    n2 = self.move2(node)
    n3 = self.move3(node)
    n4 = self.move4(node)
    n5 = self.move5(node)
    # List to store all children
    childs = [n1,n2,n3,n4,n5]
    #print('The Children are:', childs)
    # Check for valid children and append them to the list
    for child in childs:
      if a_star_algo.check_node(child, self.clearance) == True and visited_nodes[int(round(child[0],1)/0.5)][int(round(child[1],1)/0.5)][int(round(child[2],1)/30)] == 0:
        #print('The current node is:', (self.current_node[0], self.current_node[1]), 'The child node is:', (child[0], child[1]))
        #plt.quiver(np.array((self.current_node[0])), np.array((self.current_node[1])), np.array((child[0])), np.array((child[1])), units='xy' ,scale=1)
        plt.scatter(child[0], child[1], marker='o')
        valid_children.append(child)
        visited_nodes[int(round(child[0],1)/0.5)][int(round(child[1],1)/0.5)][int(round(child[2],1)/30)] = 1
        
    return valid_children

  def astar(self, goal_node):
    explored_nodes = [self.current_node]
    while len(explored_nodes) > 0:
      c1 = explored_nodes[0]
      print('C1 is:', c1)
      explored_nodes.pop(0)
      childs =  self.child_generator(c1)
      for child in childs:
        explored_nodes.append(child)
      if ((c1[0] - goal_node[0]) ** 2 + (c1[1] - goal_node[1]) ** 2) <= 1.5 ** 2:
        print('Goal node found!')
        break
    #print('The explored nodes were:', explored_nodes)
    #print('')

    
    
