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
  def move1(self):
    new_node = [self.current_node[0] + 0.5*math.cos(math.radians(self.current_node[0] + 60)), self.current_node[1] + 0.5*math.sin(math.radians(60)), self.current_node[0] + 60]
    return new_node
    
  def move2(self):
    new_node = [self.current_node[0] + 0.5*math.cos(math.radians(self.current_node[0] + 30)), self.current_node[1] + 0.5*math.sin(math.radians(30)), self.current_node[0] + 30]
    return new_node
    
  def move3(self):
    new_node = [self.current_node[0] + 0.5*math.cos(math.radians(self.current_node[0] + 0)), self.current_node[1] + 0.5*math.sin(math.radians(0)), self.current_node[0] + 0]
    return new_node
    
  def move4(self):
    new_node = [self.current_node[0] + 0.5*math.cos(math.radians(self.current_node[0] -30)), self.current_node[1] + 0.5*math.sin(math.radians(-30)), self.current_node[0] - 30]
    return new_node
    
  def move5(self):
    new_node = [self.current_node[0] + 0.5*math.cos(math.radians(self.current_node[0] -60)), self.current_node[1] + 0.5*math.sin(math.radians(-60)), self.current_node[0] - 60]
    return new_node
    
  # Method to generate index given a node
  def index(self, node):
    return node[0] + node[1]*100
    
  # Method that generates valid children given a node
  def child_generator(self):
    # List to store all valid children
    valid_children = []
    # Generating the children
    n1 = self.move1()
    n2 = self.move2()
    n3 = self.move3()
    n4 = self.move4()
    n5 = self.move5()
    # List to store all children
    childs = [n1,n2,n3,n4,n5]
    print('The Children are:', childs)
    # Check for valid children and append them to the list
    for child in childs:
      if a_star_algo.check_node(child, self.clearance) == True and visited_nodes[int(round(child[0],1)/0.5)][int(round(child[1],1)/0.5)][int(round(child[2],1)/30)] == 0:
        #print('The current node is:', (self.current_node[0], self.current_node[1]), 'The child node is:', (child[0], child[1]))
        #plt.quiver(np.array((self.current_node[0])), np.array((self.current_node[1])), np.array((child[0])), np.array((child[1])), units='xy' ,scale=1)
        plt.scatter(child[0], child[1], marker='o')
        valid_children.append(child)
        visited_nodes[int(round(child[0],1)/0.5)][int(round(child[1],1)/0.5)][int(round(child[2],1)/30)] == 1
        
    return valid_children
    
    
