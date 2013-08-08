import re
from itertools import groupby

# Use pdfminer to do the PDF -> text conversion.
# TODO: Integrate PDFminer.
# TODO: Make a GUI interface.
with open('farnell.txt', 'r') as file:
    text = "".join(line for line in file)

ArtPattern = re.compile(r"(^[0-9]{6,}$)\s(?:\w|-)+\s(\d+)$(?:(?:.*?)Beskrivning(?:.*?)Tillverkarnummer(?:.*?))(^(?:\w|\.)+_[0-9]{1,}$)", re.DOTALL | re.MULTILINE)
articles = ArtPattern.findall(text)

print "Number of matchet articles in farnell.txt: %s" % len(articles)
print "Bins needed:"
for i, j in groupby(articles, key=lambda x : x[2]):
    t = list(zip(*j))
    print(t[2][0])
print "=================================================="

barcode = ""
LastBarcode = ""
unseen = list(range(1, len(articles)+1))

while True:
    barcode = raw_input("Please scan the barcode of the article: ")
    if barcode == "exit":
        break
    if barcode == LastBarcode:
        print "Already scanned."
    else:
        result = BarPattern.search(barcode)
        a = articles[int(result.group(0))-1]
        print "%s : %s \t %s \t %s" % (int(result.group(0)), a[0], a[1], a[2])
        try:
            unseen.remove(int(result.group(0)))
        except:
            print "Could not remove from unseen articles list."
    LastBarcode = barcode

unseen.sort()
print "Unseen items: %s" % len(unseen)
for item in unseen:
    print item, str(articles[item-1])
