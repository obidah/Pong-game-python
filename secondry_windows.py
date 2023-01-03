from tkinter import *
import os

def start():
    root = Tk()
    root.geometry('800x400')
    root.title('Warning')
    root.iconbitmap(os.path.join('imgs', 'favicon.ico'))
    MyButton = Button(root, text="CLICK ME TO START!!", padx=10, pady=10, command=root.destroy)
    MyLabel = Label(root,  text="WELCOME TO MY MULTIPLAYER PONG GAME!!")
    MyLabe2 = Label(root,  text="--WASD-- FOR THE TOP PLAYER")
    MyLabe3 = Label(root,  text="--ARROWS-- FOR THE BOTTOM PLAYER")
    MyLabel.pack()
    MyLabe2.pack()
    MyLabe3.pack()
    MyButton.pack()
    root.mainloop()

def player_above_won():
    root = Tk()
    root.geometry('400x50')
    root.title('Warning')
    root.iconbitmap(os.path.join('imgs', 'favicon.ico'))
    MyLabel1 = Label(root, text="TOP PLAYER WON!!")
    MyLabel1.pack()
    root.mainloop()
    
def player_bottom_won():
    root = Tk()
    root.geometry('400x50')
    root.title('Warning')
    root.iconbitmap(os.path.join('imgs', 'favicon.ico'))
    MyLabel1 = Label(root, text="BOTTOM PLAYER WON!!")
    MyLabel1.pack()
    root.mainloop()

