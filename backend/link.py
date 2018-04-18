

class Link:

    def __init__(self, a, b, t):
        self.source = a
        self.dest = b
        self.t = t

    def getSource(self):
        return self.source

    def getDest(self):
        return self.dest

    def getType(self):
        return self.t

    def __repr__(self):
        return "Link <%s(%s) = %s)>" % (self.t, self.source, self.dest)

    def __str__(self):
        return "Link <%s(%s) = %s)>" % (self.t, self.source, self.dest)

    def __eq__(self, other):
        return self.source == other.source and self.dest == other.dest and self.t == other.t