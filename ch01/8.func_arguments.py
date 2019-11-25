# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:22:34 2019

@author: shkim
"""

"""
# 키워드 인수 (keyward arguments)
"""
#%%
def print_something(my_name, your_name):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something("kim", "lee")
print_something("lee", "kim")
print_something( your_name="KIM", my_name="LEE" )

#%%
def kwargs_test( **kwargs ):
    print(kwargs)
    print("First value is {first}".format( **kwargs ))
    print("Second value is {second}".format(  **kwargs ))
    print("Third value is {third}".format(  **kwargs ))

kwargs_test(first = 3, second = 4, third = 5)
#kwargs_test(n1 = 3, n2 = 4, n3 = 5)  # error


#%%
def kwargs_test( *kwargs ):
    print(kwargs)
    print("First value is {0}".format( *kwargs ))
    print("Second value is {1}".format(  *kwargs ))
    print("Third value is {2}".format(  *kwargs ))

kwargs_test(3,  4,  5) #리스트
#kwargs_test(n1 = 3, n2 = 4, n3 = 5)  # error, 딕셔너리
# 디폴트 인수 (default arguments)

#%%
def print_something(my_name, your_name='park'):
    print("Hello {}, My name is {}".format(your_name, my_name))

print_something("kim", "lee")
print_something("kim")
print_something(my_name="kim")




#%%
"""
# 가변 인수 (variable arguments)
"""
#%%
def vararg_test(a, b, *args ):
    print(args)

print(vararg_test(1, 2, 3, 4, 5))  # 3,4,5


#%%
def vararg_test(a, b, *args ): #튜플이다. 
    print(args)
    [*c] = args#튜플의 내용을 리스트(c)로 바꾸겠다. 
    c[1] = 44
    print(c)
#   d = args
#    print(args, c, d)
	 

print(vararg_test(1, 2, 3, 4, 5))  # 3,4,5


