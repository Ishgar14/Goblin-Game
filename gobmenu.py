from tkinter import *
from tkinter.font import Font

core = Tk()
core.title("My Game")
core.geometry("250x150")

def start():
    import goblin
    goblin.start()

title1 = Label(core, text="WELCOME TO ")
title2 = Label(core, text="RUN RUN RUN", underline = True)
instructions = Label(core,text= "Can you outrun the goblin?")
start_btn = Button(core, text="Start", command=start)
exit_btn = Button(core, text="Exit", command=lambda:exit(0))

f = Font(title2, title2.cget("font"))
f.configure(underline=True)
title2.configure(font=f)

title1.pack()
title2.pack()
instructions.pack()
start_btn.pack()
exit_btn.pack()

core.mainloop()
