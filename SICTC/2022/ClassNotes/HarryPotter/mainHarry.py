import glob
import re
import matplotlib.pyplot as plt

def findBetween(string1,string2):
    """findBetween

    Arguments:
        Str String1: First string match to split between.
        Str String2: Seconds tring to match and split between.
    
    Returns: Data inbetween two matched strings.
    """
    try:
        return l.split(string1)[1].split(string2)[0]
    except:
        return ""

books = (glob.glob("data/*.txt"))

bookList = []
for b in books:
    bookList.append(b[5:])

for i in bookList:
    data = open("data/"+i, "r", encoding="utf-8").readlines()
    reducedFile = []
    for l in data:
        if l != "\n":
            reducedFile.append(l)
        if "Page |" in l:
            page = findBetween("Page | ", " ")
            #https://www.adamsmith.haus/python/answers/how-to-remove-all-non-numeric-characters-from-a-string-in-python
            page = re.sub("[^0-9]", "", page)
    newFile = open("out/"+i,"w+", encoding="utf-8").write("".join(reducedFile))
    plt.bar(i.split("Book ")[1].split(" -")[0],int(page))


plt.xlabel("Book Number")
plt.ylabel("Pages")
plt.title("Harry Potter Book Number Amount")
plt.show()