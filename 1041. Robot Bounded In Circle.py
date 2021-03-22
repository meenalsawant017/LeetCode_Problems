'''
1041. Robot Bounded In Circle

Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees,
and then returns to (0,0).
When repeating these instructions,
the robot remains in the circle of radius 2 centered at the origin.

'''

def isRobotBounded(instructions):
      x, y, degree = 0,0,0
      arr = [1,1,1,1]
      for i in range(len(instructions)):
            if(instructions[i] == 'R'):
                  degree = (degree - 1) % 4
            elif(instructions[i] == 'L'):
                  degree = (degree + 1) % 4
            elif(instructions[i] == 'G'):
                  
                  if(degree == 0):
                        y += arr[degree]
                  if(degree == 1):
                        x += arr[degree]
                  if(degree == 2):
                        y -= arr[degree]
                  if(degree == 3):
                        x -= arr[degree]
      return  (x == 0 and y == 0) or degree != 0 

instructions = "GLRLLGLL"
#instructions = "GGLLGG"
#instructions = "GL"
res = isRobotBounded(instructions)
print(res)
