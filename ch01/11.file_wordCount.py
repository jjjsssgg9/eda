# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:57:13 2019

@author: shkim
"""

f =open("./11.yesterday.txt", 'r' )


lines = f.readlines()
f.close()

contents = ""
for line in lines:
    contents = contents + line.strip() + "\n"

contents
#%%
cnt = contents.upper().count('YESTERDAY')
print("Number of a Word 'Yesterday' : " , cnt)
