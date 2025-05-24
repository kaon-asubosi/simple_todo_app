import tkinter as tk
import task

def on_click():
    entry = var.get()
    task_label(entry,30)

root = tk.Tk()
root.title("My App")
root.geometry("800x600")

class task_label:
    def __init__(self,name:str,minutes:int):
        obj = task.Task(name,minutes)
        frame = tk.Frame(widgetframe,background="lightgrey",padx=10,pady=10);frame.pack()
        tk.Label(frame,text=obj.__repr__()).pack()

footer = tk.Frame(root,background="gray",height="100",width="800")

widgetframe = tk.Frame(root)
widgetframe.pack(fill="both")

var = tk.StringVar()
textform = tk.Entry(footer,textvariable=var)
formbotton = tk.Button(footer,text="Click",command=on_click)
textform.pack()
formbotton.pack()

footer.pack(side="bottom",fill="x")

task_label("料理",30)
root.mainloop()