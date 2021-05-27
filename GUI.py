from tkinter import *


class GUI():
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.quitButton = Button(frame, text='Quit', command=frame.quit)
        self.quitButton.pack(side=RIGHT)


root = Tk()
myGUI = GUI(root)
root.title('Application')
root.mainloop()
