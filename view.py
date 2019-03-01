
from tkinter import Tk, Entry, W, E, N, S, PhotoImage, Checkbutton, Button, Radiobutton, \
        Menu, Frame, Label, LEFT, RIGHT, TOP, BOTTOM, NW, NE, SW, CENTER

import tkinter as tk
root = Tk()

FONT_SIZE_LARGE = 14
FONT_SIZE_NORMAL = 12
FONT_SIZE_SMALL = 8

FONT_NAME_LARGE = 'TkDefaultFont'
FONT_NAME_NORMAL = 'TkDefaultFont'
FONT_NAME_SMALL = 'TkDefaultFont'

class View:
    def __init__(self, root):
        #Frame.__init__(self, root)
        button1 = Button(root, text="Quit", command=root.quit, anchor=W)
        #button1.pack()

    frame = Frame(root,bg="red")
    """
    if we use frame = Frame(root,bg="red", width=500, height = 100).pack() instead then frame will get 
    a value of Frame wich is not packed. As a result anything likeLabel(frame, text="hello", anchor=W, bg="green").pack()
    will not give proper result 
    
    """
    frame.pack(fill="x")

    padX = 200
    left = Frame(frame, bg="yellow")
    left.pack(side=LEFT, padx=(padX,0))

    right = Frame(frame, bg="yellow")
    right.pack(side=RIGHT, padx=(0, padX))

    frame.pack(fill="x")
    label1 = Label(left, text="hello", font=(FONT_NAME_LARGE, FONT_SIZE_LARGE), anchor=W, bg="green")
    label1.pack(pady=(50,50))


    label2 = Label(right, text="hello", font=(FONT_NAME_LARGE, FONT_SIZE_LARGE), anchor=W, bg="green")
    label2.pack(pady=(50,50))

    Button(text="Next").pack(side=TOP, anchor=CENTER)

    control = Frame(root, bg="cyan")

    control.pack(fill="x", side=BOTTOM)

    padX = 200
    reload = Frame(control)
    reload.pack(side = LEFT, padx=(padX,0))

    group = Frame(reload)
    group.pack(side = LEFT)

    v = tk.IntVar()
    v.set(1)
    Radiobutton(group, text="Python", padx=20, variable=v, value=1).pack(anchor=W)
    Radiobutton(group, text="Perl", padx=20, variable=v, value=2).pack(anchor=W)

    reloadBtn = Button(reload, text="Reload", anchor=W, bg="green").pack(side=RIGHT, anchor=CENTER)


    Button(control, text="Quit", command=root.quit).pack(side=RIGHT, padx=(0,100))

    #button = Button(frame, text="click me", side=RIGHT).pack()

def run():
    #SCREEN_WIDTH = root.winfo_screenwidth()
    #SCREEN_HEIGHT = root.winfo_screenheight()

    root.geometry("%dx%d" % (640, 380))

    root.configure(background="WHITE")

    root.resizable(False, False)

    root.title("Word Checker")

    View(root)


    root.bind("<Key>", key)

    root.mainloop()




#    print('Exiting main program')


def key(event):
    print("pressed", repr(event.char))
    if event.char == 'q' or event.char == 'Q' or event.char == chr(27):
        root.quit()


if __name__ == '__main__':
    run()



