import requests,re,time,random,pandas
from bs4 import BeautifulSoup

st=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
baseurl = 'https://www.lagou.com/zhaopin/suanfagongchengshi/{}/?filterOption=3'
url = []
headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
for i in range(1,31):
    pageurl = baseurl.format(i)
    #print(url)
    res = requests.get(pageurl,headers=headers,timeout=10)
    soup = BeautifulSoup(res.text,'lxml')
    url.extend([i['href'] for i in soup.select('.position_link')])
    time.sleep(10)

count=0
result={}
result['url'],result['txt'],result['title']=[],[],[]

for i in url:
    try:
        count=count+1
        #print(count)
        #print(i)
        res = requests.get(i,headers=headers,timeout=10)
        soup = BeautifulSoup(res.text,'lxml')
        if soup.select('.job_bt'):
            txt = soup.select('.job_bt')[0].text.replace('\n','').replace(' ','').replace('\xa0','').replace(',','，')
        else:
            txt='NONE'
        result['url'].append(i)
        result['txt'].append(txt)
        result['title'].append('算法工程师')
        time.sleep(15)
        #if count>9:
        #    break
    except Exception as e:
        print(e)
        time.sleep(60*3)

savefile = 'lagou_suanfagongchengshi.csv'
df = pandas.DataFrame(result)
df.to_csv(savefile,encoding="utf_8_sig")
ed=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print('start time：',st,'\n','end time：',ed)
