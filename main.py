from tkinter import *
from backend.member import *
from backend.link import *
from tkinter import filedialog
from graphviz import Digraph
import argparse

import os

allMembers = []

allLinks = []

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
"child of",
"married to",
"divorced to",
]

GENDER_OPTIONS = [
"M",
"F"
]

styles = {
    'graph': {
        'label': 'Omnes qui',
        'labelloc': 'top',
        'fontsize': '48',
        'fontcolor': 'black',
        'bgcolor': '#f1ebb9'
    },
    'nodes': {
        'fontname': 'Courier New',
        'shape': 'rectangle',
        'fontcolor': 'black',
        'color': 'black',
    },
    'edges': {
        'color': 'white',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'black',
        'color':'black',
        'penwidth': '3',
        'arrowsize': "3"

    }
}

def onLoad(filename):
    global allMembers
    global allLinks
    global generalID

    allMembers  = []
    allLinks  = []

    file = open(filename)
    if file:
        print("Loading " + filename)
        content = file.readlines()
        content = [x.strip() for x in content] 
        memberLineCount = int(content[0])


        for i in range(memberLineCount):
            components = content[i+1].split(",")
            name = components[1]
            gender = components[2]
            firstName = components[3]
            imgSrc = components[4]
            if components[5] == "NA":
                allMembers = allMembers + [Member(generalID, name, gender, firstName, imgSrc)]
            else:
                allMembers = allMembers + [Member(generalID, name, gender, firstName, imgSrc, 
                    datetime.date(year=int(components[5]), month = int(components[6]), day = int(components[7])))]
            
            generalID = generalID + 1

        linksLineCount = int(content[memberLineCount+1])

        for i in range(linksLineCount):
            components = content[memberLineCount + 1 + i + 1].split(",")
            src = components[0]
            dest = components[1]
            t = components[2]
            if len(components) > 3:
                allLinks = allLinks + [Link(allMembers[int(src)], allMembers[int(dest)], t, components[3])]
            else:
                allLinks = allLinks + [Link(allMembers[int(src)], allMembers[int(dest)], t)]

        file.close()
    else:
        print("Could not load " + filename)

def save(file):
    if file:
        file.write(str(len(allMembers)) + "\n")
        for member in allMembers:
            dateStr = ","
            if member.getBirthDate():
                dateStr = dateStr + str(member.getBirthDate().year)
            else:
                dateStr = dateStr + "NA"
            dateStr = dateStr + ","
            if member.getBirthDate():
                dateStr = dateStr + str(member.getBirthDate().month)
            else:
                dateStr = dateStr + "NA"
            dateStr = dateStr + ","
            if member.getBirthDate():
                dateStr = dateStr +str( member.getBirthDate().day)
            else:
                dateStr = dateStr + "NA"

            file.write(str(member.getId()) + "," + member.getName() + "," + member.getGender() + "," + member.getFirstName() + "," + member.getImgSrc() + dateStr + "\n")

        file.write(str(len(allLinks)) + "\n")
        for link in allLinks:
            file.write(str(link.getSource().getId()) + "," + str(link.getDest().getId()) + ","+ link.getType() + "\n")
        file.close()


def searchByName(name):
	nameList = []
	for member in allMembers:
		if name.lower() in member.getName().lower():
			nameList.append(member)
	return nameList

def addMember(firstName, lastName, gender):

    global generalID

    global allMembers

    allMembers = allMembers + [Member(generalID, firstName, gender, lastName)]

    generalID = generalID + 1


def addLink(fromID, toID, relType):
    #TODO: sanity check
    global allLinks
    allLinks = allLinks + [Link(allMembers[int(fromID)], allMembers[int(toID)], relType)]

    allLinks = infereChildOf(allLinks)

    allLinks = infereParentOf(allLinks)

def exportDotFile(filename):
    print("Export dot file")
    f = open(filename,"w")
    f.write("digraph {\n")


    for member in allMembers:
        f.write("" + member.getLabel() +" [label=\"" + member.getFirstName() + " " + member.getName() + "\"]" ";\n")
    for link in allLinks:
        if link.getType() == "parent of":
            f.write("    " + link.getSource().getLabel() + " -> " + link.getDest().getLabel() + ";\n")

    f.write("}\n")
    f.close()

