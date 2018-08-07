
# coding: utf-8

# In[1]:


#获取标题 的函式
def GetTitle():
    global item
    item=[]
    for title in soup.select('.jzList-txt-t'):
        item.append(title.text.strip())
    return item


# In[2]:


#获取薪酬和结算方式，并整理 的函式
def GetMoney():
    whatsup={}
    paid=[]
    settlement=[]
    Money = []
    money = soup.select('.jzList-salary span')
    for money in money:
        Money.append(money.text)
    for i in range(0,len(Money)):
        if i%2==0:
            paid.append(Money[i])
        else:
            settlement.append(Money[i])
    whatsup['paid']=paid
    whatsup['settlement']=settlement
    return whatsup


# In[4]:


#获取工作时间、工作类型、地点、招聘人数 的函式
def GetBanana():
    man = {}
    number=[]
    place=[]
    mold=[]
    time=[]
    apple = soup.select('.jzList-txt')
    for i in range(0,len(item)):
        for j in range(0,4):
            banana = apple[i].select('li')[j].text.replace(' ', '').replace('\n', '')
            if j%4==0:
                time.append(banana.lstrip('工作时间：'))
            elif j%4==1:
                mold.append(banana.lstrip('兼职类型：'))
            elif j%4==2:
                place.append(banana.lstrip('工作地点：'))
            else: number.append(banana.lstrip('招聘人数：').rstrip('人'))
    
    
    man['time']=time
    man['mold']=mold
    man['place']=place
    man['number']=number
    
    return man


# In[5]:


def GetParttimejob(url):
    result={}
    global res,soup
    res = requests.get(url)
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    item = GetTitle()
    whatsup = GetMoney()
    man = GetBanana()
    result['item']=item
    result['paid']=whatsup['paid']
    result['settlement']=whatsup['settlement']
    result['time']=man['time']
    result['mold']=man['mold']
    result['place']=man['place']
    result['number']=man['number']
    return result


# In[6]:


def main(city):
    for i in range(1,61):
        url = original_url.format(i)
        result = GetParttimejob(url)
        result = [result]
        total.extend(result)
    
    list1 = total
    list2 = defaultdict(list)
    #print(type(list2),list2)
    [list2[k].extend(v) for i in list1 for k, v in i.items()]
    #dict(list2)
    df = pandas.DataFrame(list2)
    filename = original_filename.format(city)
    df.to_excel(filename)
    print(city)


# In[7]:


import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import pandas


res=[]
soup=[]
total = []
original_url = 'http://www.doumi.com/sz/o{}/'
original_filename = "D:\\2大创\论文\Parttimejob_{}.xlsx"

for i in ['bj','gz','sh','sz']:
    main(i)

