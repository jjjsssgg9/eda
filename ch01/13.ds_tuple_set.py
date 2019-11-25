# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:37:58 2019

@author: shkim
"""

"""
# Tuple
"""
#%%

t=(1,2,3,4,5)
type(t)
t[1:3]
#%%
t[-1]
#%%
t[1:6:2]
#%%
t[1]=22
"""
# Set
"""
#%%
t+t
#%%
#s1={}# empty dictionart
# 합집합
s={1,2,3,4,5,4}
s

#%%
s.update({2,4,3,5,3,5,3,6,2,34,5,6,6,3,4,})
s
#%%
s.discard(2)
s
#%%
s.clear()
s
#%%
s1={1,2,3,4,5}
s2=set([3,4,5,6,7])
#%%
s3 = s1.union(s2)
#%%
#s1+s2#error

#%%
# 교집합
s1={1,2,3,4,5}
s2=set([3,4,5,6,7])
s3 = s1.intersection(s2)
s3 = s1&s2 #ok 
s3
#%%

# 차집합
s1={1,2,3,4,5}
s2=set([3,4,5,6,7])
#s3 = s1-s2
s3 = s1.difference(s2)
s3








