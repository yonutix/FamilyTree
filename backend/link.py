

class Link:

    def __init__(self, a, b, type):
        self.source = a
        self.dest = b
        self.type = type

    def getSource(self):
        return self.source

    def getDest(self):
        return self.dest

    def getType(self):
        return self.type

    def __repr__(self):
        return "Link <%s(%s) = %s)>" % (self.type, self.source, self.dest)

    def __str__(self):
        return "Link <%s(%s) = %s)>" % (self.type, self.source, self.dest)

    def __eq__(self, other):
        return self.source == other.source and self.dest == other.dest and self.type == other.type