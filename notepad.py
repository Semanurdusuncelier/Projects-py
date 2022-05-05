from tkinter import*
from tkinter import filedialog


def save_file():
     open_file=filedialog.asksaveasfile(mode='w',defaultextension=".text")
     if open_file is None:
          return
     text=str(entry.get(1.0,END))
     open_file.write(text)
     open_file.close()

def clear():
     entry.delete(1.0,END)

def open_file ():
     file=filedialog.askopenfiles(mode='r',filetypes=[{'text files','*.txt'}])
     if file is not None:
          content=file.read()
     entry.insert(INSERT,content)

root =Tk()
root.geometry("500x600")

b1=Button(root,text="save file",command=save_file)
b1.place(x=10,y=10)

b2=Button(root,text="clear",command=clear)
b2.place(x=70,y=10)

b3=Button(root,text="open file",command=open_file)

b3.place(x=120,y=10)

entry=Text(root,height=33,width=58,wrap=WORD)
entry.place(x=10,y=50)
root.mainloop()