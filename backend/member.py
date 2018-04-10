

class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name


    def getId(self):
        return self.id
    
    def getName(self):
        return self.name

    def __repr__(self):
        return "%s[%d]" % (self.name, self.id)

    def __str__(self):
        return "%s[%d]" % (self.name, self.id)

    def __eq__(self, other):

        return self.id == other.id and self.name == other.name