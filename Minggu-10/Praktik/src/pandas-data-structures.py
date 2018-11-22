Microsoft Windows [Version 10.0.16299.19]
(c) 2017 Microsoft Corporation. All rights reserved.

C:\Users\Ongen>python
Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 02:47:15) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> import pandas as pd

>>> s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
>>> s
a    0.383621
b    0.472118
c    0.286304
d    0.215361
e   -0.642872
dtype: float64
>>> s.index
Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
>>> pd.Series(np.random.randn(5))
0    0.510612
1    0.673710
2   -1.329856
3    0.545027
4    0.319763
dtype: float64
>>> d = {'b' : 1, 'a' : 0, 'c' : 2}
>>> pd.Series(d)
b    1
a    0
c    2
dtype: int64
>>>
>>>
>>> pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
a    5.0
b    5.0
c    5.0
d    5.0
e    5.0
dtype: float64
>>>
>>> s[0]
0.3836206563951815
>>>
>>> s[:3]
a    0.383621
b    0.472118
c    0.286304
dtype: float64
>>> s[s > s.median()]
a    0.383621
b    0.472118
dtype: float64
>>> s[[4, 3, 1]]
e   -0.642872
d    0.215361
b    0.472118
dtype: float64
>>> np.exp(s)
a    1.467589
b    1.603386
c    1.331497
d    1.240310
e    0.525780
dtype: float64
>>> s + s
a    0.767241
b    0.944235
c    0.572607
d    0.430723
e   -1.285744
dtype: float64
>>> s * 2
a    0.767241
b    0.944235
c    0.572607
d    0.430723
e   -1.285744
dtype: float64
>>> np.exp(s)
a    1.467589
b    1.603386
c    1.331497
d    1.240310
e    0.525780
dtype: float64
>>> s = pd.Series(np.random.randn(5), name='lourenson')
>>> s
0    0.069197
1   -0.187390
2    0.827349
3    1.892401
4   -1.064557
Name: lourenson, dtype: float64
>>> s2 = s.rename("saptenno")
>>> s2.name
'saptenno'
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
... 'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
>>> df = pd.DataFrame(d)
>>> df
   one  two
a  1.0  1.0
b  2.0  2.0
c  3.0  3.0
d  NaN  4.0
>>> pd.DataFrame(d, index=['d', 'b', 'a'])
   one  two
d  NaN  4.0
b  2.0  2.0
a  1.0  1.0
>>> pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
   two three
d  4.0   NaN
b  2.0   NaN
a  1.0   NaN
>>>
>>> d = {'one' : [1., 2., 3., 4.],
... 'two' : [4., 3., 2., 1.]}
>>> pd.DataFrame(d)
   one  two
0  1.0  4.0
1  2.0  3.0
2  3.0  2.0
3  4.0  1.0
>>>
KeyboardInterrupt
>>> pd.DataFrame(d, index=['a', 'b', 'c', 'd'])
   one  two
a  1.0  4.0
b  2.0  3.0
c  3.0  2.0
d  4.0  1.0
>>> data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
>>> data[:] = [(1,2.,'Hello'), (2,3.,"World")]
>>>
>>> pd.DataFrame(data)
   A    B         C
0  1  2.0  b'Hello'
1  2  3.0  b'World'
>>> pd.DataFrame(data, index=['first', 'second'])
        A    B         C
first   1  2.0  b'Hello'
second  2  3.0  b'World'
>>> pd.DataFrame(data, columns=['C', 'A', 'B'])
          C  A    B
0  b'Hello'  1  2.0
1  b'World'  2  3.0
>>>
>>> data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
>>> pd.DataFrame(data2)
   a   b     c
0  1   2   NaN
1  5  10  20.0
>>> pd.DataFrame(data2, index=['first', 'second'])
        a   b     c
first   1   2   NaN
second  5  10  20.0
>>> pd.DataFrame(data2, columns=['a', 'b'])
   a   b
0  1   2
1  5  10
>>> pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
... ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
... ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
... ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
... ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
       a              b
       b    a    c    a     b
A B  1.0  4.0  5.0  8.0  10.0
  C  2.0  3.0  6.0  7.0   NaN
  D  NaN  NaN  NaN  NaN   9.0
>>> pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]))
   A  B
0  1  4
1  2  5
2  3  6
>>> data
array([(1, 2., b'Hello'), (2, 3., b'World')],
      dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])
>>> pd.DataFrame.from_records(data, index='C')
          A    B
C
b'Hello'  1  2.0
b'World'  2  3.0
>>> df['one']
a    1.0
b    2.0
c    3.0
d    NaN
Name: one, dtype: float64
>>> df['three'] = df['one'] * df['two']
>>> df['flag'] = df['one'] > 2
>>> df
   one  two  three   flag
a  1.0  1.0    1.0  False
b  2.0  2.0    4.0  False
c  3.0  3.0    9.0   True
d  NaN  4.0    NaN  False
>>> del df['two']
>>> three = df.pop('three')
>>> df
   one   flag
a  1.0  False
b  2.0  False
c  3.0   True
d  NaN  False
>>> df['foo'] = 'bar'
>>> df
   one   flag  foo
a  1.0  False  bar
b  2.0  False  bar
c  3.0   True  bar
d  NaN  False  bar
>>>
