--Reference--
IntelligenTXT
α ver0.1
Author: yosiyoshi
---------------
Please just try first time:
The first time run the IntelligenTXT, please try to write daily to know the feature of this software.
[1]There are 10 menus on the upper side of the editor, select "Text processing"->"dateNow".
[2]The editor will insert the present time on the textbox, and write anything (e.g. "日記を書き始めた。") after the date inserted.
[3]Save the edit(work)ing content to any .txt file (e.g. "text.txt").
[4]Select "New" to delete the text written in textbox, and repeat [1]-[2] with any different text(e.g. "疲れた。") and rewrite on the file you've saved on step[3]("text.txt").
[5]Open the file saved on step[4], and you'll see the two articles of daily are saved.
e.g.
20:55 2018/10/02
日記を書き始めた。
20:56 2018/10/02
疲れた。

0.Prerequirement
/Python IDE to execute .py file

Basic APIs
/__future__
/tkinter
/sys
/re
/datetime

Additional APIs need to be installed (from pip or github)
/pyperclip
/pythainlp
/jieba
/pyvi
/tltk
/myanmar
/janome
/collections
/gensim
/isanlp
/cyrtranslit
/Sastrawi

1.Feature
/Two modes of editor size
"main.py" is the editor of multiple lines and same to "Notepad" software size.
"main_mini.py" is of single line so small size.

/Natural Language Processing
Automatic analysis done on your document!
Natural Langugage Processing features for 7 languages in total:
Chinese(ZH), Thai(TH), Japanese(JP), Bahasa Melayu/Indonesia(Bahasa), Vietnamese(VT), Burmese(MN), and Russian(RU). Segmentation, POS-tagging, Keywords extraction, Emotion recognition etc.
Whole your document will be processed by clicking menu to command(e.g. "NLP(?)"->as you like), and the result will be automatically shown on an independant window of the display, and auto-copied on your clipboard.

/User Friendly
Command "Save" is replaced by "addSave", is to save the editing content to a textfile without "overwriting" but just "adding": 
editor text"aaa"-> addSave -> Target .txt file text"bbb"+"aaa"="bbbaaa"

Command "Open" is replaced by "addOpen", is to open textfile and load the content on edit(work)ing file:
Opened .txt file text"aaa"-> addOpen -> editor text"bbb"+"aaa"="bbbaaa"
Therefore, no risk of missoperation to lose edit(work)ing text data.

The key of shortcut is showned as a capital letter existing within the name of function: "Save"->"S"key, "Load"->"L"key etc.

/Efficient text processing
"Text processing" menu provide you with simple but convenient tools:
Insert present date("dataNow" tool), delete numbers and numerical symbols("deleteDigit"), delete breaks("deleteBreaks") and space("deleteSpace").
