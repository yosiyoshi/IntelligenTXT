#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:39:44 2018

@author: YosiYoshi
"""
from __future__ import unicode_literals

import tkinter.filedialog as tkfd
import sys
sys.path.append("../")
import re

import pyperclip

import pythainlp as ptn

import jieba
import jieba.posseg
import jieba.analyse

import logging

from pyvi import ViTokenizer, ViPosTagger

import tltk.nlp as tl

import tkinter as tk

from myanmar import converter
from myanmar.romanizer import romanize, IPA

from janome.tokenizer import Tokenizer

import collections

from gensim.models import word2vec

from isanlp.pipeline_common import PipelineCommon
from isanlp.ru.processor_tokenizer_ru import ProcessorTokenizerRu
from isanlp.processor_sentence_splitter import ProcessorSentenceSplitter
from isanlp.ru.processor_mystem import ProcessorMystem

import cyrtranslit

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

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
        menuf0 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"File", menu=menuf0,  underline=5)
        menuf0.add_command(label=u"Save", command=Frame.save, underline=5, accelerator = 'Ctrl-S')

        menuf4 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"Gensim", menu=menuf4,  underline=5)
        menuf4.add_command(label=u"Word2vec", command=Frame.w2v, underline=5, accelerator = 'Ctrl-W') 
        
        menub1.add_cascade(label=u"NLP(ZH)", menu=menuf1,  underline=5)
        menuf1.add_command(label=u"Segment", command=Frame.segzh, underline=5, accelerator = 'Ctrl-S')
        menuf1.add_command(label=u"Keywords", command=Frame.kwzh, underline=5, accelerator = 'Ctrl-K')
        menuf1.add_command(label=u"textRank", command=Frame.trzh, underline=5, accelerator = 'Ctrl-R')
        menuf1.add_command(label=u"P.o.s.", command=Frame.poszh, underline=5, accelerator = 'Ctrl-P')
        menuf1.add_command(label=u"preprocess4textrank", command=Frame.process4txtrkzh, underline=5)
    
        menuf2 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(TH)", menu=menuf2, underline=5)
        menuf2.add_command(label=u"Segment", command=Frame.segth, underline=5, accelerator = 'Ctrl-S')
        menuf2.add_command(label=u"DeepCut", command=Frame.dsegth, underline=5, accelerator = 'Ctrl-D')
        menuf2.add_command(label=u"Romanize", command=Frame.romth, underline=5, accelerator = 'Ctrl-R')
        menuf2.add_command(label=u"Keywords", command=Frame.kwth, underline=5, accelerator = 'Ctrl-K')
        menuf2.add_command(label=u"P.o.s.", command=Frame.posth, underline=5, accelerator = 'Ctrl-P')
        menuf2.add_command(label=u"sUmmary", command=Frame.sumth, underline=5, accelerator = 'Ctrl-U')
        menuf2.add_command(label=u"sentiMent", command=Frame.senth, underline=5, accelerator = 'Ctrl-M')
        menuf2.add_command(label=u"speLL(word)", command=Frame.splth, underline=5, accelerator = 'Ctrl-L')

        menuf5 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(JP)", menu=menuf5, underline=5)
        menuf5.add_command(label=u"Segment", command=Frame.segjp, underline=5, accelerator = 'Ctrl-S')
        menuf5.add_command(label=u"Counter", command=Frame.cntjp, underline=5, accelerator = 'Ctrl-C')
        menuf5.add_command(label=u"P.o.s.", command=Frame.tokenjp, underline=5, accelerator = 'Ctrl-P')
        
        menuf8 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(Bahasa)", menu=menuf8, underline=5)
        menuf8.add_command(label=u"Katadasar", command=Frame.katadsr, underline=5, accelerator = 'Ctrl-K')

        menuf3 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(VT)", menu=menuf3,  underline=5)
        menuf3.add_command(label=u"Segment", command=Frame.segvt, underline=5, accelerator = 'Ctrl-S')
        menuf3.add_command(label=u"P.o.s.", command=Frame.posvt, underline=5, accelerator = 'Ctrl-P')

        menuf4 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(MN)", menu=menuf4,  underline=5)
        menuf4.add_command(label=u"Romanize", command=Frame.rommn, underline=5, accelerator = 'Ctrl-R')
        menuf4.add_command(label=u"enco2Unicord", command=Frame.zaw2uni, underline=5, accelerator = 'Ctrl-U')
        menuf4.add_command(label=u"enco2Zawgyi", command=Frame.uni2zaw, underline=5, accelerator = 'Ctrl-Z')

        menuf7 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(RU)", menu=menuf7,  underline=5)
        menuf7.add_command(label=u"Segment&pos", command=Frame.rs, underline=5, accelerator = 'Ctrl-S')
        menuf7.add_command(label=u"cyrillic2Latin", command=Frame.c2l, underline=5, accelerator = 'Ctrl-L')
        menuf7.add_command(label=u"latin2Cyrillic", command=Frame.l2c, underline=5, accelerator = 'Ctrl-C')

        menuf6 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"Text processing", menu=menuf6,  underline=5)
        menuf6.add_command(label=u"deleteDigit", command=Frame.dd, underline=5, accelerator = 'Ctrl-D')
        menuf6.add_command(label=u"deleteBreaks", command=Frame.db, underline=5, accelerator = 'Ctrl-B')
        menuf6.add_command(label=u"deleteSpace", command=Frame.ds, underline=5, accelerator = 'Ctrl-S')
        menuf6.add_command(label=u"Paragraphs", command=Frame.para, underline=5, accelerator = 'Ctrl-P')
        
        entry = tk.Entry(root,font=("",14),justify="left", textvariable=m) #entry textbox
        entry.pack(fill="x")
        root.mainloop()

    def save():
        fn = tkfd.asksaveasfilename()
        m = Frame.m
        f = open(fn, 'a')
        f.write(m.get())
        f.close()

    def segzh():
        m = Frame.m
        txt = m.get()
        seg = "/ ".join(jieba.cut(txt, cut_all=False))
        print(seg)
        pyperclip.copy(" ".join(jieba.cut(txt, cut_all=False)))
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
        
    def trzh():
        m = Frame.m
        txt = m.get()
        root25 = tk.Tk()
        root25.title('Result(TextrankZH')
        for x, w in jieba.analyse.textrank(txt, withWeight=True):
            print('%s %s' % (x, w))
            label25 = tk.Label(root25, text='%s %s' % (x, w),font=16)
            label25.pack(fill="x")
        root25.mainloop()
        
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
        seg1 = tl.segment(txt)
        seg = seg1.replace('<s/>', "").replace('<u/>', "").replace('|', " ")
        print(seg1)
        pyperclip.copy(seg)
        root3 = tk.Tk()
        root3.title('Result(SegmentTH)')
        label3 = tk.Label(root3,text=seg,font=16)
        label3.pack(fill="x")
        root3.mainloop()

    def romth():
        m = Frame.m
        txt = m.get()
        seg = ptn.romanization(txt,engine='royin')
        print(seg)
        pyperclip.copy(seg)
        root5 = tk.Tk()
        root5.title('Result(RomanTH)')
        label5 = tk.Label(root5,text=seg,font=16)
        label5.pack(fill="x")
        root5.mainloop()
       
    def posth():
        m = Frame.m
        txt = m.get()
        seg = tl.pos_tag(txt)
        print(seg)
#        pyperclip.copy(" ".join(seg))
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
        pyperclip.copy(seg)
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
#        pyperclip.copy(" ".join(seg))
        root10 = tk.Tk()
        label0 = tk.Label(root10,text=seg,font=16)
        label0.pack(fill="x")
        root10.title('Result(POS-VT)')
        root10.mainloop()
        
    def sumth():
        m = Frame.m
        txt = m.get()
        seg = ptn.summarize.summarize_text(txt,n=1,engine='frequency')
        print(seg)
        pyperclip.copy(" ".join(seg))
        root11 = tk.Tk()
        label1 = tk.Label(root11,text=seg,font=16)
        label1.pack(fill="x")
        root11.title('Result(SummaryTH)')
        root11.mainloop()

    def dsegth():
        m = Frame.m
        txt = m.get()
        seg = ptn.word_tokenize(txt,engine='deepcut')
        print(seg)
        pyperclip.copy(" ".join(seg))
        root12 = tk.Tk()
        root12.title('Result(DeepCutTH)')
        label12 = tk.Label(root12,text=seg,font=16)
        label12.pack(fill="x")
        root12.mainloop()
        
    def katadsr():
        m = Frame.m
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        txt = m.get()
        seg = stemmer.stem(txt)
        print(seg)
        root13 = tk.Tk()
        root13.title('Result(KataDasar)')
        label13 = tk.Label(root13,text=seg,font=16)
        label13.pack(fill="x")
        root13.mainloop()

    def process4txtrkzh():
        m = Frame.m
        txt = m.get()
        root14 = tk.Tk()
        root14.title('Result(preprocess4textrankZH)')
        result = re.sub(u'[有是会能让到]', '', txt)
        print(result)
        pyperclip.copy(result)
        label14 = tk.Label(root14,text=result,font=16)
        label14.pack(fill="x")
        
    def rommn():
        m = Frame.m
        txt = m.get()
        root15 = tk.Tk()
        root15.title('Result(RomanizeMN)')
        rm = romanize(txt, IPA)
        print(rm)
        pyperclip.copy(rm)
        label15 = tk.Label(root15,text=rm,font=16)
        label15.pack(fill="x")    
        root15.mainloop()

    def kwth():
        m = Frame.m
        txt = m.get()
        seg = ptn.word_tokenize(txt,engine='deepcut')
        print(seg)
        kw = ptn.find_keyword(seg, lentext=3)
        print(kw)
        pyperclip.copy(" ".join(kw))
        root16 = tk.Tk()
        root16.title('Result(KeywordTH)')
        label16 = tk.Label(root16,text=kw)
        label16.pack(fill="x")
        root16.mainloop()
        
    def senth():
        m = Frame.m
        txt = m.get()
        seg = ptn.sentiment(txt)
        print(seg)
        pyperclip.copy(seg)
        root17 = tk.Tk()
        root17.title('Result(SentimentTH)')
        label17 = tk.Label(root17,text=seg)
        label17.pack(fill="x")
        root17.mainloop()

    def splth():
        m = Frame.m
        txt = m.get()
        seg = ptn.spell(txt,engine='pn')
        print(seg)
        pyperclip.copy(seg)
        root18 = tk.Tk()
        root18.title('Result(SpellTH)')
        label18 = tk.Label(root18,text=seg)
        label18.pack(fill="x")
        root18.mainloop()
        
    def zaw2uni():
        m = Frame.m
        txt = m.get()
        root19 = tk.Tk()
        root19.title('Result(2UnicordMN)')
        conv = converter.convert(txt, 'unicode', 'zawgyi')
        print(conv)
        pyperclip.copy(conv)
        label19 = tk.Label(root19,text=conv,font=16)
        label19.pack(fill="x")    
        root19.mainloop()
        
    def uni2zaw():
        m = Frame.m
        txt = m.get()
        root20 = tk.Tk()
        root20.title('Result(2ZawgyiMN)')
        conv = converter.convert(txt, 'unicode', 'zawgyi')
        print(conv)
        pyperclip.copy(conv)
        label20 = tk.Label(root20,text=conv,font=16)
        label20.pack(fill="x")    
        root20.mainloop()
        
    def tokenjp():
        m = Frame.m
        txt = m.get()
        root21 = tk.Tk()
        root21.title('Result(TokenizeJP)')
        t = Tokenizer()
        for token in t.tokenize(txt):
            print(token)
            label21 = tk.Label(root21,text=token,font=16)
            label21.pack(fill="x")
        root21.mainloop()
        
    def segjp():
        m = Frame.m
        txt = m.get()
        root22 = tk.Tk()
        root22.title('Result(SegmentJP)')
        t = Tokenizer()
        token = t.tokenize(txt, wakati=True)
        print(token)
        pyperclip.copy(' '.join(token))
        label22 = tk.Label(root22,text=token,font=16)
        label22.pack(fill="x")
        root22.mainloop()
        
    def cntjp():
        m = Frame.m
        txt = m.get()
        root23 = tk.Tk()
        root23.title('Result(CounterJP)')
        t = Tokenizer()
        for token in t.tokenize(txt):
            print(token)
        c = collections.Counter(t.tokenize(txt, wakati=True))
        label23 = tk.Label(root23,text=c,font=16)
        label23.pack(fill="x")
        root23.mainloop()
        
    def w2v():
        m = Frame.m
        txt = m.get()
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        model = word2vec.Word2Vec(txt,
                          sg=1,
                          size=100,
                          min_count=1,
                          window=10,
                          hs=1,
                          negative=0)
        fn = tkfd.asksaveasfilename()
        f = open(fn, 'a')
        model.save(fn)
        f.close()

    def dd():
        m = Frame.m
        txt = m.get()
        root24 = tk.Tk()
        root24.title('Result(DeleteDigit)')
        result = re.sub('[0-9.,]', '', txt)
        print(result)
        pyperclip.copy(result)
        label24 = tk.Label(root24,text=result,font=16)
        label24.pack(fill="x")
        
    def ds():
        m = Frame.m
        txt = m.get()
        root25 = tk.Tk()
        root25.title('Result(DeleteSpace)')
        result = re.sub(' ', '', txt)
        print(result)
        pyperclip.copy(result)
        label25 = tk.Label(root25,text=result,font=16)
        label25.pack(fill="x")
        
    def para():
        m = Frame.m
        txt = m.get()
        root26 = tk.Tk()
        root26.title('Result(Paragraphs)')
        result = re.sub('[：；，。:;,.]', '\n', txt)
        print(result)
        pyperclip.copy(result)
        label26 = tk.Label(root26,text=result,font=16)
        label26.pack(fill="x")
        
    def db():
        m = Frame.m
        txt = m.get()
        root27 = tk.Tk()
        root27.title('Result(DeleteBreak)')
        result = re.sub('\n', '', txt)
        print(result)
        pyperclip.copy(result)
        label27 = tk.Label(root27,text=result,font=16)
        label27.pack(fill="x")

    def rs():
        m = Frame.m
        txt = m.get()
        ppl = PipelineCommon([(ProcessorTokenizerRu(), 
                               ['text'], 
                               {0 : 'tokens'}),
                            (ProcessorSentenceSplitter(), 
                                ['tokens'], 
                                {0 : 'sentences'}),
                             (ProcessorMystem(), 
                              ['tokens', 'sentences'], 
                              {'lemma' : 'lemma', 
                               'postag' : 'postag'})])
        result = ppl(txt)
        print(result)      

    def l2c():
        m = Frame.m
        txt = m.get()
        root28 = tk.Tk()
        root28.title('Result(Latin2Cyrillic)')
        result = cyrtranslit.to_cyrillic(txt, 'ru')
        print(result)
        pyperclip.copy(result)
        label28 = tk.Label(root28,text=result,font=16)
        label28.pack(fill="x")
        
    def c2l():
        m = Frame.m
        txt = m.get()
        root29 = tk.Tk()
        root29.title('Result(Cyrillic2Latin)')
        result = cyrtranslit.to_latin(txt, 'ru')
        print(result)
        pyperclip.copy(result)
        label29 = tk.Label(root29,text=result,font=16)
        label29.pack(fill="x")

if __name__ == '__main__':
    f = Frame()
    Frame.main()
