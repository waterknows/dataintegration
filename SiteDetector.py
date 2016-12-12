import pandas as pd
import requests
from bs4 import BeautifulSoup
import time, random
import numpy as np
import csv
df=pd.read_excel("C:/Users/yxiao/UCI_Clean.xlsx")
words=df['Domain'].tolist()
names=[]
n=0

for q in words:
    wt = random.uniform(3, 7)
    time.sleep(wt)
    if q == "N/A":
        name = "N/A"
    else:
        google = "https://www.google.com/search?q=" + str(q) +"&ie=utf-8&oe=utf-8"
        r = requests.get(google)
        soup = BeautifulSoup(r.text, "html.parser")
        try:
            name=soup.find("div",{"class":"g"}).find("a").get_text()
        except:
            name = "N/A"
    names.append(name)
    n=n+1      
    print (n)

df2=pd.DataFrame(
    {'Domain': words,
     'Site': names
    })
df2.to_excel('Site2.xlsx',index=False)

#Goldman Sachs
#Moscow Stock Exchange
#Ohio State University
#Deutsche Bank
#CERN
