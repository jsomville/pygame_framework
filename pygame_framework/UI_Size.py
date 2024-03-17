class UI_Size():
    width : int = 0
    height : int = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return "(" + str(self.width) + "," + str(self.height) + ")"

    def __eq__(self, other):
        return (self.width == other.width) and (self.height == other.height)