def onSaveButton():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    save(file)



def onLoadButton():
    filename = filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))

    onLoad(filename)


def onSearchMember():
    print("onSearchMember")

def onRender():
    print("Start on render")
    dot = Digraph(comment='The Round Table', engine='dot', format='png')
    dot.attr(overlap='false', fixedsize='true', lwidth='50', ranksep="4",pad="1", nodesep='2', image='tile.png', dimen='3')
    print("onRender " + str(len(allMembers)))
    
    
    for member in allMembers:
        birthDate = ""
        if member.getBirthDate():
            birthDate = str(member.getBirthDate())
        print(member.getImgSrc())
        thisLabel = '''<<TABLE BORDER="0"><TR> <TD>''' + member.getName() + " " + member.getFirstName() + "</TD></TR>"
        thisLabel = thisLabel + '''<TR> <TD><IMG SRC="''' + member.getImgSrc() + '''" /></TD> </TR>'''
        print(os.path.dirname(os.path.realpath(__file__)))
        
        thisLabel = thisLabel + '''<TR> <TD>''' + "GEN:" + member.getGender() + "<BR />B:" + birthDate + '''</TD></TR></TABLE>>'''


        dot.node(member.getLabel(), label=thisLabel)
        #print("Label:" + str(member.getLabel()) )


    dot.graph_attr.update(
    ('graph' in styles and styles['graph']) or {}
    )
    dot.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    dot.edge_attr.update(('edges' in styles and styles['edges']) or {})

    for link in allLinks:
        if link.getType() == "parent of":
            dot.edge(link.getSource().getLabel(), link.getDest().getLabel(), link.getAttr())
        if link.getType() == "married to":
            dot.edge(link.getSource().getLabel(), link.getDest().getLabel(), link.getAttr(), arrowhead='none', arrowsize='1', color='red')
        if link.getType() == "divorced to":
            dot.edge(link.getSource().getLabel(), link.getDest().getLabel(), link.getAttr(), style='dashed', arrowhead='none', arrowsize='1', color='red')

    #print(dot.source)
    

    dot.render('test-output/round-table.gv', view=True)


def onAddMemberButton():

    global generalID

    localName = str(nameTextField.get("1.0", END))
    
    localName = localName.replace("\n", "")

    firstName = str(firstNameTextField.get("1.0", END)).replace("\n", "")

    addMember(localName, firstName, genderVariable.get())
    
    nameTextField.delete('1.0', END)
    firstNameTextField.delete('1.0', END)

def onLoadPicture():
    filename = filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("jpg files","*.jpg"),("all files","*.*")))

    with open(filename) as file:
        content = file.readlines()

def onAddLink():
    print("onAddLink")
    src = int(fromText.get("1.0", END).replace("\n", ""))
    dest = int(toText.get("1.0", END).replace("\n", ""))

    addLink(src, dest, linkVariable.get())

    fromText.delete('1.0', END)
    toText.delete('1.0', END)

