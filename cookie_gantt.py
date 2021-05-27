# -*- coding: utf-8 -*-
"""
Created on Sun May 23 14:46:09 2021

@author: Sebastian
"""

import plotly.express as px
#import pandas as pd
import datetime

#df = pd.DataFrame([
#    dict(Task = "Task A", Start = '2000-01-01 00:00.00', Finish = '2000-01-01 00:00.50')])

tasks = ["Task A", 'Task B', 'Task C', 'Task D', 'Task E', 'Task F', 'Task G',\
        'Task H', 'Task I', 'Task J', 'Task K']

start1 = [0,0,0,379.16,825,1431.66,515,1165,1590,1740,1740]
end1 = [940,515,379.16,509.16,1165,1590,825,1431.66,1740,2950,2340]
crit1 = [False,True,False,False,True,True,True,True,True,True,False]
c, n = "Critical path", "Non-critical path"
crit1 = [n,c,n,n,c,c,c,c,c,c,n]


start2 = [0,0,0,379.16,0,340,515,825,1091.66,1241.66,1241.66]
end2 = [940,515,379.16,509.16,340,498.33,825,1091.66,1241.66,2451.66,1841.66]
crit2 = [n,c,n,n,n,n,c,c,c,c,n]
def times(start, end):
    min_start = []
    min_end = []
    start_tim = []
    end_tim = []
    span = []
    for i in start:
        min_start.append(str(datetime.timedelta(seconds=i)))
    for i in end:
        min_end.append(str(datetime.timedelta(seconds=i)))
    for i in min_start:
        start_tim.append('1990-01-01 {}'.format(i))
    for i in min_end:
        end_tim.append('1990-01-01 {}'.format(i))
    for i in range(11):
        span.append('{}-{}'.format(min_start[i], min_end[i]))
    return(start_tim, end_tim, span)
'''start_str = ['0','0','0','379.1667','825','1431.66','515','1165','1323.33',\
             '1473.33','1473.33']
end_str = ['940','515','379.1667','509.1667','1165','1590','825','1431.66',\
           '1473.33','2683.33','2073.33']'''
def make_gantt(x_start, x_end, y, color, name, text, range_x=None):
    fig = px.timeline(x_start=x_start, x_end=x_end, y=y, color=color,\
                      text=text, range_x = range_x)
    fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
    fig.write_image("D:/Python/Projects/Python 8/{}.png".format(name))
start_tim1, end_tim1, span1 = times(start1, end1)
make_gantt(start_tim1, end_tim1, tasks, crit1, "single_baker_gantt", span1)
start_tim2, end_tim2, span2 = times(start2, end2)
make_gantt(start_tim2, end_tim2, tasks, crit2, "double_baker_gantt", span2,\
           range_x = ['1990-01-01 00:00:00','1990-01-01 01:15:00'])

