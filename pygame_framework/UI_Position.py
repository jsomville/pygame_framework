class UI_Position():
    x : int = 0
    y : int = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)