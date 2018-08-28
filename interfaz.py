import tkinter
from tkinter import ttk
import sys

def demo():
    #root = tk.Tk()
    schedGraphics = tkinter
    root = schedGraphics.Tk()
    root.geometry("900x500")
    root.title("Proxy")
    universal_height = 606
	
    style = ttk.Style()
    font10 = "-family {DejaVu Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0"
    style.theme_create( "yummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] }, "foreground": "white" },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": "#aaa", "foreground": "white", "font":font10},
            "map":       {"background": [("selected", "#222")] } } } )
	
    if sys.platform == "win32":
        style.theme_use('winnative')
    else:
        style.theme_use("yummy")
    style.theme_use("yummy")
    nb = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb, width= 900,height = universal_height)
    # second page
    page2 = ttk.Frame(nb,width = 900,height = universal_height)
    # third page
    page3 = ttk.Frame(nb,width = 900,height = universal_height)

    nb.add(page1, text='History')
    nb.add(page2, text='Repeater')
    nb.add(page3, text='Info')
    nb.grid(column=0)

    day_label = schedGraphics.Label(page1, text="HTTP History")
    day_label.pack()
    day_label.place(x=10, y=10)

    day_label = schedGraphics.Label(page2, text="Request/Response")
    day_label.pack()
    day_label.place(x=10, y=10)
    
    day_label = schedGraphics.Label(page3, text="Site Information")
    day_label.pack()
    day_label.place(x=10, y=10)
    root.mainloop()

if __name__ == "__main__":
    demo()
