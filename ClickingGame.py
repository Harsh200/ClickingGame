from tkinter import *

window=Tk()
time=10
score=0
windowWidth=600
windowHeight=600
window.geometry(str(windowWidth)+"x"+str(windowHeight))

mainMenu=Menu(window)
window.config(menu=mainMenu)
mainMenu.add_command(label="New Game",command=newGame)


window.mainloop()