def startGUI():
	window = Tk()

	window.title("Family Tree App")
	window.geometry('1280x720')

	saveButton = Button(window, text="Save", command = onSaveButton)
	saveButton.grid(column=0, row=0)

	loadButton = Button(window, text="Load", command = onLoadButton)
	loadButton.grid(column=1, row = 0)

	renderButton = Button(window, text="Render", command = onRender)
	renderButton.grid(column=2, row = 0)

	lastNameTextFieldLabel = Label(window, text="Nume")
	lastNameTextFieldLabel.grid(column=0, row = 1)

	genderVariable = StringVar(window)
	genderVariable.set(GENDER_OPTIONS[0])

	genderType = OptionMenu(window, genderVariable, *GENDER_OPTIONS)
	genderType.grid(column=0, row = 2)

	nameTextField = Text(window, height=2, width=20)
	nameTextField.grid(column=0, row = 3)


	firstNameTextFieldLabel = Label(window, text="Prenume")
	firstNameTextFieldLabel.grid(column=0, row = 4)

	firstNameTextField = Text(window, height=2, width=20)
	firstNameTextField.grid(column=0, row = 5)
	    
	descriptionTextFieldLabel = Label(window, text="Descriere")
	descriptionTextFieldLabel.grid(column=0, row = 6)

	descriptionTextField = Text(window, height=8, width=20)
	descriptionTextField.grid(column=0, row = 7)

	loadPictureButton = Button(window, text="Load Picture", command = onLoadPicture)
	loadPictureButton.grid(column=0, row = 8)
	    
	addMemberButton = Button(window, text="Add member", command = onAddMemberButton)
	addMemberButton.grid(column=0, row = 12)

	linkTextFieldLabel = Label(window, text="Legatura")
	linkTextFieldLabel.grid(column=1, columnspan=2, row = 1)

	linkVariable = StringVar(window)
	linkVariable.set(OPTIONS[0])

	linkType = OptionMenu(window, linkVariable, *OPTIONS)
	linkType.grid(column=1, columnspan=2, row = 2)


	fromText = Text(window, height=2, width=20)
	fromText.grid(column=1, row = 3)

	toText = Text(window, height=2, width=20)
	toText.grid(column=2, row = 3)

	addPCLink = Button(window, text="Add Link", command = onAddLink)
	addPCLink.grid(column=1, columnspan=2, row = 4)

	searchIdLabel = Label(window, text="ID")
	searchIdLabel.grid(column=3, row = 2)

	searchIdText = Text(window, height=2, width=20)
	searchIdText.grid(column=3, row = 3)

	searchmemberButton = Button(window, text="Search member", command = onSearchMember)
	searchmemberButton.grid(column=3, row = 4)

	removeIdLabel = Label(window, text="ID to be removed member")
	removeIdLabel.grid(column=4, row = 2)

	removeIdText = Text(window, height=2, width=20)
	removeIdText.grid(column=4, row = 3)

	RemoveMemberButton = Button(window, text="Remove member", command = onSearchMember)
	RemoveMemberButton.grid(column=4, row = 4)


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



parser = argparse.ArgumentParser(description='Family tree')
parser.add_argument("--mode")

args = parser.parse_args()


if (args.mode == "cmd"):
	print("CMD mode")

	while True:
		cmd = input(">> ")
		if cmd == "exit":
			break
		elif cmd.startswith("import"):
			cmd_args = cmd.split(" ")
			print("Import: " + cmd_args[1])
			onLoad(cmd_args[1])

		elif cmd.startswith("search name"):
			cmd_args = cmd.split(" ")
			print("Search by name: " + cmd_args[2])
			resultList = searchByName(cmd_args[2])
			print(resultList)
		elif cmd.startswith("list members"):
			print(allMembers)
		elif cmd.startswith("add member"):
			cmd_args = cmd.split(" ")
			if len(cmd_args) >= 5:
				
				firstName = ""
				for i in range(2, len(cmd_args)-2):
					firstName = firstName + cmd_args[i] + " "
				addMember(firstName, cmd_args[len(cmd_args)-2], cmd_args[len(cmd_args)-1])
				print("Added " + str(allMembers[len(allMembers)-1]))
			else :
				print("add member <first name> <last name> <gender>")
		elif cmd.startswith("add link"):
			cmd_args = cmd.split(" ")
			if len(cmd_args) < 5:
				print("add link <start id> <parent of> <end id>")
			else:
				addLink(cmd_args[2], cmd_args[5], cmd_args[3] + " " + cmd_args[4])
				print("Added " + str(allLinks[len(allLinks)-1]))
		elif cmd.startswith("export dot"):
			cmd_args = cmd.split(" ")
			if len(cmd_args) == 2:
				exportDotFile("Untitled.dot")
			else:
				exportDotFile(cmd_args[2])
		elif cmd.startswith("save db"):
			cmd_args = cmd.split(" ")
			if len(cmd_args) == 2:
				save(open("Untitled_db.txt","w"))
			else:
				save(open(cmd_args[2], "w"))
		else:
			print("Unknown command")

	sys.exit(0)
elif (args.mode == "gui"):
	startGUI()
