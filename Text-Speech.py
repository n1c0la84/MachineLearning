from tkinter import Tk, Entry, Text, BOTH, W, N, E, S, END
from tkinter.ttk import Frame, Button, Label, Style

from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import Counter
from nltk import corpus
from gtts import gTTS
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from pygame import mixer

class Example(Frame):
    area = None

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Text analisys")
        self.pack(fill=BOTH, expand=True)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        label = Label(self, text="Insert URL:")
        label.grid(sticky=W, padx=5)
        entry = Entry(self)
        entry.grid(sticky=W + E, row=1, column=0, columnspan=2, padx=5)
        self.area = Text(self)
        self.area.grid(row=2, column=0, columnspan=2, rowspan=4, padx=5, sticky=E + W + S + N)
        mcombtn = Button(self, text="Common words", command=lambda: self.mcommonCallback(entry.get()))
        mcombtn.grid(row=1, column=3)
        sumbtn = Button(self, text="Summarize text.", command=lambda: self.summCallback(entry.get()))
        sumbtn.grid(row=2, column=3, pady=4)
        voicebtn = Button(self, text="Voice", command=lambda: self.voiceCallback(self.area.get("0.0", END)))
        voicebtn.grid(row=4, column=3)
        exitbtn = Button(self, text="Close", command=lambda: quit())
        exitbtn.grid(row=5, column=3)

    def mcommonCallback(self, url2open):
        soup = BeautifulSoup(urlopen(url2open), "html.parser")
        counter = Counter(soup.get_text().split())
        mostCommon = counter.most_common(30)
        self.mostCommonDict = dict(mostCommon)

        for word in corpus.stopwords.words('english'):
            try:
                del mostCommonDict[word]
            except:
                pass

        self.area.delete("0.0", END)
        text2ins = "The most common word are:\n\n" + ", ".join(self.mostCommonDict.keys())
        self.area.insert("0.0", text2ins)

    def summCallback(self, url2open):
        parser = HtmlParser.from_url(url2open, Tokenizer("english"))
        stemmer = Stemmer("english")

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words("english")

        self.area.delete("0.0", END)
        for sentence in summarizer(parser.document, 10):
            self.area.insert(END, sentence)

    def voiceCallback(self, text2speak):
        tts = gTTS(text=text2speak, lang="en")
        tts.save("./tempFile.mp3")
        mixer.init()
        mixer.music.load('./tempFile.mp3')
        mixer.music.play()

def main():
    root = Tk()
    root.geometry("800x600+300+50")
    app = Example()
    root.mainloop()

if __name__ == '__main__':
    main()