
from tkinter import *


mainWindow = Tk() # Tk() is a constructor for the main window
# thelabel = Label(frame, text="this is a text") # Label constructor
# thelabel.pack() # pack will find an available spot and put the label in the frame so you can see it
topPanel = Frame(mainWindow) # frame is like a panel; small windows inside of the main window
topPanel.pack()
bottomPanel = Frame(mainWindow)
bottomPanel.pack(side=BOTTOM)

button1 = Button(topPanel, text="Button 1", fg="red")
button2 = Button(topPanel, text="Button 2", fg="blue")
button3 = Button(topPanel, text="Button 3", fg="green")
button4 = Button(bottomPanel, text="Button 4", fg="purple")

button1.pack() # pack by default will put items on top of the next item
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

mainWindow.mainloop()
''' This will put the frame window into an infinite print window loop
without this the gui will display once and disappear
'''