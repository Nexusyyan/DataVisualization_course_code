from bs4 import BeautifulSoup
import os
for i in range(586,587):
    workname=str(i)
    if os.path.exists('text/text'+workname+'.txt'):
        with open('text/text'+workname+'.txt','r',encoding='utf-8') as f:
             content = f.read()
        soup = BeautifulSoup(content, 'lxml')
        x=soup.find_all(name='a')
        text=[xx.text for xx in x]
        href=[xx['href'].lstrip('//www.bilibili.com/video/') for xx in x]
        out_file=open('data/data'+workname+'.txt',mode='w+',encoding='utf-8')
        for i in range(len(text)):
            out_file.write(str(len(text)-i)+'\t'+text[i]+'\t'+href[i]+'\n')
        out_file.close()