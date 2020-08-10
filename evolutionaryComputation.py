charset = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
outcome = ['H', 'E', 'L', 'L', 'O']
stringLength = len(outcome)

# goal is an all-caps string
def fitness(example):
  f = 0
  for ch in example:
    if str.isupper(ch):
      f += 1
  return f



def isOutcome(example, outcome):
  #return fitness(example) == stringLength
  if example == outcome:
    return True

from random import choice,random,randint

maxsteps = 100000

def guessUntilCorrect():
  stepsTaken = 0
  while stepsTaken < maxsteps:
    stepsTaken += 1
    # sample a random string of stringLength
    guess = [choice(charset) for _ in range(stringLength)]
    
    if isOutcome(guess, outcome):
      print(f"Found outcome in {stepsTaken} steps.")
      return guess
    
  return False

guessUntilCorrect()

mutationRate = 0.5 # proportion of "genes" to randomly flip each tie
def mutate(example):
  return [(choice(charset) if random() < mutationRate else ch) for ch in example]

def crossover(parent1, parent2):
  # pick a random point to cross over at
  crossOverPoint = randint(1,stringLength)
  return parent1[:crossOverPoint] + parent2[crossOverPoint:]

example = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(mutate(example))

example1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
example2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(crossover(example1, example2))

populationSize = 50

def geneticAlgorithm():
  iterations = 0

  # the initial population is populationSize random strings
  population = [[choice(charset) for _ in range(stringLength)] for _ in range(populationSize)]

  
  while iterations < maxsteps:
    iterations += 1
    # do any of our population's individuals satisfy the goal?
    for individual in population:
      if (isOutcome(individual, outcome)):
        print(f"Found outcome in {iterations} iterations.")
        return individual
    
    # if not, crossover and mutate to get a new generation
    
    # sort the current population by descending order of fitness
    population.sort(key=fitness, reverse=True)
    
    # take the top 10 (arbitrary number) and make them parents of the new generation
    parents = population[:10]
    # make the next generation by randomly selecting two parents to
    # crossover, and then mutating the result, until we have 50 new individuals
    population = [mutate(crossover(choice(parents),choice(parents))) for _ in range(populationSize)]
  
  
  return False

geneticAlgorithm()