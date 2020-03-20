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

class Node():
  # Constructor for Node class
  def __init__(self, start_node, goal_node, parent_node, clearance, step_size):
    self.start_node = start_node
    self.parent_node = parent_node
    self.clearance = clearance
    self.goal_node = goal_node
    self.step_size = step_size
    
  # Defining action set and graph generationb 
  def move1(self,node, cost):
    angle = (node[2] + 60)%360
    new_node = [node[0] + (0.5*math.cos(math.radians(angle)))*self.step_size, node[1] + (0.5*math.sin(math.radians(angle)))*self.step_size, angle]
    cost2come = cost + 1.5*self.step_size
    cost2go = 2.8*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    #print('Cost2go 1:', cost2go, 'Cost2come 1:', cost2come)
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move2(self,node, cost):
    angle = (node[2] + 30)%360
    new_node = [node[0] + (0.5*math.cos(math.radians(angle)))*self.step_size, node[1] + (0.5*math.sin(math.radians(angle)))*self.step_size, angle]
    cost2come = cost + 1.3*self.step_size
    cost2go = 2.8*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    #print('Cost2go 2:', cost2go, 'Cost2come 2:', cost2come)
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move3(self,node, cost):
    angle = (node[2] + 0)%360
    new_node = [node[0] + (0.5*math.cos(math.radians(angle)))*self.step_size, node[1] + (0.5*math.sin(math.radians(angle)))*self.step_size, angle]
    cost2come = cost + 1*self.step_size
    cost2go = 2.8*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    #print('Cost2go 3:', cost2go, 'Cost2come 3:', cost2come)
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move4(self,node, cost):
    angle = (node[2] -30)%360
    new_node = [node[0] + (0.5*math.cos(math.radians(angle)))*self.step_size, node[1] + (0.5*math.sin(math.radians(angle)))*self.step_size,angle]
    cost2come = cost + 1.3*self.step_size
    cost2go = 2.8*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    #print('Cost2go 4:', cost2go, 'Cost2come 4:', cost2come)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move5(self,node, cost):
    angle = (node[2] -60)%360
    new_node = [node[0] + (0.5*math.cos(math.radians(angle)))*self.step_size, node[1] + (0.5*math.sin(math.radians(angle)))*self.step_size, angle]
    cost2come = cost + 1.5*self.step_size
    cost2go = 2.8*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    #print('Cost2go 5:', cost2go, 'Cost2come 5:', cost2come)
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
    #print('Childs is:', childs)
    # Dictionary with cost as key and child as value
    childs_cost = {n1[3]:n1,n2[3]:n2,n3[3]:n3,n4[3]:n4,n5[3]:n5}
    #print('The Children are:', childs)
    # Check for valid children and append them to the list
    for cost in childs_cost.keys():
      if a_star_algo.check_node(childs_cost[cost], self.clearance) == True and visited_nodes[int(round(childs_cost[cost][0],1)/0.5)][int(round(childs_cost[cost][1],1)/0.5)][int(round(childs_cost[cost][2],1)/30)] == 0:
        #print('The current node is:', (self.current_node[0], self.current_node[1]), 'The child node is:', (child[0], child[1]))
        #plt.quiver(np.array((self.current_node[0])), np.array((self.current_node[1])), np.array((child[0])), np.array((child[1])), units='xy' ,scale=1)
        #plt.scatter(childs_cost[cost][0], childs_cost[cost][1], marker='o')
        valid_children.append((cost, childs_cost[cost], childs_cost[cost][4], self.index(childs_cost[cost]),node))
        valid_childs_dict[self.index(childs_cost[cost])] = [childs_cost[cost], node, self.index(node)]
        visited_nodes[int(round(childs_cost[cost][0],1)/0.5)][int(round(childs_cost[cost][1],1)/0.5)][int(round(childs_cost[cost][2],1)/30)] = 1
        
    return valid_children

  def astar(self):
    explored_nodes = [(0, self.start_node, self.index(self.start_node), self.parent_node)]
    valid_childs_dict[self.index(self.start_node)] = [self.start_node, self.parent_node]
    cum_cost = 0
    while len(explored_nodes) > 0:
      #print('Valid Childs dict is:', valid_childs_dict)
      min_cost_child = explored_nodes[0][1]
      print('C1 is:', min_cost_child)
      explored_nodes.pop(0)
      child_costs= self.child_generator(min_cost_child, cum_cost)
      for child in child_costs:
        explored_nodes.append(child)
      explored_nodes.sort(key=operator.itemgetter(0))
      #print('Sorted Explored Nodes is:', explored_nodes)
      cum_cost = explored_nodes[0][2]
      if ((min_cost_child[0] - self.goal_node[0]) ** 2 + (min_cost_child[1] - self.goal_node[1]) ** 2) <= 1.5 ** 2:
        final_node_key =  explored_nodes[0][3]
        print('The final key is:', final_node_key)
        #print('The final dict is:', valid_childs_dict)
        print('Goal node found!')
        break 
    final_path= self.back_track(final_node_key)
    return final_path
        
  def back_track(self, node_ind):
    path = [valid_childs_dict[node_ind][0]]
    while node_ind != self.index(self.start_node):
      parent = valid_childs_dict[node_ind][1]
      path.insert(0, parent)
      """
      for key in valid_childs_dict.keys():
        if (parent == valid_childs_dict[key][0]):
          parent_key = key
        else:
          continue
      """
      node_ind = valid_childs_dict[node_ind][2]
      #print('Node index is:', node_ind)
    print('The path is:', path)
    return path
    
    """
    goal_found = False
    cum_cost = 0
    while not goal_found:
      childs, child_costs = self.child_generator(self.start_node, cum_cost)
      cum_cost = min(child_costs.keys())
      print('The cost with child is:', child_costs)
      print('The child costs is:', child_costs.keys(), 'The child with least cost is:', cum_cost)
      self.start_node = child_costs[cum_cost]
      print('The current node is:', self.start_node)
      if ((self.start_node[0] - self.goal_node[0]) ** 2 + (self.start_node[1] - self.goal_node[1]) ** 2) <= 1.5 ** 2:
        goal_found = True
    print('Goal node found!')
   """
  """
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
  """
    
    
