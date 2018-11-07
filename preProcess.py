# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 20:49:55 2018

@author: callu
"""

import pywikibot, json, os, sys, wikipedia
import nltk, re

site = pywikibot.Site()

page = pywikibot.Page(site, u"cheese").text

#print(page)

sentTokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
wordTokenizer = nltk.tokenize.word_tokenize(page)

headings = re.compile('=+ ([^=]+) =+\s*')

page = wikipedia.page("cheese").content

content = re.sub(headings, '', page)

#print(content)

#print("\n\n"+sentTokenizer.tokenize(page)[2])