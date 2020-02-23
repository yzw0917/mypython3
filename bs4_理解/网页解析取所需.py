from bs4 import BeautifulSoup
import requests


url='http://www.baojinews.com/'
res=requests.get(url).content
soup=BeautifulSoup(res,'html.parser',from_encoding='uft-8')
reslut=soup('a') #soup.find_all简写形式 标签a
reslut=soup.get_text('title') # 获得标签中的文本内容
reslut=soup.get('body')  # 获得标签的属性内容
print(reslut)

