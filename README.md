Jalali.py
=========

Jalali.py is a simple Python code for converting between Persian date and Gregorian date. It is a port of http://jdf.scr.ir/ (PHP).

Sample Usage
--------

```python
>>> import jalali

>>> jalali.Persian('1393-1-11').gregorian_string()
'2014-3-31'
>>> jalali.Persian(1393, 1, 11).gregorian_datetime()
datetime.date(2014, 3, 31)
>>> jalali.Persian('1393/1/11').gregorian_string("{}/{}/{}")
'2014/3/31'
>>> jalali.Persian((1393, 1, 11)).gregorian_tuple()
(2014, 3, 31)

>>> jalali.Gregorian('2014-3-31').persian_string()
'1393-1-11'
>>> jalali.Gregorian('2014,03,31').persian_tuple()
(1393, 1, 11)
>>> jalali.Gregorian(2014, 3, 31).persian_string("{0}")
'1393'
```

Original License
----------------
As mentioned in http://jdf.scr.ir/, the original code is free and open source, and you are not allowed to sell it. You can read more in http://jdf.scr.ir/.