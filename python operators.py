Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #arithametic operators
>>> a=10
>>> # arithmetic operators are +,-,*,/,//,**,%
>>> a=10
>>> b=20
>>> a+b
30
>>> a-b
-10
>>> a*b
200
>>> a**b
100000000000000000000
>>> a/b
0.5
>>> a//b
0
>>> a%b
10
>>> a=10
>>> a
10
>>> a=10
>>> b=20
>>> a<b
True
>>> a>b
False
>>> a==b
False
>>> a!=b
True
>>> a,=b
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a,=b
TypeError: cannot unpack non-iterable int object
>>> a<=b
True
>>> a>=b
False
>>> # arithmetic operators are +,-,*,/,//,**,%
>>> #comparision operators are <,>,<=,>=,==,!=
>>> #identity operators is , is not
>>> a=10
>>> b=10
>>> a==10
True
>>> a is b
True
>>> a is not b
False
>>> l=[10,20,30,40,50]
>>> l2=[10,20,30,40,50]
>>> l == l2
True
>>> l is l2
False
>>> ## what happend here is the comparision operators are compare the values but identity operators are compare the memory locations
>>> ##when a=10 b=10 both are went to same memory location becuase immutable but lists are mutable so is not equal to ==
>>> #Assignment operators are =,+=,-=,*=,/=
>>> a=10
>>> a
10
>>> #the above code is a example of = operator it aleays assign a right value to a left variable
>>> a+=10
>>> a
20
>>> a-=10
>>> a
10
>>> a*=10
>>> a
100
>>> a/=10
>>> a
10.0
>>> a//=10
>>> a
1.0
>>> #The assignment operators are used for perform some functions on own variable
>>> #python also suuports a bitwise operators
>>> #the bitwise operators are &,|,^,>>,<<
>>> a=1
>>> b=2
>>> a&b
0
>>> a|b
3
>>> a=1
>>> b=1
>>> a&b
1
>>> 
>>> 
>>> a=10
>>> a
10
>>> b=20
>>> b
20
>>> c=30
>>> c
30
>>> 
>>> a=10
>>> a
10
>>> b=20
>>> a=10
>>> b=20
>>> a&b
0
>>> a=10
>>> b=10
>>> a&b
10
>>> a&b
10
>>> a|b
10
>>> a=10
>>> b=10
>>> a|b
10
>>> a=5
>>> b=5
>>> a|b
5
>>> a||b
SyntaxError: invalid syntax
>>> a|b
5
>>> print(a|b)
5
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=10
>>> a
10
>>> a
10
>>> a
10
>>> a
10
a
>>> 
>>> a
10
>>> b=20
>>> 
>>> b
20
>>> c=30
>>> c
30
>>> a
10
>>> dela
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    dela
NameError: name 'dela' is not defined
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=10
>>> a
10
>>> a=20
>>> a
20
>>> 
====================================================================================== RESTART: Shell ======================================================================================
>>> a=30
'
>>> a
30
>>> a
30
>>> a
30
>>> #operators
>>> a=10
>>> b=20
>>> a&b
0
>>> a|b
30
>>> bin(10)
'0b1010'
>>> bin(100)
'0b1100100'
>>> not(True)
False
>>> not(10)
False
>>> 
>>> 
>>> 
>>> #Arithmatic operators
>>> #the arithmatic operators are +,-,*,/,//,**,%
>>> #The arithmatic operators are used for perform some mathematical functions
>>> a=10
>>> b=20
>>> a+b
30
>>> a-b
-10
>>> a
10
>>> a/b
0.5
>>> a//b
0
>>> a%b
10
>>> a**b
100000000000000000000
>>> #Comparision operators
>>> #comparision operators are used for comparing expressions and data types
>>> a=10
>>> b=20
>>> a<b
True
>>> a>b
False
>>> a<=b
True
>>> a>=b
False
>>> a==b
False
>>> a!=b
True
>>> #Identity operators
>>> #Is and Is not
>>> a=10
>>> b=20
>>> a is b
False
>>> a=20
>>> a is b'
SyntaxError: EOL while scanning string literal
>>> a is b
True
>>> #So from above instance we can feel that == and is are same but no why because is compares memory location where== compares the values
>>> # have a example
>>> l=[10,20,30]
>>> l2=[10,20,30]
>>> l == l2
True
>>> l is l2
False
>>> l is not l2
True
>>> a is b
True
>>> #Assignment operators
>>> #Assignment operators are =,+=,-=,*=
>>> a=10
>>> b=20
>>> c=a
>>> c
10
>>> a=5
>>> a
5
>>> #when if use = it means right aasign to left variable
>>> a=10
>>> a
10
>>> a+=5
>>> a
15
>>> a-=5
>>> a
10
>>> a*=5
>>> a
50
>>> a*/=5
SyntaxError: invalid syntax
>>> a/=5
>>> a
10.0
>>> here the
SyntaxError: invalid syntax
>>> #here the assignmebt operators are used for perform the some action on it's own variable
>>> #Bitwise operators
>>> #Bitwise operators are used for perform action on single bit
>>> a=10
>>> bin(a)
'0b1010'
>>> b=20
>>> a&b
0
>>> a=10
>>> b=10
>>> a&b
10
>>> a|b
10
>>> a^b
0
>>> a>>2
2
>>> a
10
>>> a<<3
80
>>> #logical operators
>>> #those are and or not
>>> #these operators are used between comparision expressions
>>> a=10
>>> b=20
>>> a==10 and b==20
True
>>> a==90 and b==20
False
>>> a==90 or b==20
True
>>> a==10 or b==20
True
>>> a==5 or b==9
False
>>> #Membership operators
>>> # in notin always print boolean
>>> l=[1,2,3,4,5,6,7,8]
>>> 3 in l
True
>>> 90 in l
False
>>> not(900 in l)
True
>>> 500 not in l
True
>>> 