# imports
from bs4 import BeautifulSoup
import requests
import csv
import re
from collections import Counter, OrderedDict

# this function returns a soup page object
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj

# scraper website: heise.com
def main():

    fobj = open('heise_headers.csv', 'w')      # open file
    csvw = csv.writer(fobj, delimiter = ';')      # create csv writer, set delimiter to ;
    csvr = csv.reader(fobj, delimiter = ';')    #create csv reader, set delimiter to ;

    for page in range(0,4,1):   #cycle through all the pages of the site below
        heise_url = "https://www.heise.de/thema/https?seite="+ str(page)

        content = getPage(heise_url).find("div", { "class" : "keywordliste" })

    # find header in xml
        for c in content.findAll("header"):
            #filter not relevat data
            if c.parent.find("aside"):
                break
            else:
                zeile = []
                c = c.text.encode('utf-8')
                zeile.append(c)
                csvw.writerow(zeile)
    
    #read heise_headers.csv to return 3 most common
    words = re.findall('\w+', open('heise_headers.csv').read(),re.UNICODE)
    print(Counter(words).most_common(3))

    fobj.close()                                # close file
    print("\nDONE !\n\n\nheise.com headers were scraped completely.\n")
    

# main program

if __name__ == '__main__':
    main()
