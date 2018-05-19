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

from pyvi import ViTokenizer, ViPosTagger

import tltk.nlp as tl

import tkinter as tk

class Frame(tk.Frame):
    root = tk.Tk()
    m = tk.StringVar()

    def main():
        root = Frame.root
        m = Frame.m
        root.title('Editor')
        root.geometry("800x25")
        
        menub1 = tk.Menu(root, tearoff=0)
        root.configure(menu = menub1)
        menuf1 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(ZH)", menu=menuf1,  underline=5)
        menuf1.add_command(label=u"Segment", command=Frame.segzh, underline=5, accelerator = 'Ctrl-S')
        menuf1.add_command(label=u"Keywords", command=Frame.kwzh, underline=5, accelerator = 'Ctrl-K')
        menuf1.add_command(label=u"POS", command=Frame.poszh, underline=5, accelerator = 'Ctrl-P')
    
        menuf2 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(TH)", menu=menuf2,  underline=5)
        menuf2.add_command(label=u"Segment", command=Frame.segth, underline=5, accelerator = 'Ctrl-S')
#        menuf2.add_command(label=u"IPA", command=Frame.ipath, underline=5, accelerator = 'Ctrl-I')
#        menuf2.add_command(label=u"Romanize", command=Frame.romth, underline=5, accelerator = 'Ctrl-R')
        menuf2.add_command(label=u"POS", command=Frame.posth, underline=5, accelerator = 'Ctrl-P')
        
        menuf3 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(VT)", menu=menuf3,  underline=5)
        menuf3.add_command(label=u"Segment", command=Frame.segvt, underline=5, accelerator = 'Ctrl-S')
        menuf3.add_command(label=u"POS", command=Frame.posvt, underline=5, accelerator = 'Ctrl-P')

        entry = tk.Entry(root,font=("",14),justify="left", textvariable=m) #entry textbox
        entry.pack(fill="x")
        root.mainloop()

    def segzh():
        m = Frame.m
        txt = m.get()
        seg = "/ ".join(jieba.cut(txt, cut_all=False))
        print(seg)
        root2 = tk.Tk()
        root2.title('Result(SegmentZH)')
        label2 = tk.Label(root2,text=seg,font=16)
        label2.pack(fill="x")
        root2.mainloop()
        
    def kwzh():
        m = Frame.m
        txt = m.get()
        root6 = tk.Tk()
        root6.title('Result(KeywordsZH)')
        for x, w in jieba.analyse.extract_tags(txt, withWeight=True):
            print('%s %s' % (x, w))
            label6 = tk.Label(root6,text='%s %s' % (x, w),font=16)
            label6.pack(fill="x")
        root6.mainloop()
        
    def poszh():
        m = Frame.m
        txt = m.get()
        words = jieba.posseg.cut(txt)
        root7 = tk.Tk()
        root7.title('Result(POS-ZH)')
        for w in words:
            print('%s %s' % (w.word, w.flag))
            label7 = tk.Label(root7,text='%s %s' % (w.word, w.flag),font=16)
            label7.pack(fill="x")
        root7.mainloop()

    def segth():
        m = Frame.m
        txt = m.get()
        seg = tl.segment(txt)
        print(seg)
        root3 = tk.Tk()
        root3.title('Result(SegmentTH)')
        label3 = tk.Label(root3,text=seg,font=16)
        label3.pack(fill="x")
        root3.mainloop()
        
#    def ipath():
#        m = Frame.m
#        txt = m.get()
#        seg = tl.th2ipa(txt)
#        print(seg)
#        root4 = tk.Tk()
#        root4.title('Result(IPA-TH)')
#        label4 = tk.Label(root4,text=seg,font=16)
#        label4.pack(fill="x")
#        root4.mainloop()
#
#    def romth():
#        m = Frame.m
#        txt = m.get()
#        seg = tl.th2roman(txt)
#        print(seg)
#        root5 = tk.Tk()
#        root5.title('Result(RomanTH)')
#        label5 = tk.Label(root5,text=seg,font=16)
#        label5.pack(fill="x")
#        root5.mainloop()
#       
    def posth():
        m = Frame.m
        txt = m.get()
        seg = tl.pos_tag(txt)
        print(seg)
        root8 = tk.Tk()
        root8.title('Result(POS-TH)')
        label8 = tk.Label(root8,text=seg,font=16)
        label8.pack(fill="x")
        root8.mainloop()
    
    def segvt():
        m = Frame.m
        txt = m.get()
        seg = ViTokenizer.tokenize(txt)
        print(seg)
        root9 = tk.Tk()
        root9.title('Result(KeywordsVT)')
        label9 = tk.Label(root9,text=seg,font=16)
        label9.pack(fill="x")
        root9.mainloop()

    def posvt():
        m = Frame.m
        txt = m.get()
        seg = ViPosTagger.postagging(ViTokenizer.tokenize(txt))
        print(seg)
        root10 = tk.Tk()
        label0 = tk.Label(root10,text=seg,font=16)
        label0.pack(fill="x")
        root10.title('Result(POS-VT)')
        root10.mainloop()

        
if __name__ == '__main__':
    f = Frame()
    Frame.main()
        seg = "/ ".join(jieba.cut(txt, cut_all=False))
        print(seg)
        root2 = tk.Tk()
        root2.title('Result(SegmentZH)')
        label2 = tk.Label(root2,text=seg,font=16)
        label2.pack(fill="x")
        root2.mainloop()
        
    def kwzh():
        m = Frame.m
        txt = m.get()
        root6 = tk.Tk()
        root6.title('Result(KeywordsZH)')
        for x, w in jieba.analyse.extract_tags(txt, withWeight=True):
            print('%s %s' % (x, w))
            label6 = tk.Label(root6,text='%s %s' % (x, w),font=16)
            label6.pack(fill="x")
        root6.mainloop()
        
#    def poszh():
#        m = Frame.m
#        txt = m.get()
#        words = jieba.posseg.cut(txt)
#        root7 = tk.Tk()
#        root7.title('Result(POS-ZH)')
#        for word, flag in words:
#            print('%s %s' % (word, flag))
#            label7 = tk.Label(root7,text='%s %s' % (word, flag),font=16)
#            label7.pack(fill="x")
#        root7.mainloop()

    def segth():
        m = Frame.m
        txt = m.get()
        seg = tl.segment(txt)
        print(seg)
        root3 = tk.Tk()
        root3.title('Result(SegmentTH)')
        label3 = tk.Label(root3,text=seg,font=16)
        label3.pack(fill="x")
        root3.mainloop()
        
#    def ipath():
#        m = Frame.m
#        txt = m.get()
#        seg = tl.th2ipa(txt)
#        print(seg)
#        root4 = tk.Tk()
#        root4.title('Result(IPA-TH)')
#        label4 = tk.Label(root4,text=seg,font=16)
#        label4.pack(fill="x")
#        root4.mainloop()
#
#    def romth():
#        m = Frame.m
#        txt = m.get()
#        seg = tl.th2roman(txt)
#        print(seg)
#        root5 = tk.Tk()
#        root5.title('Result(RomanTH)')
#        label5 = tk.Label(root5,text=seg,font=16)
#        label5.pack(fill="x")
#        root5.mainloop()
#       
    def posth():
        m = Frame.m
        txt = m.get()
        seg = tl.pos_tag(txt)
        print(seg)
        root8 = tk.Tk()
        root8.title('Result(POS-TH)')
        label8 = tk.Label(root8,text=seg,font=16)
        label8.pack(fill="x")
        root8.mainloop()
        
if __name__ == '__main__':
    f = Frame()
    Frame.main()
