from tkinter import*
from time import strftime
def time():
    samay=strftime("%H:%M:%S %p\n%d/%m/%Y\n%A")
    label.config(text=samay)
    label.after(450,time)
    
window=Tk()
window.title("clock")
window.config(background='black')
label=Label(window,font=('arial',80),background='black',foreground="#005018")
label.pack(side='top',expand=True,fill=X)
time()
mainloop()