Jalali.py
=========

Jalali.py is a simple Python code for converting between Jalali date and Gregorian date. It is a port of http://jdf.scr.ir/ (PHP).

Sample Usage
--------

```python
>>> import jalali
>>> jalali.convert_to_gregorian('1393-1-11')
datetime.date(2014, 3, 31)
>>> jalali.convert_to_jalali('2014-3-31')
'1393-1-11'
>>> import datetime
>>> today = datetime.date(2014, 5, 7)
>>> jalali.convert_to_jalali(today)
'1393-2-17'
```

Original License
----------------
As mentioned in http://jdf.scr.ir/, the original code is free and open source, and you are not allowed to sell it. You can read more in http://jdf.scr.ir/.