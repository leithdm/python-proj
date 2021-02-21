from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Productivity Timer")
# add padding to the window, and change background color
window.config(padx=100, pady=50, bg=YELLOW)
# create a canvas in order to put on an image, change background color, highlightthickness
# is POORLY documented by tkinter team, but it gets rid of box around image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# need a PhotoImage to get the location of the image to place on the canvas
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# create text to display the timer
canvas.create_text(100, 130, text="00:00", fill="purple", font=(FONT_NAME, 35, "bold"))
canvas.pack()



window.mainloop()