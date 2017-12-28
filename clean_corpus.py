import re

with open("data/corpus.txt") as fin:

    new_corpus = ""

    for line in fin:
        text = fin.readline().replace("Russ Roberts: ", "")

        myRegex = re.compile(r"\d+:\d+")
        mo = myRegex.search(text)
        if mo:
            pattern = mo.group()
            newtext = text.replace(pattern, "")
            new_corpus = new_corpus + newtext
        else:
            new_corpus = new_corpus + text

with open("data/new_corpus.txt", "a") as fout:
    fout.write(new_corpus)
