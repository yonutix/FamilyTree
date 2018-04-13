from backend.member import *
from gui.guimember import *
import queue

class GUISupport:
    WIDTH = 50
    HEIGHT = 30
    HSPACE = 20
    VSPACE = 20

    MIN_HOFFSET = 2000
    MIN_VOFFSET = 2000

    def __init__(self, contextMembers, contextLinks):
        self.leafs = []
        self.graph = []
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

                if(current.getX() < GUISupport.MIN_HOFFSET):
                    GUISupport.MIN_HOFFSET = current.getX()

                if(current.getY() < GUISupport.MIN_VOFFSET):
                    GUISupport.MIN_VOFFSET = current.getY()

                m = GUISupport.getParent(current.getMember(), links, "M")
                f = GUISupport.getParent(current.getMember(), links, "F")

                if not m == None:
                    guiM = GUIMember(m, None, None)

                    guiM.setX(currentLeaf.getX() - GUISupport.WIDTH/2 - GUISupport.HSPACE/2)
                    guiM.setY(currentLeaf.getY() - GUISupport.VSPACE - GUISupport.HEIGHT)
                    current.setMother(guiM)
                    q.put(guiM)

                if not f == None:
                    guiF = GUIMember(f, None, None)
                    guiF.setX(currentLeaf.getX() + GUISupport.WIDTH/2 + GUISupport.HSPACE/2)
                    guiF.setY(currentLeaf.getY() - GUISupport.VSPACE - GUISupport.HEIGHT)
                    current.setMother(guiF)
                    q.put(guiF)

            self.leafs = self.leafs + [currentLeaf]
            GUISupport.MIN_HOFFSET -= 1
            GUISupport.MIN_VOFFSET -= 1
            print("addMember\n")
            GUISupport.printLeafs(currentLeaf)


    def drawGraph(self, canvas):

        for leaf in self.leafs:
            q = queue.Queue()
            q.put(leaf)
            while not q.empty():
                current = q.get()
                canvas.create_rectangle(-GUISupport.MIN_HOFFSET + current.getX(), 
                    -GUISupport.MIN_VOFFSET + current.getY(),
                    -GUISupport.MIN_HOFFSET + current.getX() + GUISupport.WIDTH,
                    -GUISupport.MIN_VOFFSET + current.getY() + GUISupport.HEIGHT,
                    fill='red')

                canvas.create_text(-GUISupport.MIN_HOFFSET + current.getX() + 10,
                    -GUISupport.MIN_VOFFSET + current.getY() + 10,
                    fill="black",
                    font="Arial 10",
                    text=current.getMember().getId())

                f = current.getMother()
                m = current.getFather()
            
                if not f == None:
                    '''
                    canvas.create_line(-GUISupport.MIN_HOFFSET + current.getX() + GUISupport.WIDTH/2,
                        -GUISupport.MIN_VOFFSET + current.getY(),
                        -GUISupport.MIN_HOFFSET + current.getX() + GUISupport.WIDTH/2,
                        -GUISupport.MIN_VOFFSET + current.getY() - GUISupport.VSPACE/2)

                    canvas.create_line(-GUISupport.MIN_HOFFSET + current.getX() + GUISupport.WIDTH/2,
                        -GUISupport.MIN_VOFFSET + current.getY() - GUISupport.VSPACE/2,
                        -GUISupport.MIN_HOFFSET + f.getX() + GUISupport.WIDTH/2,
                        -GUISupport.MIN_VOFFSET + current.getY() - GUISupport.VSPACE/2)

                    canvas.create_line(-GUISupport.MIN_HOFFSET + f.getX() + GUISupport.WIDTH/2,
                        -GUISupport.MIN_VOFFSET + current.getY() - GUISupport.VSPACE,
                        -GUISupport.MIN_HOFFSET + f.getX() + GUISupport.WIDTH/2,
                        -GUISupport.MIN_VOFFSET + current.getY() - GUISupport.VSPACE/2)
                    '''
                    q.put(f)
                if not m == None:
                    q.put(m)
                
        #print(self.leafs)
            