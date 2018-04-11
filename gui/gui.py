from backend.member import *
from gui.guimember import *
import queue

class GUISupport:
    def __init__(self, contextMembers, contextLinks):
        self.leafs = []
        self.contextMembers = contextMembers
        self.contextLinks = contextLinks



    def getChildren(member, links):
        result = []
        for link in links:
            if link.getType() == "childOf":
                if link.getSource() == member:
                    result = result + [link.getDest()]
        return result

    def getParent(member, links, sex):
        for link in links:
            if link.getType() == "childOf" and link.getDest() == member:
                if link.getSource().getSex() == sex:
                    return link.getSource()

        return None


    def printLeafs(leaf):
        print("Tree")
        q = queue.Queue()
        q.put(leaf)

        while not q.empty():
            current = q.get()
            print(current)
            if not current.getMother() == None:
                q.put(current.getMother())
            if not current.getFather() == None:
                q.put(current.getFather())
        


    def addMember(self, member, links):
        if len(GUISupport.getChildren(member, self.contextLinks)) == 0:

            currentLeaf = GUIMember(member, None, None)
            

            m = GUISupport.getParent(currentLeaf.getMember(), links, "M")
            f = GUISupport.getParent(currentLeaf.getMember(), links, "F")

            q = queue.Queue()

            q.put(currentLeaf)

            while not q.empty():
                current = q.get()

                m = GUISupport.getParent(current.getMember(), links, "M")
                f = GUISupport.getParent(current.getMember(), links, "F")

                if not m == None:
                    guiM = GUIMember(m, None, None)
                    current.setMother(guiM)
                    q.put(guiM)

                if not f == None:
                    guiF = GUIMember(f, None, None)
                    current.setMother(guiF)
                    q.put(guiF)

            self.leafs = self.leafs + [currentLeaf]

            GUISupport.printLeafs(currentLeaf)

        

        #print(self.leafs)
            