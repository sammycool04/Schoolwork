import turtle
class Tree:
    def __init__(self, xpos, ypos, wetness, probCatch):
        self.probCatch = probCatch * (100 - wetness) / 100
        self.wetness = wetness
        self.burning = False
        self.xpos = xpos
        self.ypos = ypos

    def draw(self):
        pass

class Oak(Tree):
    def __init__(self, xpos, ypos, wetness, probCatch=0.45):
        super().__init__(xpos, ypos, wetness, probCatch)

    def draw(self):
        turtle.setheading(90)
        if not self.burning:
            turtle.color("green")
        else:
            turtle.color("red")
        turtle.shape("circle")
        turtle.penup()
        turtle.goto(self.xpos, self.ypos)
        turtle.pendown()
        turtle.stamp()

class Pine(Tree):
    def __init__(self, xpos, ypos, wetness, probCatch=0.95):
        super().__init__(xpos, ypos, wetness, probCatch)

    def draw(self):
        turtle.setheading(90)
        if not self.burning:
            turtle.shape("triangle")
            turtle.color("green")
            turtle.penup()
            turtle.goto(self.xpos, self.ypos)
            turtle.pendown()
            turtle.stamp()
        else:
            turtle.shape("triangle")
            turtle.color("red")
            turtle.penup()
            turtle.goto(self.xpos, self.ypos)
            turtle.pendown()
            turtle.stamp()
