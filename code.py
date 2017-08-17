from difflib import SequenceMatcher
import urllib.request
import os
from bs4 import BeautifulSoup

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def scarpe():
    url = input('Enter URL of the playList- ') #"https://www.youtube.com/playlist?list=PL5-da3qGB5ICeMbQuqbbCOQWcS6OYBr5A"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    file = open('list.txt','w')
    s=''
    i=1
    youtubeList=[""]

    for link in soup.find_all('a'):
        if "index" in link.get('href'):
            tmp=link.text.strip()
            if len(tmp)>0:
                youtubeList.append(tmp)
                s=s+tmp+'\n'
                i=i+1
 
    #print (youtubeList)
    file.write(s)
    file.close()
    return youtubeList


def handleFiles():
    dirction = input("Enter dirction of playList on your PC ") #r"C:\Users\SaherOs\Downloads\Machine learning in Python with scikit-learn"
    file_list = os.listdir(dirction)
    return file_list , dirction
    
def getMatch():
    listFromWeb = scarpe()
    listFromComputer , dirction = handleFiles()
    
    counter = 0 
    savedDir=os.getcwd()
    os.chdir(dirction)
    for i in listFromComputer:
        counter = 0
        for j in listFromWeb :
            if similar(i , j) > .9:
                os.rename(i , str(counter)+ '- ' + i  )
                break ;
            counter+=1 
    os.chdir(savedDir)
getMatch()