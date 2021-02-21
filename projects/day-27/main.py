# import tkinter
# easier to import the entire tkinter in this example as using a lot of classes
from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500, height=300)
my_label = Label(text="Label", font=("Arial", 24, "bold"))

# label will not show without being 'packed' onto the screen
# my_label.pack(side="left") #side lets you position the label
my_label.pack()


# reconfiguring
my_label["text"] = "New label text"
# can reconfigure using .config (very useful for lots of configurations at same time)
my_label.config(text="New label text, again")

# buttons
# command is the name of the function to be invoked
def button_clicked():
    # get the text from the input, and display it as the label
    input_text = input.get()
    my_label["text"] = input_text


button = Button(text="Click Me", command=button_clicked)
# pack onto the screen in order to display it
button.pack()
# getting the button to work requires an event-listener

# Entry i.e input
input = Entry(width=10)
input.pack()



# required to keep the window open
window.mainloop()