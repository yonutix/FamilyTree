

class Member:
    def __init__(self, id, name, gender, firstName):
        self.id = id
        self.name = name
        self.gender = gender
        self.firstName = firstName

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getFirstName(self):
        return self.firstName

    def __repr__(self):
        return "%s[%d] %s" % (self.name, self.id, self.gender)

    def __str__(self):
        return "%s[%d] %s" % (self.name, self.id, self.gender)

    def __eq__(self, other):
        if other == None:
            return False
        return self.id == other.id and self.name == other.name and self.sex == other.sex