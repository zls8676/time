#! /usr/bin/env python
#-*-coding=utf-8-*-
#写一个函数，计算给定日期是该年的第几天．

def dayOfYear(year,month,day):
    dayOfYear = 0
    #判断该年是平年还是闰年
    if year%400==0 or (year%4==0 and year%100!=0):
        print('%d年是闰年，2月份有29天！'%year)
        li1 = [31,29,31,30,31,30,31,31,30,31,30,31]
        for i in range(month-1):
            dayOfYear += li1[i]
        return dayOfYear+day
    else:
        print('%d年是平年，2月份有29天！' % year)
        li2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(month-1):
            dayOfYear +=li2[i]
        return dayOfYear+day


if __name__ == "__main__":
    year = int(input('请输入年份：'))
    month = int(input('请输入月份：'))
    day = int(input('请输入日期：'))
    dayOfYear = dayOfYear(year,month,day)
    print('%d年%d月%d日是今年的第%d天！'%(year,month,day,dayOfYear))