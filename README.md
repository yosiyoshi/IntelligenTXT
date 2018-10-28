This project is consist of 4 contents.

# (1)IntelligenTXT: Main GUI project
Simplest but an intelligent text editor with NLP functions:

https://github.com/yosiyoshi/IntelligenTXT/blob/master/main.py

https://github.com/yosiyoshi/IntelligenTXT/blob/master/main_mini.py

# (2)main.Frame: IntelligenTXT used as a GUI library
(1)"IntelligenTXT" itself is also working as a GUI library "main.Frame".

Usage: put "main.py" or "main_mini.py" on any directory -> "from main import Frame" or "from main_mini import Frame"

# (3)YNLTK: "YoshiNLTK" Original NLP library
Merged with YoshiNLTK: https://github.com/yosiyoshi/YoshiNLTK
Usage: put ynltk.py on any directory -> "import ynltk"

# (4)AufIntelligenTXT: Open version of this repository
Released in AufIntelligenTXT(AITXT), the repository is aimed to develop a practical software application with functions in this repository for Windows, MacOS, Linux, iOS, Android etc. The author of this repository is Yosiyoshi, and the copyright is written on the bottom of this document: https://github.com/yosiyoshi/AufIntelligenTXT-AITXT-

# How to Use


1.Install all requirement written in "readme.txt" on this repository.


2.Just prompt "python main.py" or "python main_mini.py"


# Languages


v0.04: Chinese, Thai, Vietnamese, and Burmese(Myanmar). 4 languages in total.

v0.05: Added Japanese, and Gensim word2vec module. 5 languages in total.

v0.06: Added Text processing feature to delete numerals(0-9.,), and Chinese textrank

v0.07: Added Russian. 6 languages in total.

v0.09: Added basic functions as a text editor like "Notepad".

v0.10: Added Bahasa(Indonesian/Malay). 7 languages in total.

# Requirement API Used
/gensim


Chinese


/jieba


Japanese


/janome


Vietnamese


/pyvi


/underthesea


Thai


/tltk


/pythainlp


Burmese


/python-myanmar


Russian


/pymystem3


/isanlp (dependencies: grpcio)


/cyrtranslit

Bahasa

/PySastrawi

etc.


/logging


/pyperclip


/tkinter


# Copyright
Yosiyoshi is a GitHub user.
Copyright © 2018 Yosiyoshi All Rights Reserved.
