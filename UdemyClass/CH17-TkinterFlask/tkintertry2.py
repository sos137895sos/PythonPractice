import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()


def hello():
    label = tk.Label(root, text="Hello World!", fg='green',
                     font=('helvetica', 20, 'bold'))
    canvas.create_window(150, 200, window=label)


button = tk.Button(text="Click Me!", fg='black', command=hello)
canvas.create_window(250, 250, window=button)

root.mainloop()
