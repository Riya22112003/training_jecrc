#GUI -graphical user interface
# libraries
#############
# 1. Tkinter
# 2. PyQT
# 3. Turtle

import tkinter as ttk
app=ttk.Tk()
app.title('my app')
app.geometry('600x400')

ttk.Label(app ,text='A Simple Text Label').place(x=50,y=50)

app.mainloop()