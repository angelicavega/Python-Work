#Breadth-First Search Algorithm
from collections import deque

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

def breadthFirstGrid(start)
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

breadthFirst()
breadthFirstGrid()
    
