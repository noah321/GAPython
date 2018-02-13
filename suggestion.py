'''
A Genetic Algorithm (GA) approach to the Traveling Salesman Problem (TSP).
'''

from random import shuffle, randint;

#Generate list of 100 locations with [x, y] values of 0-5000.
locations = [[randint(0, 5000), randint(0, 5000)] for i in range(100)];
defaultRoute = [i for i in range(len(locations) - 1)];

mutateRate = 2;
generationSize = 5000;
generationsToRun = 1000;

class Organism():
	def __init__(self, classifyData):
		self.classifyData = classifyData;
		self.routeLength = self.calculateRouteLength(classifyData);
		
	def calculateRouteLength(self, classifyData):
		distance = 0;

		for count in range(1, len(classifyData)):
			x2, x1 = locations[classifyData[count]][0], locations[classifyData[count - 1]][0];
			y2, y1 = locations[classifyData[count]][1], locations[classifyData[count - 1]][1];

			distance += (( ((x2 - x1)**2) + ((y2 - y1)**2) ) ** 0.5);

		return distance;


def genOrganism():
	newRoute = defaultRoute[:];
	shuffle(newRoute)
	return Organism(newRoute);

def mutateOrganism(orgOne):
	newRoute = orgOne.classifyData;
	for i in range(randint(0, mutateRate)):
		toChange = randint(0, len(newRoute) - 1);
		toSwitch = randint(0, len(newRoute) - 1);
		if (toChange != toSwitch):
			valOne = newRoute[toChange];
			valTwo = newRoute[toSwitch];

			newRoute[toChange] = valTwo;
			newRoute[toSwitch] = valOne;

	return Organism(newRoute);


def findBestOrganism(organisms):
	bestRoute = organisms[0].routeLength;
	bestRouteIndex = 0;

	for count, organism in enumerate(organisms):
		if (organism.routeLength < bestRoute):	
			bestRoute = organism.routeLength;
			bestRouteIndex = count;

	return organisms[bestRouteIndex];


generation = [genOrganism() for i in range(generationSize)];
print("First random organism: " + str(generation[0].routeLength));
for i in range(generationsToRun):
	topOrganism = findBestOrganism(generation);
	print(topOrganism.routeLength);
	generation = [mutateOrganism(topOrganism) for i in range(generationSize - 1)];
	generation.append(topOrganism);
