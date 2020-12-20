Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4,5,6]
>>> l
[1, 2, 3, 4, 5, 6]
>>> type(l)
<class 'list'>
>>> print(type(l))
<class 'list'>
>>> id(l)
1625530265408
>>> l.append(80)
>>> id(l)
1625530265408
>>> print(l,id(l))
[1, 2, 3, 4, 5, 6, 80] 1625530265408
>>> #so lists are muatable
>>> #here mutable is nothing but you can edit(modify) the data type in same location
>>> l=[1,2,3,4,5,6]
>>> l
[1, 2, 3, 4, 5, 6]
>>> id(l)
1625535710272
>>> l.append('arun')
>>> l
[1, 2, 3, 4, 5, 6, 'arun']
>>> l.append('kumar;)
	 
SyntaxError: EOL while scanning string literal
>>> l.append('kumar')
>>> l
[1, 2, 3, 4, 5, 6, 'arun', 'kumar']
>>> l.append(60.888)
>>> l
[1, 2, 3, 4, 5, 6, 'arun', 'kumar', 60.888]
>>> l.append(complex(1,2))
>>> l
[1, 2, 3, 4, 5, 6, 'arun', 'kumar', 60.888, (1+2j)]
>>> a='arun kumar'
>>> a
'arun kumar'
>>> #TUPLES
>>> l=[]
>>> l
[]
>>> type(l)
<class 'list'>
>>> t=()
>>> t=(1,2,3,4,5,6)
>>> t
(1, 2, 3, 4, 5, 6)
>>> type(t)
<class 'tuple'>
>>> id(t)
1625534745472
>>> t=(2,3,4)
>>> id(t)
1625535655040
>>> t=(1,'arun',1.3,complex(1,2),[1,2,3,4,5,6,'kumar',21.96,complex(6,5)])
>>> t
(1, 'arun', 1.3, (1+2j), [1, 2, 3, 4, 5, 6, 'kumar', 21.96, (6+5j)])
>>> t[0]
1
>>> t[4]
[1, 2, 3, 4, 5, 6, 'kumar', 21.96, (6+5j)]
>>> t[4][4]
5
>>> #tuples and lists are same but main difference is tuples are immutable whether lists are mutable.
>>> #we can use tuples when the user don't need to over write it.
>>> #DICTIONARIES
>>> ###dictionaries are also called as hashmaps
>>> #it stores the values in key value apirs
>>> d
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> d={'name':arun}
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    d={'name':arun}
NameError: name 'arun' is not defined
>>> d={'name':'arun'}
>>> d
{'name': 'arun'}
>>> d={'name':'arun','age'=90}
SyntaxError: invalid syntax
>>> d={'name':'arun','age':90}
>>> d[age]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    d[age]
NameError: name 'age' is not defined
>>> d['age']
90
>>> id(d)
1625535699904
>>> d.update('sur name','kumar')
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d.update('sur name','kumar')
TypeError: update expected at most 1 argument, got 2
>>> d.update(('surname','kumar'))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d.update(('surname','kumar'))
ValueError: dictionary update sequence element #0 has length 7; 2 is required
>>> help(d.update)
Help on built-in function update:

update(...) method of builtins.dict instance
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]

>>> id(d)
1625535699904
>>> d={'name':'arun','age':90,'surname':'kumar'}
>>> d
{'name': 'arun', 'age': 90, 'surname': 'kumar'}
>>> id(d)
1625535700928
>>> 