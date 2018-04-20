

class Link:

    def __init__(self, a, b, t, attr = ""):
        self.source = a
        self.dest = b
        self.t = t
        self.attr = attr

    def getSource(self):
        return self.source

    def getDest(self):
        return self.dest

    def getType(self):
        return self.t

    def getAttr(self):
        return self.attr
        
    def __repr__(self):
        return "Link <%s(%s) = %s)>" % (self.t, self.source, self.dest)

    def __str__(self):
        return "Link <%s(%s) = %s)>" % (self.t, self.source, self.dest)

    def __eq__(self, other):
        return self.source == other.source and self.dest == other.dest and self.t == other.t