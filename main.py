import PyPDF2
import operator

book: dict = {}


def indexWord(context: str) -> None:
    """
        Takes a Page as a str, splits it
        if needed it inserts a new entry into dict
        else it updates the word count
    """
    words = context.split()
    for word in words:
        if word not in book:
            book.update({word: 0})
        else:
            book[word] += 1


with open('pythonhighperformance.pdf', 'rb') as f:
    pdf = PyPDF2.PdfFileReader(f)
    i = 0
    while i < pdf.getNumPages():
        # print(i)
        page = pdf.getPage(i)
        context = page.extractText()
        indexWord(context)
        i += 1
book = sorted(book.items(), key=operator.itemgetter(1))
print(book)
