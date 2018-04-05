from tkinter import *
 
window = Tk()
 
window.title("Family Tree App")
window.geometry('1280x720')
saveButton = Button(window, text="Save")
saveButton.grid(column=0, row=0)

loadButton = Button(window, text="Load")
loadButton.grid(column=1, row = 0)

addMemberButton = Button(window, text="Add member")
addMemberButton.grid(column=2, row = 0)

editMemberButton = Button(window, text="Edit member")
editMemberButton.grid(column=3, row = 0)

removeMemberButton = Button(window, text="Remove member")
removeMemberButton.grid(column=4, row = 0)

searchMemberButton = Button(window, text="Search member")
searchMemberButton.grid(column=5, row = 0)

canvas = Canvas(window, bg="white", width=1270, height=690)
canvas.grid(column=0, columnspan=8, row=1)

window.mainloop()