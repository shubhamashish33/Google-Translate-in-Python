from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# main logic


def translate(text='type', src='English', dest='Hindi'):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text


def getData():
    s = src_combo.get()
    d = dstn_combo.get()
    msg = SrcTxt.get(1.0, END)
    getText = translate(text=msg, src=s, dest=d)
    DstnTxt.delete(1.0, END)
    DstnTxt.insert(END, getText)


# div placement
root = Tk()

root.title("Google Translator with Python")
root.geometry("500x700")
root.config(bg='white')

labeltxt = Label(root, text='Translate With Python', font=(
    "Poppins", 20), bg='white', fg='black')
labeltxt.place(x=100, y=40, height=40, width=300)

frame = Frame(root).pack(side=BOTTOM)

# source label
labeltxt = Label(root, text='Source Text', font=(
    "Poppins", 20), bg='white', fg='black')
labeltxt.place(x=100, y=100, height=20, width=300)


# source textBox
SrcTxt = Text(frame, font=("Poppins", 20), wrap=WORD)
SrcTxt.place(x=10, y=130, height=100, width=480)

list_text = list(LANGUAGES.values())

# source combo box
src_combo = ttk.Combobox(frame, values=list_text)
src_combo.place(x=10, y=300, height=30, width=150)
src_combo.set("english")

# button
buttonChange = Button(frame, text='Translate', relief=RAISED, command=getData)
buttonChange.place(x=170, y=300, height=30, width=150)

# destination combo box
dstn_combo = ttk.Combobox(frame, values=list_text)
dstn_combo.place(x=330, y=300, height=30, width=150)
dstn_combo.set("english")

# destination label
labeltxt = Label(root, text='Destination Text', font=(
    "Poppins", 20), bg='white', fg='black')
labeltxt.place(x=100, y=360, height=20, width=300)


# destination textBox
DstnTxt = Text(frame, font=("Poppins", 20), wrap=WORD)
DstnTxt.place(x=10, y=400, height=100, width=480)

root.mainloop()
