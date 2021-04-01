# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 02:10:32 2021

@author: Shaked
"""

##
def revword(word:str) -> str:
    word=word.lower()
    length=len(word)
    w_new=''
    for char in word:
        w_new=w_new+word[length-1]
        length=length-1
    return w_new    


def countword() ->int:
    text=open('text.txt')
    n=0
    count_w=1
    for line in text:
        line=line.rstrip()
        if n==0:
            word=line.lower()
            n=1
            continue
        else:
            words_l=line.split()
            for w in words_l:
                w_new1=revword(w)
                if w_new1==word:
                    count_w=count_w+1
    return count_w                    




