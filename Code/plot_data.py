# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 01:11:24 2022

@author: Nexus Long
"""

import pyecharts.options as opts
from pyecharts.charts import WordCloud,Timeline,Bar,Grid,Page
import pandas as pd
from pyecharts.faker import Faker
#%%
x = Faker.choose()
tl = Timeline(init_opts=opts.InitOpts(width="100%", height="600px"))
totaldic={}
#%%
for i in range(568,607):
    data=pd.read_excel('data.xlsx',sheet_name=str(i))
    data_1=data.drop(columns=['Unnamed: 0','title'])
    tmp=data_1.values.reshape(-1, 1)
    tmp=tmp[~pd.isnull(tmp)]
    dic={}
    for m in range(len(tmp)):
        try:
            dic[tmp[m]]+=1
        except:
            dic[tmp[m]]=1
    data=list(zip(dic.keys(),dic.values()))
    data.sort(key=lambda data:data[1],reverse=True)
    tmp={d[0]:d[1]+totaldic.get(d[0],0) for d in data}
    totaldic=tmp
    x_data=[d[0] for d in data if d[1]>2]
    y_data=[d[1] for d in data if d[1]>2]
    g1=(
        WordCloud()
        .add(series_name="热点分析", data_pair=data,pos_left='40%',width='60%')
        .set_global_opts(
            title_opts=opts.TitleOpts(title="热点分析",pos_left='50%'),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    b1 = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis('',y_data,category_gap='80%')        
    .set_global_opts(
            datazoom_opts=[opts.DataZoomOpts(pos_bottom='10%')],)
    )
    grid = Grid()
    grid.add(b1, grid_opts=opts.GridOpts(pos_left='5%',pos_right='65%',pos_bottom='10%'))
    grid.add(g1, grid_opts=opts.GridOpts())
    if i<=600:
        tl.add(grid, "21年第{}周".format(i-548))
    else:
        tl.add(grid,"22年第{}周".format(i-600))
#%%
data=list(zip(totaldic.keys(),totaldic.values()))
data.sort(key=lambda data:data[1],reverse=True)
x_data=[d[0] for d in data if d[1]>2]
y_data=[d[1] for d in data if d[1]>2]
g1=(
        WordCloud()
        .add(series_name="总统计", data_pair=data,pos_left='40%',width='60%')
        .set_global_opts(
            title_opts=opts.TitleOpts(title="总分析",pos_left='50%'),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
b1 = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis('',y_data,category_gap='80%')        
    .set_global_opts(
            datazoom_opts=[opts.DataZoomOpts(pos_bottom='10%')],)
    )
grid = Grid(init_opts=opts.InitOpts(width="100%", height="600px"))
grid.add(b1, grid_opts=opts.GridOpts(pos_left='5%',pos_right='65%',pos_bottom='10%'))
grid.add(g1, grid_opts=opts.GridOpts())
p=Page()
p.add(tl,grid)
p.render("timeline_bar.html")
