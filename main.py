#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
Created on 2012-5-6

@author: kwdhdts
'''
'''
Created on 2012-5-19

@author: Administrator
'''

from __future import division
import nltk
from nltk.book import *

def gutenberg():
    from nltk.corpus import gutenberg
    for t in gutenberg.fileids():
        num_chars = len(gutenberg.raw(t))
        num_words = len(gutenberg.words(t))
        num_sents = len(gutenberg.sents(t))
        num_vocab = len(set([w.lower() for w in gutenberg.words(t)]))
        print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), t
        
def lexical_diversity(text):
    return len(text) / len(set(text))

def word_percentage(text,word): 
    c = text.count(word)
    per = c/len(text)*100
    return (c,per)

def long_words(text,length):
    return [word for word in text if len(word) >= length]

def length_frequency(text,length,frequency):
    fdist = FreqDist(text)
    return sorted([w for w in set(text) if len(w) >= length and fdist[w] >= frequency])
    
def main():
    pass

if __name__ == "__main__":
    main()
    