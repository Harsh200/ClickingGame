from tkinter import *
from random import randint
from threading import Timer



def newGame():
    global time,score
    print("New Game")
    time=10
    score=0
    clickMe.place(x=windowWidth/2,y=windowHeight/2)
    timer()




def clicked():
    global score
    score+=1
    clickMe.place(x=randint(buttonWidth,windowWidth-buttonWidth),y=randint(buttonHeight,windowHeight-buttonHeight))
    mainMenu.entryconfigure(3,label="Score= "+str(score))






def timer():
    global time
    if time ==0:
        clickMe.place_forget()
        return
    time-=1





window=Tk()
time=10
score=0
windowWidth=600
windowHeight=600
buttonWidth=80
buttonHeight=80
window.geometry(str(windowWidth)+"x"+str(windowHeight))

mainMenu=Menu(window)
window.config(menu=mainMenu)
mainMenu.add_command(label="New Game",command=newGame)
mainMenu.add_separator()
mainMenu.add_command(label="Score=0")
mainMenu.add_separator()
mainMenu.add_command(label="Time= "+str(time)+"s")
clickMe=Button(window,text="Click Me!",
               bg="Green",fg="White",padx=buttonWidth/2,pady=buttonHeight/2,command=clicked)
clickMe.place(x=windowWidth/2,y=windowHeight/2)


window.mainloop()
