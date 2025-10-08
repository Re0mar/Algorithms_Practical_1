import re

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class Road:
  def __init__(self, startstage, endstage, transport):
    self.startStage = startstage
    self.endStage = endstage
    self.transport = transport

  def __repr__(self):
      return "Road from %s to %s, for %s" % (self.startStage, self.endStage, self.transport)

  def __str__(self):
      return "Road from %s to %s, for %s" % (self.startStage, self.endStage, self.transport)


def constructRoadGraph(inputfile):
    countedroads = 0
    constructroads = []

    intputFile = open(inputfile)

    #Line structure: "a b", with a: number of stages, b: number of roads
    stagelist = re.sub(r'[^0-9\s]', '', intputFile.readline()).split() #Splits on whitespaces, so should be right
    expectedroads = int(stagelist[1])
    expectedstages = int(stagelist[0])

    # Line structure: "a b c", with a: root stage, b: dest stage, c: transport
    # We're using re.sub to ensure that no
    for line in intputFile:
        countedroads += 1
        road = re.sub(r'[^0-9\s]', '', line).split()
        constructroads.append(Road(int(road[0]), int(road[1]), int(road[2]))) #Should make new road from 0 to 1 with transport of 2

    return expectedstages, expectedroads, countedroads, constructroads


if __name__ == '__main__':
    stages, neededRoads, roadCount, roads = constructRoadGraph("testset1.txt")
    print("Stages: %s, Needed roads: %s, Actual Roads: %s" % (stages, neededRoads, roadCount))
    for road in roads:
        print(road)

