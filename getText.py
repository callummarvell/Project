# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:32:00 2018

@author: callu
"""

import wikipedia, nltk, os, json, random

wordlist = []
done = []
target = 5000000
current = ""

with open('words.json','r') as f:
    datastore=json.load(f)

for r in range(0,len(datastore[0])-1):
    #print(datastore[0]["WORD"+str(r+1)].lower())
    wordlist.append(datastore[0]["WORD"+str(r+1)].lower().replace(" ", "_"))
    
try:
    os.mkdir("corpora")
    os.chdir("corpora")
except OSError:
    os.chdir("corpora")
    
for word in wordlist[1:]:
    print(word)
    random.seed(word)
    current = ""
    if word in done:
        continue
    with open(word+".json",'r') as f:
        titles = json.load(f)
    while len(current)<target:
        rand_index = random.randrange(len(titles))
        try:
            content = wikipedia.page(titles[rand_index]).content
            current += "\n"+content
        except wikipedia.PageError:
            continue
        except wikipedia.DisambiguationError:
            continue
    done.append(word)
    with open(word+"_tot.json",'w') as f:
        json.dump(current, f)    
        #print(current)