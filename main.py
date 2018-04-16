from tkinter import *
from backend.member import *
from backend.link import *
from tkinter import filedialog

allMembers = [Member(0, "Alice", "F"), Member(1, "Bob", "M")]

allLinks = [Link(allMembers[0], allMembers[1], "parentOf")]

generalID = 0

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


OPTIONS = [
"parent of",
"child of"
]

GENDER_OPTIONS = [
"M",
"F"
]

window = Tk()

allLinks = infereChildOf(allLinks)

allLinks = infereParentOf(allLinks)


def onSave():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        file.write(str(len(allMembers)) + "\n")
        for member in allMembers:
            file.write(str(member.getId()) + "," + member.getName() + "," + member.getSex() + "\n")
            print(str(member.getId()) + "," + member.getName() + "," + member.getSex() + "\n")

        file.write(str(len(allLinks)) + "\n")
        for link in allLinks:
            file.write(str(link.getSource().getId()) + "," + str(link.getDest().getId()) + ","+ link.getType() + "\n")
            print(str(link.getSource().getId()) + "," + str(link.getDest().getId()) + ","+ link.getType() + "\n")
        file.close()


def onLoad():
    print("onLoad")



def onSearchMember():
    print("onSearchMember")

def onAddPCLink():
    print("onAddPCLink")


window.title("Family Tree App")
window.geometry('1280x720')

saveButton = Button(window, text="Save", command = onSave)
saveButton.grid(column=0, row=0)

loadButton = Button(window, text="Load", command = onLoad)
loadButton.grid(column=1, row = 0)



lastNameTextFieldLabel = Label(window, text="Nume")
lastNameTextFieldLabel.grid(column=0, row = 2)

nameTextField = Text(window, height=2, width=20)
nameTextField.grid(column=0, row = 3)


variable = StringVar(window)
variable.set(GENDER_OPTIONS[0])

genderType = OptionMenu(window, variable, *GENDER_OPTIONS)
genderType.grid(column=0, row = 1)

def onAddMember():
    print("onAddMember" + nameTextField.get("1.0", END))
    


addMemberButton = Button(window, text="Add member", command = onAddMember)
addMemberButton.grid(column=0, row = 4)




linkTextFieldLabel = Label(window, text="Legatura")
linkTextFieldLabel.grid(column=1, columnspan=2, row = 2)

variable = StringVar(window)
variable.set(OPTIONS[0])

linkType = OptionMenu(window, variable, *OPTIONS)
linkType.grid(column=1, columnspan=2, row = 3)


fromText = Text(window, height=2, width=20)
fromText.grid(column=1, row = 4)

toText = Text(window, height=2, width=20)
toText.grid(column=2, row = 4)


addPCLink = Button(window, text="Add PC Link", command = onAddPCLink)
addPCLink.grid(column=1, columnspan=2, row = 5)


searchIdLabel = Label(window, text="ID")
searchIdLabel.grid(column=3, row = 1)

searchIdText = Text(window, height=2, width=20)
searchIdText.grid(column=3, row = 2)

searchmemberButton = Button(window, text="Search member", command = onSearchMember)
searchmemberButton.grid(column=3, row = 3)

removeIdLabel = Label(window, text="ID to be removed member")
removeIdLabel.grid(column=4, row = 1)

removeIdText = Text(window, height=2, width=20)
removeIdText.grid(column=4, row = 2)

RemoveMemberButton = Button(window, text="Remove member", command = onSearchMember)
RemoveMemberButton.grid(column=4, row = 3)




removeLinkLabel = Label(window, text="Link to be romved")
removeLinkLabel.grid(column=5, columnspan=2, row = 1)

variable = StringVar(window)
variable.set(OPTIONS[0])

removelinkType = OptionMenu(window, variable, *OPTIONS)
removelinkType.grid(column=5, columnspan=2, row = 2)

removeParentText = Text(window, height=2, width=20)
removeParentText.grid(column=5, row = 3)

removeChildText = Text(window, height=2, width=20)
removeChildText.grid(column=6, row = 3)

removeLinkButton = Button(window, text="Remove link", command = onSearchMember)
removeLinkButton.grid(column=5, columnspan=2, row = 4)


window.mainloop()
