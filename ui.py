import tkinter as tk
import task

root = tk.Tk()
root.title("My App")
root.geometry("800x600")

class task_label:
    def __init__(self,name:str,minutes:int):
        obj = task.Task(name,minutes)
        frame = tk.Frame(widgetframe,background="lightgrey",padx=10,pady=10);frame.pack()
        tk.Label(frame,text=obj.__repr__()).pack()
side_frame = tk.Frame(root,background="lightgray",width="150")
side_frame.pack(side="left",fill="y")

footer = tk.Frame(root,background="gray",height="100",width="800")
footer.pack(side="bottom",fill="x")

widgetframe = tk.Frame(root)
widgetframe.pack(fill="both")

task_label("料理",30)
root.mainloop()