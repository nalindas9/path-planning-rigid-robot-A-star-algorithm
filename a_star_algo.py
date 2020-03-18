"""
A* Algorithm

Authors:
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import numpy as np
import math
import node

# Function to generate new points
def new_points(point, clearance, direction):
  if direction == 0:
    point[1] = point[1] - np.sqrt(2)*clearance
  elif direction == 1:
    point[0] = point[0] + np.sqrt(2)*clearance
  elif direction == 2:
    point[1] = point[1] + np.sqrt(2)*clearance
  else:
    point[0] = point[0] - np.sqrt(2)*clearance
  return point
    
# Function to generate new points for the concave polygon
def new_points_pol(point, point0, point1, point3, clearance, direction):
  if direction == 0:
    slope1 = (point1[1] - point[1]) / (point1[0] - point[0])
    a1 = (90 - math.degrees(math.atan(slope1)))/2
    l1 = clearance/math.sin(math.radians(a1))
    x1 = l1*math.sin(math.radians(a1))
    y1 = l1*math.cos(math.radians(a1))       
    point[0] = point[0] - x1 
    point[1] = point[1] - y1 
  elif direction == 1:
    point[1] = point[1] - np.sqrt(2)*clearance
  elif direction == 2:
    point[1] = point[1] - np.sqrt(2)*clearance 
  elif direction == 3:
    point[0] = point[0] + np.sqrt(2)*clearance
  elif direction == 4:
    slope4 = (point[1] - point1[1]) / (point[0] - point1[0])
    a4 = math.degrees(math.atan(slope4))
    l4 = clearance/math.sin(math.radians(a4))
    x4 = l4*math.cos(math.radians(a4))
    y4 = l4*math.sin(math.radians(a4))       
    point[0] = point[0] + x4 
    point[1] = point[1] + y4 
  else:
    slope5 = (point[1] - point1[1]) / (point[0] - point1[0])
    a5 = 180 - math.degrees(math.atan(slope5))
    l5 = clearance/math.sin(math.radians(a5))
    x5 = l5*math.cos(math.radians(a5))
    y5 = l5*math.sin(math.radians(a5))       
    point[0] = point[0] - x5 
    point[1] = point[1] + y5 
  return point
# Function to generate new equation of line acc. to new points

def eqn(point1, point2):
  a = point1[1] - point2[1]
  b = point2[0] - point1[0]
  c = point1[1]*b - point1[0]*(-a)
  return a,b,c

# Function to check if the given point lies outside the final map or in the obstacle space
def check_node(node, clearance):
  u = 150.  # x-position of the center
  v = 100.  # y-position of the center
  a = 40.  # radius on the x-axis
  b = 20.  # radius on the y-axis

  clear_val = clearance

  # New points for diamond obstacle
  p1 = new_points([225,15], clear_val, 0)
  p2 = new_points([250,30], clear_val, 1)
  p3 = new_points([225,45], clear_val, 2)
  p4 = new_points([200,30], clear_val, 3)


  # New lines for diamond obstacle

  a1,b1,c1 = eqn(p1,p2)
  a2,b2,c2 = eqn(p2,p3)
  a3,b3,c3 = eqn(p3,p4)
  a4,b4,c4 = eqn(p4,p1)   

  # New points for tilted cuboid
  p5 = new_points([95,30], clear_val, 0)
  p6 = new_points([100,38.66], clear_val, 1)
  p7 = new_points([35.05,76.16], clear_val, 2)
  p8 = new_points([30.05,67.5], clear_val, 3)

    
  # New lines for tilted cuboid

  a5,b5,c5 = eqn(p5,p6)
  a6,b6,c6 = eqn(p6,p7)
  a7,b7,c7 = eqn(p7,p8)
  a8,b8,c8 = eqn(p8,p5)

  # New points for concave polygon
  p9 = new_points_pol([20,120], [20,120], [50,150], [100,150],clear_val, 0)
  p10 = new_points_pol([50,150], [20,120], [50,150], [100,150],clear_val, 1)
  p11 = new_points_pol([75,120],[20,120], [50,150], [100,150],clear_val, 2)
  p12 = new_points_pol([100,150], [20,120], [50,150], [100,150],clear_val, 3)
  p13 = new_points_pol([75,185], [20,120], [50,150], [100,150],clear_val,4)
  p14 = new_points_pol([25,185], [20,120], [50,150], [100,150],clear_val, 5)


  # New lines for concave polygon

  a9,b9,c9 = eqn(p9,p10)
  a10,b10,c10 = eqn(p10,p11)
  a11,b11,c11 = eqn(p11,p12)
  a12,b12,c12 = eqn(p12,p13)
  a13,b13,c13 = eqn(p13,p14)
  a14,b14,c14 = eqn(p14,p9)  
  a15,b15,c15 = eqn(p14,p11)

  if node[0] + clearance >= 300 or node[0] - clearance < 0 or node[1] + clearance>= 200 or node[1] - clearance< 0:
    print('Sorry the point is out of bounds! Try again.')
    return False
  elif (node[0] - 225) ** 2 + (node[1] - 150) ** 2 <= (25+clear_val) ** 2 :
    print('Sorry the point is in the obstacle space! Try again')
    return False
  elif ((node[0] - 150) ** 2) / (a+clear_val) ** 2 + ((node[1] - 100) ** 2) / (b+clear_val) ** 2 <= 1:
    print('Sorry the point is in the obstacle space! Try again')
    return False
  elif (a1*node[0] + b1*node[1]>=c1) and (a2*node[0] + b2*node[1]>=c2) and (
        a3*node[0] + b3*node[1]>=c3) and (a4*node[0] + b4*node[1]>=c4):
    print('Sorry the point is in the obstacle space! Try again')
    return False
  elif (a5*node[0] + b5*node[1]>=c5) and (a6*node[0] + b6*node[1]>=c6) and (
        a7*node[0] + b7*node[1]>=c7) and (a8*node[0] + b8*node[1]>=c8):
    print('Sorry the point is in the obstacle space! Try again')
    return False
  # Dividing concave shape into 2 convex shapes
  elif (a10*node[0] + b10*node[1]>=c10) and (a11*node[0] + b11*node[1]>=c11) and (a12*node[0] + b12*node[1]>=c12) and (a13*node[0] + b13*node[1]>=c13):
    print('Sorry the point is in the obstacle space! Try again')
    return False
  elif (a10*node[0] + b10*node[1]<=c10) and (a14*node[0] + b14*node[1]>=c14) and (a9*node[0] + b9*node[1]>=c9):
    print('Sorry the point is in the obstacle space! Try again')
    return False
  else:
    return True
"""
def astar(start_node, goal_node, step_size):
  explored_nodes = [start_node]
  print('Startnode is:', start_node)
  while len(explored_nodes) > 0:
    c1 = explored_nodes[0]
    print('C1 is:', c1)
    explored_nodes.pop(0)
    childs =  c1.child_generator()
    for child in childs:
      explored_nodes.append(child)
    if (c1 == goal_node):
      print('Goal node found!')
      break
  print('The explored nodes were:', explored_nodes)
  print('')
"""      
  
