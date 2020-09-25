import numpy as np
import queue
import time



#Here we attempt to create a 5x5 Grid
for iter in range(5):
   
    n = 5
    grid = np.zeros((n,n))

    #G Node Location
    x = np.random.randint(n)
    y = np.random.randint(n)
    grid[y,x] = 1

    # Start
    start_x,start_y = np.random.randint(n),np.random.randint(n)

class Node:
  def __init__(self, value):
    self.value = value
    self.adjacentNodes = []
    
 #Here is the depth-search code/algorithm
def depthFirst(node, goalValue, visitedNodes):
  if node.value == goalValue:
    return True
  
  visitedNodes.add(node)
  for adjNode in node.adjacentNodes:
    if adjNode not in visitedNodes:
      if depthFirst(adjNode, goalValue, visitedNodes):
        return True
      
  return False
initNode = Node("x")
initNode.adjacentNodes = [Node("x"), Node("x")]
initNode.adjacentNodes[0].adjacentNodes = [Node("x")]
initNode.adjacentNodes[1].adjacentNodes = [Node("G")]
visitedNodes = set()
depthFirst(initNode, "G", visitedNodes)
from collections import deque

#Here is the breadth-search code/algorithm
def breadthFirst(startingNode, goalValue):
  visitedNodes = set()
  queue = deque([startingNode])
  
  while len(queue) > 0:
    node = queue.pop()
    if node in visitedNodes:
      continue
      
    visitedNodes.add(node)
    if node.value == goalValue:
      return True
    
    for n in node.adjacentNodes:
      if n not in visitedNodes:
        queue.appendleft(n)
        
  return False
breadthFirst(initNode, "G")
from collections import deque

def breadthFirstGrid(start):
  visited = set()
  frontier = deque([start])
  
  while len(frontier) > 0:
    nextSquare = frontier.pop()
    if nextSquare in visited:
      continue
      
    visited.add(nextSquare)
    if nextSquare.value == "G":
      return True
    
    (x, y) = nextSquare
    
print('~~~~~~~~~5x5 Grid~~~~~~~~~')
print(grid)

print('~~~~~~~~~Start~~~~~~~~~')
print("Starting X: ",start_x," Starting Y: ",start_y)

print('~~~~~~~~~Results~~~~~~~~~')
print("Depth-Search Algorithm: ", " Execution Time : ", depthFirst)
print("Breadth-First Algoritm: ", " Execution Time : ", breadthFirst)
