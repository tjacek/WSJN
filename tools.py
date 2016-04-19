def read_text(filename,words=True):
    txt = open(filename)
    txt=txt.read()
    txt=clean(txt)
    if(words):
        text=txt.split(" ")
    else:
        text=[s_i for s_i in txt] 
    return text

def clean(text):
    text=text.lower()
    return " ".join(text.split())

path="PJN/pjn_lab1/54.txt"
print(read_text(path,True))
