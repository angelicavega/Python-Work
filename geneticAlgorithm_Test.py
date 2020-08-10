import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt

#For this section I will create a new Alien World class that will help determine the fitness, route, population, distance, individual ranking, mating pool, and generation.
class World:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, world):
        xDis = abs(self.x - world.x)
        yDis = abs(self.y - world.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
#The Fitness will help determine the path and distance that the alien population will partake under route, distance, and fitness classfications.
class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0
    
    def routeAlienDistance(self):
        if self.distance ==0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromWorld = self.route[i]
                toWorld = None
                if i + 1 < len(self.route):
                    toWorld = self.route[i + 1]
                else:
                    toWorld = self.route[0]
                pathDistance += fromWorld.distance(toWorld)
            self.distance = pathDistance
        return self.distance
    
    def routeAlienFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeAlienDistance())
        return self.fitness

#Here is a normal sample code that will create a new "World List" for the alien route.
def createAlienRoute(worldList):
    route = random.sample(worldList, len(worldList))
    return route

#Here the code will initialize the alien population size.
def initialAlienPopulation(popSize, worldList):
    population = []

    for i in range(0, popSize):
        population.append(createAlienRoute(worldList))
    return population

#Under this section, each alien's individual ranking will be calculated.
def rankAlienRoutes(population):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i]).routeAlienFitness()
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)

#In order to determine the best out of the best, a more refined list of rankings will be generated.
def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults

#The Alien Mating Pool will be determined by the general population.
def matingAlienPool(population, selectionResults):
    matingAlienpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingAlienpool.append(population[index])
    return matingAlienpool

#From the mating pool, a crossover function is created in order to generate alien children from two seperate parents.
def alienBreed(alienparent1, alienparent2):

    alienchild = []
    alienchildP1 = []
    alienchildP2 = []
    
    geneA = int(random.random() * len(alienparent1))
    geneB = int(random.random() * len(alienparent1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        alienchildP1.append(alienparent1[i])
        
    alienchildP2 = [item for item in alienparent2 if item not in alienchildP1]

    alienchild = alienchildP1 + alienchildP2
    return alienchild

#From the mating pool, a crossover function is created in order to generate alien children from two seperate parents.
def alienBreed(alienparent1, alienparent2):

    alienchild = []
    alienchildP1 = []
    alienchildP2 = []
    
    geneA = int(random.random() * len(alienparent1))
    geneB = int(random.random() * len(alienparent1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        alienchildP1.append(alienparent1[i])
        
    alienchildP2 = [item for item in alienparent2 if item not in alienchildP1]

    alienchild = alienchildP1 + alienchildP2
    return alienchild

#A new alien children breed population will stem from the elite section of the general population.
def alienBreedPopulation(matingalienpool, eliteSize):
    alienchildren = []
    length = len(matingalienpool) - eliteSize
    pool = random.sample(matingalienpool, len(matingalienpool))

    for i in range(0,eliteSize):
        alienchildren.append(matingalienpool[i])
    
    for i in range(0, length):
        alienchild = alienBreed(pool[i], pool[len(matingalienpool)-i-1])
        alienchildren.append(alienchild)
    return alienchildren

#In this section, a new mutating function will be added in order to 
def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            
            world1 = individual[swapped]
            world2 = individual[swapWith]
            
            individual[swapped] = world2
            individual[swapWith] = world1
    return individual

#Same function as above, is continued here:
def mutateAlienPopulation(population, mutationRate):
    mutatedPop = []
    
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

#Here, the next generation of the alien population will be determined, including the current generation, with the elite and mutated.
def nextAlienGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankAlienRoutes(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingalienpool = matingAlienPool(currentGen, selectionResults)
    alienchildren = alienBreedPopulation(matingalienpool, eliteSize)
    nextAlienGeneration = mutateAlienPopulation(alienchildren, mutationRate)
    return nextAlienGeneration

#Here the generic algorithm is implemented using all functions created in order to determine a random sample using the best route for the new alien population.
def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    pop = initialAlienPopulation(popSize, population)
    print("Initial distance: " + str(1 / rankAlienRoutes(pop)[0][1]))
    
    for i in range(0, generations):
        pop = nextAlienGeneration(pop, eliteSize, mutationRate)
    
    print("Final distance: " + str(1 / rankAlienRoutes(pop)[0][1]))
    bestRouteIndex = rankAlienRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute

#Genetic Algorithm
#--------------------------------------------------------------------------------------------------

#The New Alien World is created!
worldList = []

for i in range(0,25):
    worldList.append(World(x=int(random.random() * 200), y=int(random.random() * 200)))

#Here we run the genetic algorithm in order to visually finalize our report!
geneticAlgorithm(population=worldList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)

#Here we plot the algorithm
def geneticAlgorithmPlot(population, popSize, eliteSize, mutationRate, generations):
    pop = initialAlienPopulation(popSize, population)
    progress = []
    progress.append(1 / rankAlienRoutes(pop)[0][1])
    
    for i in range(0, generations):
        pop = nextAlienGeneration(pop, eliteSize, mutationRate)
        progress.append(1 / rankAlienRoutes(pop)[0][1])
    
    plt.plot(progress)
    plt.ylabel('Distance Traveled')
    plt.xlabel('Total Generation')
    plt.show()

geneticAlgorithmPlot(population=worldList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)