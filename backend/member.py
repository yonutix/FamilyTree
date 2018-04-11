

class Member:
    def __init__(self, id, name, sex):
        self.id = id
        self.name = name
        self.sex = sex


    def getId(self):
        return self.id
    
    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def __repr__(self):
        return "%s[%d] %s" % (self.name, self.id, self.sex)

    def __str__(self):
        return "%s[%d] %s" % (self.name, self.id, self.sex)

    def __eq__(self, other):
        if other == None:
            return False
        return self.id == other.id and self.name == other.name and self.sex == other.sex