import turtle
import random
from tree import *

class Forest:
    def __init__(self, density, percentPine, wetness):
        self.density = density
        self.percentPine = percentPine
        self.wetness = wetness
        self.trees = [[None for x in range(40)] for y in range(40)]
        self.burningCoordinate = []
        self.addTree()
        self.setFire()
        self.redraw()

    def addTree(self):
        for i in range(40):
            for j in range(40):
                r = random.random()
                if r <= self.density:
                    randnumer = random.random()
                    if randnumer <= self.percentPine:
                        self.trees[i][j] = Pine(i, j, self.wetness)
                    else:
                        self.trees[i][j] = Oak(i, j, self.wetness)

    def updateForest(self):
        turtle.clearstamps()
        for i, j in self.burningCoordinate:
            self.updateNeighbor(i, j)
        self.removeTrees(self.burningCoordinate)
        self.burningCoordinate = []
        for i in range(40):
            for j in range(40):
                if self.trees[i][j] and self.trees[i][j].burning:
                    self.burningCoordinate.append((i, j))
        self.redraw()
        turtle.update()

    def removeTrees(self, tree_list):
        for i, j in tree_list:
            self.trees[i][j] = None

    def updateNeighbor(self, i , j):
        if self.thereistree(i - 1, j):
            self.tryToBurn(i - 1, j)
        if self.thereistree(i + 1, j):
            self.tryToBurn(i + 1, j)
        if self.thereistree(i, j - 1):
            self.tryToBurn(i, j - 1)
        if self.thereistree(i, j + 1):
            self.tryToBurn(i, j + 1)

    def thereistree(self, i, j):
        return i >= 0 and i < 40 and j >= 0 and j < 40 and self.trees[i][j] != None

    def tryToBurn(self, i , j):
        r = random.random()
        if r < self.trees[i][j].probCatch:
            self.trees[i][j].burning = True

    def redraw(self):
        for x in range(40):
            for y in range(40):
                if self.trees[x][y]:
                    self.trees[x][y].draw()


    def isBurning(self):
        for i in range(40):
            for j in range(40):
                if self.trees[i][j] and self.trees[i][j].burning:
                    return True
        return False

    def setFire(self):
        i = random.randint(0, 40)
        j = random.randint(0, 40)
        while self.trees[i][j] is None:
            i = random.randint(0, 40)
            j = random.randint(0, 40)
        self.trees[i][j].burning = True
        self.burningCoordinate.append((i, j))
