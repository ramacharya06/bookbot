def get_book_text(path):
    with open(path, "r") as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_unique_letters(text):
    d = dict()
    for i in text:
        if i.isalpha():
            i=i.lower()
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def sorted_unique_letters(d):
    l =[]
    for i in sorted(d.items()):
        l.append({"char":i[0], "num":i[1]})
        # l.append(i)
    return l
