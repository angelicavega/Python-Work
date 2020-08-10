class Node:
  def __init__(self, value):
    self.value = value
    self.adjacentNodes = []

def depthFirst(node, goalValue):
  if node.value == goalValue:
    return True
  
  for adjNode in node.adjacentNodes:
    depthFirst(adjNode, goalValue)

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