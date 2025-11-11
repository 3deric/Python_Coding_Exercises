import tkinter as tk

expression = ""

def key(input):
    global expression
    expression += str(input)
    output_text.config(text = expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        output_text.config(text = result)
        expression = str(result)
    except:
        output_text.config(text = "ERROR")
        expression = ""

def clear():
    global expression
    expression = ""
    output_text.config(text = expression)


if __name__ == "__main__":
    # main window
    root = tk.Tk()
    root.geometry("300x400")
    root.title("Calculator")

    # grid 4x5
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)

    display_font = ("Comic Sans MS", 25)

    output_text = tk.Label(root, relief = tk.SUNKEN, font = display_font)
    output_text.grid(column=0, row=0, columnspan = 4, sticky=tk.EW, padx = 10, pady = 10)

    button_0 = tk.Button(root, text = "0", font = display_font, command =lambda:key(0))
    button_0.grid(column = 1, row = 4)

    button_1 = tk.Button(root, text = "1", font = display_font, command = lambda:key(1))
    button_1.grid(column = 0, row = 3)

    button_2 = tk.Button(root, text = "2", font = display_font, command = lambda:key(2))
    button_2.grid(column = 1, row = 3)

    button_3 = tk.Button(root, text = "3", font = display_font, command = lambda:key(3))
    button_3.grid(column = 2, row = 3)

    button_4 = tk.Button(root, text = "4", font = display_font, command = lambda:key(4))
    button_4.grid(column = 0, row = 2)

    button_5 = tk.Button(root, text = "5", font = display_font, command = lambda:key(5))
    button_5.grid(column = 1, row = 2)

    button_6 = tk.Button(root, text = "6", font = display_font, command = lambda:key(6))
    button_6.grid(column = 2, row = 2)

    button_7 = tk.Button(root, text = "7", font = display_font, command = lambda:key(7))
    button_7.grid(column = 0, row = 1)

    button_8 = tk.Button(root, text = "8", font = display_font, command = lambda:key(8))
    button_8.grid(column = 1, row = 1)
    
    button_9 = tk.Button(root, text = "9", font = display_font, command = lambda:key(9))
    button_9.grid(column = 2, row = 1)

    button_clear = tk.Button(root, text = "C", font = display_font, command = clear)
    button_clear.grid(column = 3, row = 1)

    button_add = tk.Button(root, text = "+", font = display_font, command = lambda:key("+"))
    button_add.grid(column = 3, row = 2)

    button_sub = tk.Button(root, text = "-", font = display_font, command = lambda:key("-"))
    button_sub.grid(column = 3, row = 3)

    button_mult = tk.Button(root, text = "x", font = display_font, command = lambda:key("*"))
    button_mult.grid(column = 0, row = 4)
    
    button_div = tk.Button(root, text = "/", font = display_font, command = lambda:key("/"))
    button_div.grid(column = 2, row = 4)

    button_return = tk.Button(root, text = "=", font = display_font, command=calculate)
    button_return.grid(column = 3, row = 4)

    root.mainloop()