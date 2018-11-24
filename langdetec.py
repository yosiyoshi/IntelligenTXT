# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 22:30:29 2018

@author: Yosiyoshi
"""
from main import Frame
import tkinter as tk
class LangDetec(tk.Frame):
    def main():
        root = Frame.root
        m = Frame.m
        root2 = tk.Tk()
        root2.title('Console')
        label1 = tk.Label(root,text="""Click button named "Detect" to detect the language written on your editor!""",font=16)
        label1.pack(fill="x")
        entry = tk.Entry(root,font=("",14),justify="left", textvariable=m)
        m.pack(fill="x")
        menub1 = tk.Menu(root, tearoff=0)
        root.configure(menu = menub1)
        menuf0 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"File", menu=menuf0,  underline=5)
        menuf0.add_command(label=u"New", command=Frame.new, underline=5, accelerator = 'Ctrl-N')
        menuf0.add_command(label=u"addOpen", command=Frame.load, underline=5, accelerator = 'Ctrl-O')
        menuf0.add_command(label=u"addSave", command=Frame.save, underline=5, accelerator = 'Ctrl-S')
        menuf0.add_command(label=u"eXit", command=root.destroy, underline=5, accelerator = 'Ctrl-X')
        button = tk.Button(root2,text='Detect',command=Frame.langety)
        button.grid(row=2,column=1,columnspan=2)
        entry.pack(fill="x")
        root.title('LanguageDetector')
        root.mainloop()

if __name__ == '__main__':
    LangDetec.main()