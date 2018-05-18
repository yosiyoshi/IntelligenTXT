# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:39:44 2018

@author: YosiYoshi
"""
from __future__ import unicode_literals
import sys
sys.path.append("../")

import jieba
import jieba.posseg
import jieba.analyse

import tltk.nlp as tl

import tkinter as tk

class Frame(tk.Frame):
    root = tk.Tk()
    m = tk.StringVar()

    def main():
        root = Frame.root
        m = Frame.m
        root.title('Editor')
        root.geometry("560x320")
        
        menub1 = tk.Menu(root, tearoff=0)
        root.configure(menu = menub1)
        menuf1 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(ZH)", menu=menuf1,  underline=5)
        menuf1.add_command(label=u"Segment", command=Frame.segzh, underline=5, accelerator = 'Ctrl-N')

        menuf2 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(TH)", menu=menuf2,  underline=5)
        menuf2.add_command(label=u"Segment", command=Frame.segth, underline=5, accelerator = 'Ctrl-N')
        text_widget = tk.Text(root)
        text_widget.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        root.mainloop()
#↓Unfinished work↓ 
    def segzh():
        #想获得所Frame定义的m（StringVar）内容。
        m = Frame.m
        #txt正获得m的内容而在seg命令为了启动结巴的分词系统
        txt = m.get()
        seg = "/ ".join(jieba.cut(txt, cut_all=False))
        print(seg)
        root2 = tk.Tk()
        root2.title('Result(SegmentZH)')
        label2 = tk.Label(root2,text=seg,font=16)
        label2.pack(fill="x")
        root2.mainloop()
        
    def segth():
        #想获得所Frame定义的m（StringVar）内容。
        m = Frame.m
        txt = m.get()
        seg = tl.segment(txt)
        print(seg)
        root3 = tk.Tk()
        root3.title('Result(SegmentTH)')
        label3 = tk.Label(root3,text=seg,font=16)
        label3.pack(fill="x")
        root3.mainloop()

if __name__ == '__main__':
    f = Frame()
    Frame.main()
