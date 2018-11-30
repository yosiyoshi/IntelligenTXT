# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 09:30:55 2018

@author: Yosiyoshi
"""
import difflib
import nltk
from nltk import CFG
from nltk import ChartParser
import nltk.parse
from nltk.tokenize import wordpunct_tokenize
from nltk.stem import SnowballStemmer
import re

class Langvowel:
    def langvowel(self, txt):
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
        return result

class Viet2Pinyin():
    def viet2pinyin(self, txt):
        a = re.sub("ch","zh", txt)
        b = re.sub("q","(g/j/q)", a)
        c = re.sub("tr","zh", b)
        d = re.sub("[yỷýỳ]","i", c)
        e = re.sub("vi[ệê]", "yue", d)
        f = re.sub("c", "g", e)
        g = re.sub("ư", "i", f)
        h = re.sub("v", "(w/y)", g)
        i = re.sub("ngh", "y", h)
        j = re.sub("nhậ", "ri", i)
        k = re.sub("th", "(ch/sh/T)", j)
        l = re.sub("nhâ", "re", k)
        m = re.sub("[áàã]", "(a/e)", l)
        n = re.sub("[êểơờ]", "a", m)
        o = re.sub("[âếấở]", "i", n)
        p = re.sub("nh", "ng", o)
        q = re.sub("d", "(m/y)", p)
        r = re.sub("đ", "d", q)
        s = re.sub("[òồo]", "u", r)
        t = re.sub("ngi", "r", s)
        u = re.sub("x", "sh", t)
        v = re.sub("ĩa", "i", u)
        w = re.sub("ậ", "i", v)
        x = re.sub("gh", "ch", w)
        y = re.sub("t", "(j/s/x/z)", x)
        z = re.sub("kh", "K", y)
        result = re.sub("k", "(j/q)", z)
        return result

class ThaiForeignEtymolgy():
    def foreign2Thai(self, corpus, mode = "sk"):
        if mode == "sk":
            sk1 = corpus.replace("ara", "on")
            sk2 = sk1.replace("bh", "ph")
            sk3 = sk2.replace("ana", "an")
            sk4 = sk3.replace("t", "d")
            sk5 = sk4.replace("g", "gh")
            sk6 = sk5.replace("gh", "kh")
            sk7 = sk6.replace("usya", "ut")
            sk8 = sk7.replace("aka", "ok")
            sk9 = sk8.replace("j", "cha")
            sk10 = sk9.replace("asa", "atsa")
            sk11 = sk10.replace("di", "ti")
            sk12 = sk11.replace("rn", "n")
            sk13 = sk12.replace("sv", "sw")
            sk14 = sk13.replace("ry", "riy")
            sk15 = sk14.replace("tt", "d")
            sk16 = sk15.replace("d", "th")
            sk17 = sk16.replace("ao", "aa")
            skfinal = sk17.replace("v", "w")
            return skfinal
        elif mode == "ch":
            ch1 = corpus.replace("g", "kh")
            ch2 = ch1.replace("ng", "n")
            ch3 = ch2.replace("j", "y")
            ch4 = ch3.replace("n", "y")
            ch5 = ch4.replace("e", "u")
            ch6 = ch5.replace("a", "ua")
            ch7 = ch6.replace("b", "ph")
            ch8 = ch7.replace("dz", "ch")
            ch9 = ch8.replace("hr", "h")
            chfinal = ch9.replace("ts", "s")
            return chfinal
        else:
            print("invalid mode")

class OmnibusStem:
    def stemmer(self, corpus):
        conju0 = corpus.replace("ri", "ni")
        conju0a = conju0.replace("ru", "ni")
        conju0b = conju0a.replace("zh", "ts")
        conju0c = conju0b.replace("q", "g")
        conju1 = conju0c.replace("w", "kw")
        conju2 = conju1.replace("th", "t")
        conju3 = conju2.replace("d", "t")
        conju4 = conju3.replace("hk", "k")
        conju5 =conju4.replace("c", "k")
        conju6 = conju5.replace("f", "p")
        conju7 = conju6.replace("y", "j")
        conju8 = conju7.replace("p", "p")
        conju9 = conju8.replace("i", "e")
        conju10 = conju9.replace("n", "m")
        conju11 = conju10.replace("u", "e")
        conju12 = conju11.replace("b", "b")
        conju13 = conju12.replace("l", "l")
        conju14 = conju13.replace("h", "k")
        conju15 = conju14.replace("j", "g")
        conju16 = conju15.replace("kwh", "kw")
        conju17 = conju16.replace("z", "dy")
        conju18 = conju17.replace("v", "w")
        conju19 = conju18.replace("x", "k")
        final = conju19.replace("oe", "ew")
        return final

    def compStemmer(self, corpus1, corpus2, skip=0, result=1):
        corpus = corpus1 + " " + corpus2
        conju0 = corpus.replace("b", "p")
        conju1 = conju0.replace("d", "t")
        conju2 = conju1.replace("g", "k")
        conju3 = conju2.replace("q", "g")
        conju4 = conju3.replace("w", "kw")
        conju5 = conju4.replace("th", "t")
        conju6 = conju5.replace("d", "t")
        conju7 = conju6.replace("hk", "k")
        conju8 =conju7.replace("c", "k")
        conju9 = conju8.replace("f", "p")
        conju10 = conju9.replace("y", "j")
        conju11 = conju10.replace("a", "o")
        conju12 = conju11.replace("i", "e")
        conju13 = conju12.replace("u", "e")
        conju14 = conju13.replace("h", "k")
        conju15 = conju14.replace("j", "g")
        conju16 = conju15.replace("kw", "hw")
        conju17 = conju16.replace("z", "dy")
        conju18 = conju17.replace("v", "w")
        conju19 = conju18.replace("x", "k")
        final = conju19.replace("oe", "ew")
        l = final.split(" ")
        l1 = ''.join(l[0])
        l2 = ''.join(l[1])
        s = difflib.SequenceMatcher(None, l1, l2).ratio()
        if skip == 0:
            print(corpus1, ",", corpus2, "=>", l1, ",", l2, ": simlilarity =", s)
            if result >= 1:
                if s >= 0.5:
                    result = "high possibility of co-etymology"
                else:
                    result = "low possibility of co-etymology"
                return result
            else:
                return
        else:
            return

    def compTwoStems(self, corpus, skip=0, result=1):
        l = corpus.split(" ")
        l1 = ''.join(l[0])
        l2 = ''.join(l[1])
        corpus = l1 + "," + l2
        conju0 = corpus.replace("ri", "ni")
        conju0a = conju0.replace("ru", "ni")
        conju0b = conju0a.replace("zh", "ts")
        conju0c = conju0b.replace("q", "g")
        conju1 = conju0c.replace("w", "(k/h)w")
        conju2 = conju1.replace("th", "t")
        conju3 = conju2.replace("d", "t")
        conju4 = conju3.replace("hk", "k")
        conju5 =conju4.replace("c", "k")
        conju6 = conju5.replace("f", "p")
        conju7 = conju6.replace("y", "j")
        conju8 = conju7.replace("p", "p")
        conju9 = conju8.replace("i", "e")
        conju10 = conju9.replace("kk", "k")
        conju11 = conju10.replace("u", "e")
        conju12 = conju11.replace("b", "b")
        conju13 = conju12.replace("l", "l")
        conju14 = conju13.replace("h", "k")
        conju15 = conju14.replace("j", "g")
        conju16 = conju15.replace("kwh", "kw")
        conju17 = conju16.replace("z", "dy")
        conju18 = conju17.replace("v", "w")
        conju19 = conju18.replace("x", "k")
        final = conju19.replace("oe", "ew")
        resl = final.split(",")
        resl1 = ''.join(resl[0])
        resl2 = ''.join(resl[1])
        s = difflib.SequenceMatcher(None, l1, l2).ratio()
        if skip == 0:
            print(l1, ",", l2, "=>", resl1, ",", resl2, ": simlilarity =", s)
            if result >= 1:
                if s >= 0.5:
                    result = "high possibility of co-etymology"
                else:
                    result = "low possibility of co-etymology"
                return result
            else:
                return
        else:
            return

    def compStemmerStem(self, corpus, stem, skip=0, result=1):
        conju0 = corpus.replace("ri", "ni")
        conju0a = conju0.replace("ru", "ni")
        conju0b = conju0a.replace("zh", "ts")
        conju0c = conju0b.replace("q", "g")
        conju1 = conju0c.replace("w", "kw")
        conju2 = conju1.replace("th", "t")
        conju3 = conju2.replace("d", "t")
        conju4 = conju3.replace("hk", "k")
        conju5 =conju4.replace("c", "k")
        conju6 = conju5.replace("f", "p")
        conju7 = conju6.replace("y", "j")
        conju8 = conju7.replace("p", "p")
        conju9 = conju8.replace("i", "e")
        conju10 = conju9.replace("n", "m")
        conju11 = conju10.replace("u", "e")
        conju12 = conju11.replace("b", "b")
        conju13 = conju12.replace("l", "l")
        conju14 = conju13.replace("h", "k")
        conju15 = conju14.replace("j", "g")
        conju16 = conju15.replace("kwh", "kw")
        conju17 = conju16.replace("z", "dy")
        conju18 = conju17.replace("v", "w")
        conju19 = conju18.replace("x", "k")
        final = conju19.replace("oe", "ew")
        s = difflib.SequenceMatcher(None, final, stem).ratio()
        if skip == 0:
            print(corpus, ",", stem, "=>", final, ",", stem, ": simlilarity =", s)
            if result >= 1:
                if s >= 0.5:
                    result = "high possibility of co-etymology"
                else:
                    result = "low possibility of co-etymology"
                return result
            else:
                return
        else:
            return

    def simpleComp(self, corpus1, corpus2, skip=0, result=1):
        s = difflib.SequenceMatcher(None, corpus1, corpus2).ratio()
        if skip == 0:
            print(corpus1, ",", corpus2, "=>", corpus1, ",", corpus2, ": simlilarity =", s)
            if result >= 1:
                if s >= 0.5:
                    result = "high possibility of co-etymology"
                else:
                    result = "low possibility of co-etymology"
                return result
            else:
                return
        else:
            return

    def help(self):
        mes="""stemmer(self, corpus):
            `Proto-Indo-European, Proto-Sino-Tibetan etc. stemmer
            
            compStemmer(self, corpus1, corpus2, skip=0, result=1)
            if skip==0, print(corpus => stem, similarity)
            if result=1, print(high/low possibility of co-etymology)"""
        return mes

class ThrHeadStem:
    def stemmer(self, s, lang):
        print("The original sentence: ", s)
        w = wordpunct_tokenize(s)
        print("Tokenized as: ", w)
        w0 = ''.join(w[0])
        w1 = ''.join(w[1])
        w2 = ''.join(w[2])
        print("The 3 headwords: ", w0, w1, w2)
        sbstem = SnowballStemmer(lang)
        return sbstem.stem(w0), sbstem.stem(w1), sbstem.stem(w2)

class JpStem:
    def stemmer(self, corpus):
        neg = corpus.replace("ない", "")
        past = neg.replace("た", "る")
        asm = past.replace("れば", "")
        negv = asm.replace("れ", "る")
        comv = negv.replace("ろ", "る")
        adj = comv.replace("く", "し")
        adj2 = adj.replace("き", "し")
        adj3 = adj2.replace("け", "し")
        fin1 = adj3.replace("す", "する")
        fin2 = fin1.replace("るる", "る")
        return fin2

    def help(self):
        mes = """stemmer(self, corpus):
            `Japanese(Ancient/Modern) stemmer"""
        return mes

class PieStem:
    def stemmer(self, corpus):
        conju1 = corpus.replace("wh", "kw")
        conju2 = conju1.replace("th", "t")
        conju3 = conju2.replace("d", "t")
        conju4 = conju3.replace("h", "k")
        conju5 = conju4.replace("c", "k")
        conju6 = conju5.replace("f", "p")
        conju7 = conju6.replace("y", "k")
        conju8 = conju7.replace("ou", "ew")
        conju9 = conju8.replace("a", "eh")
        final = conju9.replace("i", "he")
        return final

    def help(self):
        mes = """stemmer(self, corpus):
            `Proto-Indo-European stemmer"""
        return mes

class MCRecon:
    def MCRecLiao(self, corpus):
        liao1 = corpus.replace("q", "k")
        liao2 = liao1.replace("ang", "uang")
        liao3 = liao2.replace("ia", "e")
        liao4 = liao3.replace("o", "u")
        liao5 = liao4.replace("jin", "kin")
        liao6 = liao5.replace("j", "ts")
        liao7 = liao6.replace("c", "ts")
        liao8 = liao7.replace("sh", "dz")
        liao9 = liao8.replace("zh", "tshi")
        liao10 = liao9.replace("ch", "tshi")
        liao11 = liao10.replace("w", "m")
        liao12 = liao11.replace("f", "p")
        liao13 = liao12.replace("b", "ph")
        liao14 = liao13.replace("ua", "a")
        final = liao14.replace("r", "n")
        return final

    def help(self):
        mes = """MCRecLiao(self, corpus):
            Liao-age Middle Chinese Reconstructor"""
        return mes
        
class ZhTokenDemo:
    def tokenizer(self, sent):
        print(sent)
        chinese_grammer = CFG.fromstring("""
        s -> NP VP
        PP -> P NP
        NP -> Det N | Det N PP | '我'
        VP -> V  NP | VP  PP | PP VP
        Det -> '个' | '我的'
        N -> '钱包' | '书包' | '商店'
        V -> '有' | '买' | '丢'
        P -> '在'
        """)
        parser = nltk.ChartParser(chinese_grammer)
        for tree in parser.parse(sent):
            return tree
            
    def help(self):
        mes = """tokenizer(self, sent):
            sent = list[]"""
        return mes

class MlTokenDemo:
    def tokenizer(self, sent):
        print(sent)
        malay_grammer = CFG.fromstring("""
        s -> NP VP
        PP -> P NP
        NP -> N Det | N Det PP | 'saya'
        VP -> V  NP | VP  PP | PP VP
        Det -> 'suatu' | 'itu'
        N -> 'buku' | 'kapor' | 'toko'
        V -> 'punya' | 'membeli' | 'menghilangi'
        P -> 'di'
        """)
        parser = nltk.ChartParser(malay_grammer)
        for tree in parser.parse(sent):
            return tree
class Satemize:
    def satemizer(self, corpus, avs=0):
        conju1 = corpus.replace("e", "a")
        conju2 = conju1.replace("o", "a")
        conju3 = conju2.replace("h", "")
        conju4 = conju3.replace("k", "s")
        conju5 = conju4.replace("g", "j")
        conju6 = conju5.replace("w", "v")
        final = conju6.replace("l", "r")
        if avs==0:
            return final
        else:
            conju7 = final.replace("s", "x")
            conju8 = conju7.replace("r", "arar")
            final2 = conju8.replace("j", "z")
            return final2