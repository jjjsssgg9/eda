# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:26:38 2019

@author: shkim
"""

"""
# deque
"""
#%%
# Stack

from collections import deque

dq_list = deque()
for i in range(5):
    dq_list.append(i)
    
dq_list

#%%
dq_list.pop()
#%%
dq_list.popleft()

#%%
# Queue
from collections import deque

dq_list = deque()
for i in range(5):
    dq_list.appendleft(i)
    
dq_list
#%%
dq_list.pop()

#%%
# Circular Queue - rotate()
from collections import deque

dq_list = deque()
for i in range(5):
    dq_list.appendleft(i)
#    dq_list.appendleft(i)

dq_list
#%%
dq_list.rotate(2)
dq_list
#%%
dq_list.rotate(2)
dq_list
#%%
# reverse()
dq_list.reverse()
dq_list



#%%
# extend(), extendleft()

dq_list = deque([0, 1, 2, 3, 4])
dq_list
#%%
dq_list.extend([5,6,7])
dq_list
dq_list

#%%
dq_list = deque([0, 1, 2, 3, 4])
dq_list.extendleft([5,6,7])
dq_list

#%%
"""
# Ordering Dictionary
"""
#%%
d = {}
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

for k, v in d.items():
    print(k, v)

#%% 
from collections import OrderedDict  

d = OrderedDict()

d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

for k, v in d.items():
    print(k, v)

#%%
from collections import OrderedDict   

d = {}
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

def sort_by_key(t):
    return t[1]      #1로 하면 value로 소팅

od = OrderedDict(sorted(d.items(),key=sort_by_key))
od.items()

#%%
from collections import OrderedDict   

d = {}
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

def sort_by_value(t):
    return t[1]     

od = OrderedDict(sorted(d.items(), key=sort_by_value))
od.items()
  
#%%
"""
# Default Dictionary
"""
#%%
# error 
d = dict()
print(d["first"])

#%%
from collections import defaultdict

d = defaultdict(lambda: "ㄷㄷㄷ")          # Default 값을 0으로 설정
print(d["first"], d['bb'])
d.items()

#%%
# error : yellow key
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = dict()
for k, v in s:
    d[k].append(v)

print(d.items())#key가 유니크 하지 않아 에러가 뜬다. error

#%%
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d.items()) # [('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])]


#%%
# collections 응용-1 : text 내에 포함된 각 단어의 수를 출력하라

# split() : space로 분리, split(',')
text = """A press release is the quickest and easiest way to get free \
  publicity. If well written, a press release can result in multiple \
  published articles about your firm and its products. And that can mean \
  new prospects contacting you asking you to sell to them. ….""".lower().split()
type(text), text[:10]

# default dictionary 사용
from collections import defaultdict

word_count = ...........             # Default 값을 0으로 설정
.......

word_count

# ordered dictionary 사용
from collections import OrderedDict

od = ...........
od

#%%
"""
# Counter Module
"""
#%%
from collections import Counter

text = list('Good morning everybody!!')
type(text), text[:10]

#%%
c = ..........
c['o'], c['e'], c['g']


#%%
# collections 응용-1

text = """A press release is the quickest and easiest way to get free \
  publicity. If well written, a press release can result in multiple \
  published articles about your firm and its products. And that can mean \
  new prospects contacting you asking you to sell to them. ….""".lower().split()
type(text), text[:10]

from collections import Counter

c = .........
c

#%%
from collections import Counter

c = Counter({'red':3, 'blue':1, 'gray':4})
list(c.___)

#%%
list(c.____)

#%%
list(c.____)

#%%
from collections import Counter

c = Counter(cats=3, dogs=5)
list(c.elements())

#%%
# 덧셈, 뺄셈, 논리연산  

from collections import Counter

c1 = Counter(a=3, b=5, c=2)
c2 = Counter(a=-1, b=3, c=7)
....   #뺄셈
c1

#%%
from collections import Counter

c1 = Counter(a=3, b=5, c=2)
c2 = Counter(a=-1, b=3, c=7)
....  # 덧셈
....  # 논리 AND
....  # 논리 OR

#%%
"""
# namedtuple Module
"""
#%%
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
p

#%%
p = Point(11, y=22)
p

#%%
p = Point(y=11, x=22)
p, p.x, p.y, p[0], p[1]

#%%