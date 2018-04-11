from backend.member import*

class GUIMember:
    def __init__(self, member, mother, father):
        self.member = member
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.mother = mother
        self.father = father

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

    def getMother(self):
        return self.mother

    def getFather(self):
        return self.father

    def setFather(self, father):
        self.father = father

    def setMother(self, mother):
        self.mother = mother
    
    def __repr__(self):
        return "{%s M[%s] F[%s] [%d %d] [%d %d]}" % (self.member, self.mother, self.father, self.x, self.y, self.width, self.height)

    def __str__(self):
        return "{%s M[%s] F[%s] [%d %d] [%d %d]}" % (self.member, self.mother, self.father, self.x, self.y, self.width, self.height)



    