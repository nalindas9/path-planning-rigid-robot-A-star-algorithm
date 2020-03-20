"""
Path Planning for Rigid Robot using A* Algorithm

Authors:
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import matplotlib.pyplot as plt
import numpy as np
import custom_map
import a_star_algo
import node

# Main Function
def main():
  # Taking the obstacle clearance and the robot radius from the user
  clearance = eval(input('Enter the clearance of the robot from the obstacle:'))
  print('The clearance value you entered is:', clearance)
  print('')
  
  radius = eval(input('Enter the robot radius:'))
  print('The radius value you entered is:', radius)
  print('')
  
  # Taking the Start Point and Goal Points from the user
  start_point = eval(input('Please enter the start coordinates in this format - [X_coord, Y_coord, Theta]:'))
  while not a_star_algo.check_node(start_point, radius+clearance):
    start_point = eval(input('Please enter the start coordinates in this format - [X_coord, Y_coord, Theta]:'))
  print('The start point you entered is:', start_point)
  print('')
  start_circle = plt.Circle((start_point[0], start_point[1]), radius= radius+clearance, fc='g')
  plt.gca().add_patch(start_circle)
  
  goal_point = eval(input('Please enter the goal coordinates in this format - [X_coord, Y_coord, Theta]:'))
  while not a_star_algo.check_node(goal_point, radius+clearance):
    goal_point = eval(input('Please enter the goal coordinates in this format - [X_coord, Y_coord, Theta]:'))
  print('The goal point you entered is:', goal_point)
  print('')
  goal_circle = plt.Circle((goal_point[0], goal_point[1]), radius= 1.5,fill=False)
  plt.gca().add_patch(goal_circle)
  
  # Taking the step size of movement from the user
  step_size = eval(input('Enter the movement step size:'))
  print('The step size value you entered is:', step_size)
  print('')
  
  # Taking the step size of movement from the user
  theta = eval(input('Enter the angle between the action set for any given node:'))
  print('The angle value you entered is:', theta)
  print('')

  s1 = node.Node(start_point, goal_point, [0,0], radius+clearance, step_size)
  path, explored = s1.astar()
  
  plt.title('Path planning implemented for a Rigid Robot using A* Algorithm',fontsize=10)
  
  # Plotting the explored nodes and final path
  points1x = []
  points1y = []
  points2x = []
  points2y = []
  points3x = []
  points3y = []
  points4x = []
  points4y = []
  
  for point in range(len(explored)):
    if point+1 < len(explored):
      points1x.append(explored[point][0])
      points1y.append(explored[point][1])
      points2x.append((explored[point+1][0])-(explored[point][0]))
      points2y.append((explored[point+1][1])-(explored[point][1]))
    else:
      points1x.append(explored[point][0])
      points1y.append(explored[point][1])
      points2x.append((explored[-1][0])-(explored[point][0]))
      points2y.append((explored[-1][1])-(explored[point][1]))
      
  for point in range(len(path)):
    if point+1 < len(path):
      points3x.append(path[point][0])
      points3y.append((path[point][1]))
      points4x.append((path[point+1][0])-(path[point][0]))
      points4y.append((path[point+1][1])-(path[point][1]))
    else:
      points3x.append(path[point][0])
      points3y.append((path[point][1]))
      points4x.append((path[-1][0])-(path[point][0]))
      points4y.append((path[-1][1])-(path[point][1]))
  
  plt.quiver(np.array(points1x), np.array(points1y), np.array(points2x), np.array(points2y), units='xy' ,scale=1, label = 'Final Path', color = 'r')
     
  plt.quiver(np.array(points3x), np.array(points3y), np.array(points4x), np.array(points4y), units='xy' ,scale=1, label = 'Final Path')
  plt.show() 
      
  
if __name__ == '__main__':
  main()
