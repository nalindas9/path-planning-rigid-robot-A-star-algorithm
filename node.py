"""
Node class for A* Algorithm

Authors:
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import math

class Node():
  # Constructor for Node class
  def __init__(self, start_node, parent_node, index):
    self.current_node = start_node
    self.parent_node = parent_node
    self.index = index
    
  # Defining action set
  def move1(self):
    new_node = [self.current_node[0] + 0.5*math.cos(math.radians(60)), self.current_node[1] + 0.5*math.sin(math.radians(60))]
    return new_node
    
  def move2(self):
    new_node = [self.current_node[0] + 0.5*math.cos(math.radians(30)), self.current_node[1] + 0.5*math.sin(math.radians(30))]
    return new_node
    
  def move3(self):
    new_node = [self.current_node[0] + 0.5*math.cos(math.radians(0)), self.current_node[1] + 0.5*math.sin(math.radians(0))]
    return new_node
    
  def move4(self):
    new_node = [self.current_node[0] + 0.5*math.cos(math.radians(-30)), self.current_node[1] + 0.5*math.sin(math.radians(-30))]
    return new_node
    
  def move5(self):
    new_node = [self.current_node[0] + 0.5*math.cos(math.radians(-60)), self.current_node[1] + 0.5*math.sin(math.radians(-60))]
    return new_node
