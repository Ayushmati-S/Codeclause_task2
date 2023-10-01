import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()


def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()    

root=Tk()
root.title('Musicplayer System')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

playlist=Listbox(root,selectmode=SINGLE,bg="Navy Blue",fg="white",font=('Calibri',19),width=40)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\LENOVO\Desktop\musicccc')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="play",command=playsong)
playbtn.config(font=('Comic Sans MS',18),bg="Purple",fg="black",padx=8,pady=8)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('Comic Sans MS',18),bg="Purple",fg="Black",padx=8,pady=8)
pausebtn.grid(row=1,column=1)

Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('Comic Sans MS',18),bg="Purple",fg="Black",padx=8,pady=8)
Resumebtn.grid(row=1,column=3)

mainloop()