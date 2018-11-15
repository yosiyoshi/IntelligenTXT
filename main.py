#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:39:44 2018

@author: YosiYoshi
"""
from __future__ import unicode_literals

import tkinter.filedialog as tkfd
from tkinter import scrolledtext
import sys
sys.path.append("../")
import re
from datetime import datetime

import pyperclip

import pythainlp as ptn
from pythainlp.date import now

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
    m = scrolledtext.ScrolledText(root,font=("",14),height=2000,width=2000)
    
    def main():
        root = Frame.root
        m = Frame.m
        root.title('IntelligenTXT v0.1')
      
        menub1 = tk.Menu(root, tearoff=0)
        root.configure(menu = menub1)
        menuf1 = tk.Menu(menub1, tearoff=0)
        menuf0 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"File", menu=menuf0,  underline=5)
        menuf0.add_command(label=u"New", command=Frame.new, underline=5, accelerator = 'Ctrl-N')
        menuf0.add_command(label=u"addOpen", command=Frame.load, underline=5, accelerator = 'Ctrl-O')
        menuf0.add_command(label=u"addSave", command=Frame.save, underline=5, accelerator = 'Ctrl-S')
        menuf0.add_command(label=u"eXit", command=root.destroy, underline=5, accelerator = 'Ctrl-X')

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
        menuf2.add_command(label=u"dateNow", command=Frame.dateth, underline=5, accelerator = 'Ctrl-N')
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
        menuf8.add_command(label=u"Stem", command=Frame.katadsr, underline=5, accelerator = 'Ctrl-S')

        menuf3 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(VT)", menu=menuf3,  underline=5)
        menuf3.add_command(label=u"Vietnam2pinyin", command=Frame.vnzh, underline=5, accelerator = 'Ctrl-V')
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
        menuf6.add_command(label=u"CapitalLower", command=Frame.cptlow, underline=5, accelerator = 'Ctrl-C')
        menuf6.add_command(label=u"dateNow", command=Frame.date, underline=5, accelerator = 'Ctrl-N')
        menuf6.add_command(label=u"deleteDigit", command=Frame.dd, underline=5, accelerator = 'Ctrl-D')
        menuf6.add_command(label=u"deleteBreaks", command=Frame.db, underline=5, accelerator = 'Ctrl-B')
        menuf6.add_command(label=u"deleteSpace", command=Frame.ds, underline=5, accelerator = 'Ctrl-S')
        menuf6.add_command(label=u"Paragraphs", command=Frame.para, underline=5, accelerator = 'Ctrl-P')
        menuf6.add_command(label=u"Language?", command=Frame.langety, underline=5, accelerator = 'Ctrl-L')

        m.pack(fill="x")
        root.mainloop()

    def new():
        m = Frame.m
        m.delete('1.0', 'end')

    def save():
        fn = tkfd.asksaveasfilename()
        m = Frame.m
        f = open(fn, 'a', encoding="utf-8_sig")
        f.write(m.get('1.0', 'end -1c')+"\n")
        f.close()

    def load():
        fn = tkfd.askopenfilename()
        m = Frame.m
        f = open(fn, 'r', encoding="utf-8_sig")
#        m.insert('end', '\n')
        for x in f:
            m.insert('end', x)
        f.close()
        m.focus_set()
    
    def date():
        m = Frame.m
        m.insert('end', datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    def dateth():
        m = Frame.m
        m.insert('end', now())

    def segzh():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
        root6 = tk.Tk()
        root6.title('Result(KeywordsZH)')
        for x, w in jieba.analyse.extract_tags(txt, withWeight=True):
            print('%s %s' % (x, w))
            label6 = tk.Label(root6,text='%s %s' % (x, w),font=16)
            label6.pack(fill="x")
        root6.mainloop()
        
    def trzh():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
        root25 = tk.Tk()
        root25.title('Result(TextrankZH')
        for x, w in jieba.analyse.textrank(txt, withWeight=True):
            print('%s %s' % (x, w))
            label25 = tk.Label(root25, text='%s %s' % (x, w),font=16)
            label25.pack(fill="x")
        root25.mainloop()
        
    def poszh():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
        seg = tl.pos_tag(txt)
        print(seg)
        pyperclip.copy(" ".join(seg))
        root8 = tk.Tk()
        root8.title('Result(POS-TH)')
        label8 = tk.Label(root8,text=seg,font=16)
        label8.pack(fill="x")
        root8.mainloop()
    
    def segvt():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
        seg = ViPosTagger.postagging(ViTokenizer.tokenize(txt))
        print(seg)
        pyperclip.copy(" ".join(seg))
        root10 = tk.Tk()
        label0 = tk.Label(root10,text=seg,font=16)
        label0.pack(fill="x")
        root10.title('Result(POS-VT)')
        root10.mainloop()
        
    def sumth():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
        seg = stemmer.stem(txt)
        print(seg)
        root13 = tk.Tk()
        root13.title('Result(KataDasar)')
        label13 = tk.Label(root13,text=seg,font=16)
        label13.pack(fill="x")
        root13.mainloop()

    def process4txtrkzh():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
        root14 = tk.Tk()
        root14.title('Result(preprocess4textrankZH)')
        result = re.sub(u'[有是会能让到]', '', txt)
        print(result)
        pyperclip.copy(result)
        label14 = tk.Label(root14,text=result,font=16)
        label14.pack(fill="x")
        
    def rommn():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        model = word2vec.Word2Vec(txt,
                          sg=1,
                          size=100,
                          min_count=1,
                          window=10,
                          hs=1,
                          negative=0)
        fn = tkfd.asksaveasfilename()
        f = open(fn, 'a', encoding="utf-8_sig")
        model.save(fn)
        f.close()

    def dd():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
        root24 = tk.Tk()
        root24.title('Result(DeleteDigit)')
        result = re.sub('[0-9.,]', '', txt)
        print(result)
        pyperclip.copy(result)
        label24 = tk.Label(root24,text=result,font=16)
        label24.pack(fill="x")
        
    def ds():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
        root25 = tk.Tk()
        root25.title('Result(DeleteSpace)')
        result = re.sub(' ', '', txt)
        print(result)
        pyperclip.copy(result)
        label25 = tk.Label(root25,text=result,font=16)
        label25.pack(fill="x")
        
    def para():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
        root26 = tk.Tk()
        root26.title('Result(Paragraphs)')
        result = re.sub('[：；，。:;,.]', '\n', txt)
        print(result)
        pyperclip.copy(result)
        label26 = tk.Label(root26,text=result,font=16)
        label26.pack(fill="x")
        
    def db():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
        root27 = tk.Tk()
        root27.title('Result(DeleteBreak)')
        result = re.sub('\n', '', txt)
        print(result)
        pyperclip.copy(result)
        label27 = tk.Label(root27,text=result,font=16)
        label27.pack(fill="x")

    def rs():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
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
        txt = m.get('1.0', 'end -1c')
        root28 = tk.Tk()
        root28.title('Result(Latin2Cyrillic)')
        result = cyrtranslit.to_cyrillic(txt, 'ru')
        print(result)
        pyperclip.copy(result)
        label28 = tk.Label(root28,text=result,font=16)
        label28.pack(fill="x")
        
    def c2l():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
        root29 = tk.Tk()
        root29.title('Result(Cyrillic2Latin)')
        result = cyrtranslit.to_latin(txt, 'ru')
        print(result)
        pyperclip.copy(result)
        label29 = tk.Label(root29,text=result,font=16)
        label29.pack(fill="x")
        
    def langety():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
        root30 = tk.Tk()
        root30.title('Result(LanguageDetection)')
        h=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        h[0]=txt.count("oo")
        h[1]=txt.count("y")
        h[2]=txt.count("oe")
        h[3]=txt.count("oi")
        h[4]=txt.count("ie")
        h[5]=txt.count("ee")
        h[6]=txt.count("ou")
        h[7]=txt.count("uu")
        h[8]=txt.count("ei")
        h[9]=txt.count("eu")
        h[10]=txt.count("ai")
        h[11]=txt.count("au")
        h[12]=txt.count("é")
        h[13]=txt.count("è")
        h[14]=txt.count("ua")
        h[15]=txt.count("à")
        h[16]=txt.count("â")
        h[17]=txt.count("aa")
        h[18]=txt.count("oa")
        h[19]=txt.count("ea")
        h[20]=txt.count("ä")
        h[21]=txt.count("ö")
        h[22]=txt.count("ü")
        h[23]=txt.count("ue")
        h[24]=txt.count("ij")
        message= "Input text:", txt, "\n[oo,y,oe,oi,ie,ee,ou,uu,ei,eu,ai,au,é,è,ua,à,â,aa,oa,ea,ä,ö,ü,ue,ij] existing in the text:\n", h, "\nRecognized as:\n"
        if max(h)==0:
            result="None"
        elif max(h)==h[1] or max(h)==h[18] or max(h)==h[19]:
            result="English?"
        elif max(h)==h[2]:
            result="Dutch or Old Indonesian?"
        elif max(h)==h[3] or max(h)==h[6] or max(h)==h[12] or max(h)==h[13] or max(h)==h[14] or max(h)==h[15] or max(h)==h[16] or max(h)==h[23]:
            result="French?"
        elif max(h)==h[4]:
            result="French or German?"
        elif max(h)==h[5] or max(h)==h[0]:
            result="English or Dutch?"
        elif max(h)==h[7] or max(h)==h[17] or max(h)==h[24]:
            result="Dutch?"
        elif max(h)==h[8] or max(h)==h[20] or max(h)==h[21] or max(h)==h[22]:
            result="German?"
        elif max(h)==h[10]:
            result="English or French?"
        elif max(h)==h[11] or max(h)==h[9]:
            result="English, French or German?"

        result2=message,result
        print(result2)
        pyperclip.copy(result)
        label30 = tk.Label(root30,text=result,font=16)
        label30.pack(fill="x")

    def vnzh():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
        root31 = tk.Tk()
        root31.title('Result(VN2Pinyin)')
        a = re.sub("tr","(zh/ch)", txt)
        b = re.sub("quy","(q/j)u", a)
        c = re.sub("q","g", b)
        d = re.sub("[yỷý]","i", c)
        e = re.sub("việ", "yue", d)
        f = re.sub("c", "g", e)
        g = re.sub("ư", "i", f)
        h = re.sub("v", "(w/y)", g)
        i = re.sub("ngh", "y", h)
        j = re.sub("nhậ", "ri", i)
        k = re.sub("th", "(ch/sh/T)", j)
        l = re.sub("nhâ", "re", k)
        m = re.sub("[áàã]", "e", l)
        n = re.sub("[êể]", "a", m)
        o = re.sub("[âế]", "i", n)
        p = re.sub("nh", "ng", o)
        q = re.sub("d", "(m/y)", p)
        r = re.sub("đ", "d", q)
        s = re.sub("[òồo]", "u", r)
        t = re.sub("ngi", "r", s)
        u = re.sub("x", "sh", t)
        v = re.sub("ĩa", "i", u)
        w = re.sub("ậ", "i", v)
        x = re.sub("gh", "ch", w)
        y = re.sub("t", "(s/j/x/z)", x)
        z = re.sub("k", "j", y)
        result = re.sub("jh", "k", z)

        pyperclip.copy(result)
        print(result)
        label31 = tk.Label(root31,text=result,font=16)
        label31.pack(fill="x")
    
    def cptlow():
        m = Frame.m
        txt = m.get('1.0', 'end -1c')
        root32 = tk.Tk()
        root32.title('Result(CapitalLower)')
        result = txt.lower()
        pyperclip.copy(result)
        print(result)
        label32 = tk.Label(root32,text=result,font=16)
        label32.pack(fill="x")

if __name__ == '__main__':
    f = Frame()
    Frame.main()
