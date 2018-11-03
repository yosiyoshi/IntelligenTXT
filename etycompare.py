# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 22:30:29 2018

@author: Yosiyoshi
"""
import re
from main_mini import Frame
from ynltk import OmnibusStem
import tkinter as tk
import pyperclip
class LangDetec(tk.Frame):
    root = Frame.root
    m = Frame.m
    n = tk.StringVar()
    def main():
        root = LangDetec.root
        m = LangDetec.m
        n = LangDetec.n
        root3 = Frame.root
        entry = Frame.entry
        entry2 = tk.Entry(root3,font=("",14),justify="left", textvariable=n)
        root2 = tk.Tk()
        root2.title('Console')
        label1 = tk.Label(root,text="""Fill two entries with any words to compare and click button named "Compare" to calculate the similarity in the etymology!""",font=16)
        label1.pack(fill="x")
        menub1 = tk.Menu(root, tearoff=0)
        root.configure(menu = menub1)
        menuf0 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"File", menu=menuf0,  underline=5)
        menuf0.add_command(label=u"eXit", command=root.destroy, underline=5, accelerator = 'Ctrl-X')
        button = tk.Button(root2,text='Compare',command=LangDetec.compare)
        button.grid(row=2,column=1,columnspan=2)
        entry.pack(fill="x")
        entry2.pack(fill="x")
        root.title('EtymologyCompare')
        root.mainloop()
    def compare():
        m = LangDetec.m
        n = LangDetec.n
        txt1 = re.sub(' ', '', m.get())
        txt2 = re.sub(' ', '', n.get())
        s=OmnibusStem()
        result = s.compStemmer(txt1,txt2)
        print(result)
        pyperclip.copy(result)
        root2 = tk.Tk()
        root2.title('Result')
        label2 = tk.Label(root2,text=result,font=16)
        label2.pack(fill="x")
        root2.mainloop()

if __name__ == '__main__':
    LangDetec.main()