"""
Path Planning for Rigid Robot using A* Algorithm

Authors:
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import matplotlib.pyplot as plt
import custom_map
import node

def main():
  # Taking the Start Point and Goal Points from the user
  start_point = eval(input('Please enter the start coordinates in this format - [X_coord, Y_coord, Theta]:'))
  print('The start point you entered is:', start_point)
  print('')
  
  goal_point = eval(input('Please enter the goal coordinates in this format - [X_coord, Y_coord, Theta]:'))
  print('The goal point you entered is:', goal_point)
  print('')
  
  # Taking the obstacle clearance and the robot radius from the user
  clearance = eval(input('Enter the clearance of the robot from the obstacle:'))
  print('The clearance value you entered is:', clearance)
  print('')
  
  radius = eval(input('Enter the robot radius:'))
  print('The radius value you entered is:', radius)
  print('')

  # Taking the step size of movement from the user
  step_size = eval(input('Enter the movement step size:'))
  print('The step size value you entered is:', step_size)
  print('')
  
  # Taking the step size of movement from the user
  theta = eval(input('Enter the angle between the action set for any given node:'))
  print('The angle value you entered is:', theta)
  print('')

  nodel = node.Node([0,0], [10,10], 5)
  new = nodel.move1()
  new1 = nodel.move2()
  new2 = nodel.move3()
  new3 = nodel.move4()
  new4 = nodel.move5()
  print (new)
  
  plt.show()
  
if __name__ == '__main__':
  main()
