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
  
  print('Explored:', explored)
  plt.title('Path planning implemented for a Rigid Robot using A* Algorithm',fontsize=10)
  
  for point in range(0, 200):
    #plt.scatter(point[0], point[1], marker='o')
    if point+1 < len(explored):
      plt.quiver(np.array((explored[point][0])), np.array((explored[point][1])), np.array((explored[point+1][0])-(explored[point][0])), np.array((explored[point+1][1])-(explored[point][1])), units='xy' ,scale=1, color= 'r', label = 'Explored nodes')
      plt.savefig('/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-rigid-robot-A-star-algorithm/Images/image' + str(point) + '.png')
    else:
      plt.quiver(np.array((explored[point][0])), np.array((explored[point][1])), np.array((explored[-1][0])-(explored[point][0])), np.array((explored[-1][1])-(explored[point][1])), units='xy' ,scale=1, color= 'r', label = 'Explored nodes')
      plt.savefig('/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-rigid-robot-A-star-algorithm/Images/image' + str(point) + '.png')
  
  for point in range(200, 49800, 400):
    #plt.scatter(point[0], point[1], marker='o')
    if point+1 < len(explored):
      plt.quiver(np.array((explored[point][0])), np.array((explored[point][1])), np.array((explored[point+1][0])-(explored[point][0])), np.array((explored[point+1][1])-(explored[point][1])), units='xy' ,scale=1, color= 'r', label = 'Explored nodes')
      plt.savefig('/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-rigid-robot-A-star-algorithm/Images/image' + str(point) + '.png')
    else:
      plt.quiver(np.array((explored[point][0])), np.array((explored[point][1])), np.array((explored[-1][0])-(explored[point][0])), np.array((explored[-1][1])-(explored[point][1])), units='xy' ,scale=1, color= 'r', label = 'Explored nodes')
      plt.savefig('/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-rigid-robot-A-star-algorithm/Images/image' + str(point) + '.png')

  for point in range(49800, len(explored), 1):
    #plt.scatter(point[0], point[1], marker='o')
    if point+1 < len(explored):
      plt.quiver(np.array((explored[point][0])), np.array((explored[point][1])), np.array((explored[point+1][0])-(explored[point][0])), np.array((explored[point+1][1])-(explored[point][1])), units='xy' ,scale=1, color= 'r', label = 'Explored nodes')
      plt.savefig('/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-rigid-robot-A-star-algorithm/Images/image' + str(point) + '.png')
    else:
      plt.quiver(np.array((explored[point][0])), np.array((explored[point][1])), np.array((explored[-1][0])-(explored[point][0])), np.array((explored[-1][1])-(explored[point][1])), units='xy' ,scale=1, color= 'r', label = 'Explored nodes')
      plt.savefig('/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-rigid-robot-A-star-algorithm/Images/image' + str(point) + '.png')

  for point in range(len(path)):
    #plt.scatter(point[0], point[1], marker='o')
    if point+1 < len(path):
      plt.quiver(np.array((path[point][0])), np.array((path[point][1])), np.array((path[point+1][0])-(path[point][0])), np.array((path[point+1][1])-(path[point][1])), units='xy' ,scale=1, label = 'Final path')
      plt.savefig('/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-rigid-robot-A-star-algorithm/Images/image' + str(len(explored)+point) + '.png')
    else:
      plt.quiver(np.array((path[point][0])), np.array((path[point][1])), np.array((path[-1][0])-(path[point][0])), np.array((path[-1][1])-(path[point][1])), units='xy' ,scale=1, label = 'Final Path')
      plt.savefig('/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-rigid-robot-A-star-algorithm/Images/image' + str(len(explored)+point) + '.png')

  #plt.show()
  
if __name__ == '__main__':
  main()
