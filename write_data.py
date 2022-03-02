import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
for l in range(586,587):
    shname=str(l)
    if l !=599:
        t=pd.read_csv('data/data'+shname+'.txt',sep='\t',names=['rank','title','bvalue'])
        tag=pd.DataFrame(columns=range(30))
        for i in range(len(t)):
            r = requests.get(url='https://www.bilibili.com/video/'+t.iloc[i][2])
            soup = BeautifulSoup(r.text, 'lxml')
            x=[t.iloc[i][1]]
            for ul in soup.find_all(name='a',attrs='tag-link'):
                x.append(ul.text.split()[0])
            x=pd.DataFrame(x).T
            x.index=[t.iloc[i][0]]
            tag=pd.concat([tag,x],axis=0)
        tmp=list(tag.columns)
        tmp[0]='title'
        for n in range(1,30):
            tmp[n]='tag'+str(n)
        tmp=tag.reindex(columns=tmp)
        tmp['title']=tag[0]
        for o in range(1,30):
            tmp['tag'+str(o)]=tag[o]
        tag=tmp
        if not os.path.exists('data.xlsx'):
            tag.to_excel('data.xlsx',sheet_name=shname)
        else:
            with pd.ExcelWriter('data.xlsx', engine='openpyxl',mode='a') as writer:
                tag.to_excel(writer,shname)
