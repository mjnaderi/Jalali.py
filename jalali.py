# In The Name Of Allah
#
# Jalali date converter
# Ported from PHP (http://jdf.scr.ir/) to Python (2&3) by Mohammad Javad Naderi <mjnaderi@gmail.com>
#
# As mentioned in http://jdf.scr.ir/, the original code is free and open source,
# and you are not allowed to sell it. You can read more in http://jdf.scr.ir/.
#
# Original License Notes:
#
#    /** Software Hijri_Shamsi , Solar(Jalali) Date and Time
#    Copyright(C)2011, Reza Gholampanahi , http://jdf.scr.ir
#    version 2.55 :: 1391/08/24 = 1433/12/18 = 2012/11/15 */
#
#    /** Convertor from and to Gregorian and Jalali (Hijri_Shamsi,Solar) Functions
#    Copyright(C)2011, Reza Gholampanahi [ http://jdf.scr.ir/jdf ] version 2.50 */
#
# Example Usage:
#  >>> import jalali
#  >>> jalali.convert_to_gregorian('1393-1-11')
#  datetime.date(2014, 3, 31)
#  >>> jalali.convert_to_persian('2014-3-31')
#  '1393-1-11'
#  >>> import datetime
#  >>> today = datetime.date(2014, 5, 7)
#  >>> jalali.convert_to_persian(today)
#  '1393-2-17'

import re
import datetime


def convert_to_persian(date):

    # Parse date
    if type(date) is str:
        m = re.match(r'^(\d{4})-(\d{1,2})-(\d{1,2})$', date)
        if m:
            [year, month, day] = [int(m.group(1)), int(m.group(2)), int(m.group(3))]
        else:
            raise Exception("Invalid Input String")
    elif type(date) is datetime.date:
        [year, month, day] = [date.year, date.month, date.day]
    else:
        raise Exception("Invalid Input Type")

    # Check the validity of input date
    try:
        datetime.datetime(year, month, day)
    except:
        raise Exception("Invalid Date")

    # Convert date to Jalali
    d_4 = year % 4
    g_a = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    doy_g = g_a[month] + day
    if d_4 == 0 and month > 2:
        doy_g += 1
    d_33 = int(((year - 16) % 132) * .0305)
    a = 286 if (d_33 == 3 or d_33 < (d_4 - 1) or d_4 == 0) else 287
    if (d_33 == 1 or d_33 == 2) and (d_33 == d_4 or d_4 == 1):
        b = 78
    else:
        b = 80 if (d_33 == 3 and d_4 == 0) else 79
    if int((year - 10) / 63) == 30:
        a -= 1
        b += 1
    if doy_g > b:
        jy = year - 621
        doy_j = doy_g - b
    else:
        jy = year - 622
        doy_j = doy_g + a
    if doy_j < 187:
        jm = int((doy_j - 1) / 31)
        jd = doy_j - (31 * jm)
        jm += 1
    else:
        jm = int((doy_j - 187) / 30)
        jd = doy_j - 186 - (jm * 30)
        jm += 7
    return "{}-{}-{}".format(jy, jm, jd)


def convert_to_gregorian(date):

    # Parse date
    m = re.match(r'^(\d{4})-(\d{1,2})-(\d{1,2})$', date)
    if m:
        [year, month, day] = [int(m.group(1)), int(m.group(2)), int(m.group(3))]
    else:
        raise Exception("Incorrect Date Format")

    # Check validity of date. TODO better check
    if month > 12 or day > 31:
        raise Exception("Incorrect Date")

    # Convert date
    d_4 = (year + 1) % 4
    if month < 7:
        doy_j = ((month - 1) * 31) + day
    else:
        doy_j = ((month - 7) * 30) + day + 186
    d_33 = int(((year - 55) % 132) * .0305)
    a = 287 if (d_33 != 3 and d_4 <= d_33) else 286
    if (d_33 == 1 or d_33 == 2) and (d_33 == d_4 or d_4 == 1):
        b = 78
    else:
        b = 80 if (d_33 == 3 and d_4 == 0) else 79
    if int((year - 19) / 63) == 20:
        a -= 1
        b += 1
    if doy_j <= a:
        gy = year + 621
        gd = doy_j + b
    else:
        gy = year + 622
        gd = doy_j - a
    for gm, v in enumerate([0, 31, 29 if (gy % 4 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]):
        if gd <= v:
            break
        gd -= v
    return datetime.date(gy, gm, gd)