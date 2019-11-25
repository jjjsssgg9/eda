# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:58:39 2019

@author: shkim
"""

score = int(input("Inpur Score==>"))#키보드로 들어오는건 전부 string


if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else :
    grade = 'F'

print(grade)
#%%

score = int(input("Inpur Score==>"))#키보드로 들어오는건 전부 string


if score >= 90:
    grade = 'A'
if 90>= score >= 80 :
    grade = 'B'
if 80 >= score >= 70:
    grade = 'C'
if 70 >= score >= 60:
    grade = 'D'
if score<=60:
    grade = 'F'

print(grade)
