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
import operator
import random 

k = 0
# 3D array with (x,y,theta) as index
visited_nodes = np.zeros((600,400,12))
# Dictionary for backtracking 
valid_childs_dict = {}
# List to store all the explored nodes for visualization
explored = []
# Node class containing action set, graph generation and Astar Algorithm

class Node():
  # Constructor for Node class
  def __init__(self, start_node, goal_node, parent_node, clearance, step_size):
    self.start_node = start_node
    self.parent_node = parent_node
    self.clearance = clearance
    self.goal_node = goal_node
    self.step_size = step_size
    
  # Defining action set and graph generation
  def move1(self,node, cost):
    angle = (node[2] + 60)%360
    new_node = [node[0] + (0.5*math.cos(math.radians(angle)))*self.step_size, node[1] + (0.5*math.sin(math.radians(angle)))*self.step_size, angle]
    cost2come = cost + 1.5*self.step_size
    cost2go = 2.8*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move2(self,node, cost):
    angle = (node[2] + 30)%360
    new_node = [node[0] + (0.5*math.cos(math.radians(angle)))*self.step_size, node[1] + (0.5*math.sin(math.radians(angle)))*self.step_size, angle]
    cost2come = cost + 1.3*self.step_size
    cost2go = 2.8*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move3(self,node, cost):
    angle = (node[2] + 0)%360
    new_node = [node[0] + (0.5*math.cos(math.radians(angle)))*self.step_size, node[1] + (0.5*math.sin(math.radians(angle)))*self.step_size, angle]
    cost2come = cost + 1*self.step_size
    cost2go = 2.8*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move4(self,node, cost):
    angle = (node[2] -30)%360
    new_node = [node[0] + (0.5*math.cos(math.radians(angle)))*self.step_size, node[1] + (0.5*math.sin(math.radians(angle)))*self.step_size,angle]
    cost2come = cost + 1.3*self.step_size
    cost2go = 2.8*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move5(self,node, cost):
    angle = (node[2] -60)%360
    new_node = [node[0] + (0.5*math.cos(math.radians(angle)))*self.step_size, node[1] + (0.5*math.sin(math.radians(angle)))*self.step_size, angle]
    cost2come = cost + 1.5*self.step_size
    cost2go = 2.8*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  # Method to generate index given a node
  def index(self, node):
    return (node[0], node[1], node[2])
    
  # Method that generates valid children given a node
  def child_generator(self, node, cost):
    # List to store all valid children
    valid_children = []
    # Generating the children
    n1 = self.move1(node, cost)
    n2 = self.move2(node, cost)
    n3 = self.move3(node, cost)
    n4 = self.move4(node, cost)
    n5 = self.move5(node, cost)
    # List to store all children
    childs = [n1,n2,n3,n4,n5]
    # Dictionary with cost as key and child as value
    childs_cost = {n1[3]:n1,n2[3]:n2,n3[3]:n3,n4[3]:n4,n5[3]:n5}
    # Check for valid children and append them to the list
    for cost in childs_cost.keys():
      if a_star_algo.check_node(childs_cost[cost], self.clearance) == True and visited_nodes[int(round(childs_cost[cost][0],1)/0.5)][int(round(childs_cost[cost][1],1)/0.5)][int(round(childs_cost[cost][2],1)/30)] == 0:
        valid_children.append((cost, childs_cost[cost], childs_cost[cost][4], self.index(childs_cost[cost]),node))
        valid_childs_dict[self.index(childs_cost[cost])] = [childs_cost[cost], node, self.index(node)]
        visited_nodes[int(round(childs_cost[cost][0],1)/0.5)][int(round(childs_cost[cost][1],1)/0.5)][int(round(childs_cost[cost][2],1)/30)] = 1
        
    return valid_children

  def astar(self):
    print('Started Search ... ')
    explored_nodes = [(0, self.start_node, self.index(self.start_node), self.parent_node)]
    explored.append(self.start_node)
    valid_childs_dict[self.index(self.start_node)] = [self.start_node, self.parent_node]
    cum_cost = 0
    itr = 0
    while len(explored_nodes) > 0:
      print('Explored Depth:', itr)
      min_cost_child = explored_nodes[0][1]
      explored_nodes.pop(0)
      child_costs= self.child_generator(min_cost_child, cum_cost)
      for child in child_costs:
        explored_nodes.append(child)
        explored.append(child[1])
      explored_nodes.sort(key=operator.itemgetter(0))
      cum_cost = explored_nodes[0][2]
      itr = itr+1
      if ((min_cost_child[0] - self.goal_node[0]) ** 2 + (min_cost_child[1] - self.goal_node[1]) ** 2) <= 1.5 ** 2:
        final_node_key =  explored_nodes[0][3]
        print('Goal node found!')
        break 
    print('Started Backtracking ...')
    final_path= self.back_track(final_node_key)
    print('Backtracking complete!')
    return final_path, explored
        
  def back_track(self, node_ind):
    path = [valid_childs_dict[node_ind][0]]
    while node_ind != self.index(self.start_node):
      parent = valid_childs_dict[node_ind][1]
      path.insert(0, parent)
      node_ind = valid_childs_dict[node_ind][2]
    print('The path is:', path)
    return path
    
