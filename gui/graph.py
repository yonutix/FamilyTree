from member import*

class GUIMember:
    def __init__(self, member):
        self.member = member
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0


    def getX(self):
        return self.x
        
    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getMember(self):
        return self.member