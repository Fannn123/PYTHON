import tkinter 

windows = tkinter.Tk()

tampilan1= tkinter.Label(windows, text="email")
tampilan2 = tkinter.Label(windows, text="paspowrd")

tombol1 = tkinter.Button(windows, text="tombol1")
tombol2 = tkinter.Button(windows, text="tombol2")

tampilan1.pack()
tampilan2.pack()
tombol1.pack()
tombol2.pack()

windows.mainloop()