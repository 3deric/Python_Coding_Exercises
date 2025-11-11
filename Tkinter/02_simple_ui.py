import tkinter as tk

enabled = False

def say_hello():
    global enabled
    if enabled == False:
        enabled = True
    else:
        enabled = False
    label.config(text = str(enabled))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hello World")
    root.geometry("400x300")

    label = tk.Label(root, 
                    text = str(enabled),
                    bg = "yellow",
                    font = ("Verdana", 15),
                    wraplength = 100,
                    justify = "center")
    label.pack(padx = "20", pady = "20")

    button = tk.Button(root,
                       text = "Set",
                       command = say_hello)

    button.pack()
    root.mainloop()


