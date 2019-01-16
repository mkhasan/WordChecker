
from tkinter import Tk, Entry, W, E, N, S, PhotoImage, Checkbutton, Button, \
        Menu, Frame, Label

root = Tk()


class View:
    def __init__(self, root):
        button1 = Button(root, text="Quit", command=root.quit, anchor=W)
        button1.pack()

def run():
    #SCREEN_WIDTH = root.winfo_screenwidth()
    #SCREEN_HEIGHT = root.winfo_screenheight()

    root.geometry("%dx%d" % (640, 480))

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



