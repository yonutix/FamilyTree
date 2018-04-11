from tkinter import *
from backend.member import *
from backend.link import *
from gui.gui import *

allMembers = [Member(0, "Alice", "F"), Member(1, "Bob", "M")]

allLinks = [Link(allMembers[0], allMembers[1], "parentOf")]

def infereChildOf(links):
    for link in links:
        if link.getType() == "parentOf":
            if not Link(link.getDest(), link.getSource(), "childOf") in links:
                links = links + [Link(link.getDest(), link.getSource(), "childOf")]
    return links

def infereParentOf(links):
    for link in links:
        if link.getType() == "childOf":
            if not Link(link.getDest(), link.getSource(), "parentOf") in links:
                links = links + [Link(link.getDest(), link.getSource(), "parentOf")]
    return links



def onSave():
    print("onSave")

def onLoad():
    print("onLoad")

def onAddMember():
    print("onAddMember")

def onSearchMember():
    print("onSearchMember")


window = Tk()

allLinks = infereChildOf(allLinks)

allLinks = infereParentOf(allLinks)

print(allLinks)

#
gui = GUISupport(allMembers, allLinks)
for member in allMembers:
    gui.addMember(member, allLinks)
 
window.title("Family Tree App")
window.geometry('1280x720')

saveButton = Button(window, text="Save", command = onSave)
saveButton.grid(column=0, row=0)

loadButton = Button(window, text="Load", command = onLoad)
loadButton.grid(column=1, row = 0)

addMemberButton = Button(window, text="Add member", command = onAddMember)
addMemberButton.grid(column=2, row = 0)

searchmemberButton = Button(window, text="Search member", command = onSearchMember)
searchmemberButton.grid(column=3, row = 0)

canvas = Canvas(window, bg="white", width=1270, height=690)
canvas.grid(column=0, columnspan=8, row=1)

window.mainloop()
