import requests
from bs4 import BeautifulSoup

# 配置请求头
headers={
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
     }

# 网站诗词内容下载
url='http://www.shicimingju.com/book/hongloumeng/54.html'
#获取标题正文页数据
gethtml = requests.get(url,headers=headers).text
soup = BeautifulSoup(gethtml,'html.parser')
#解析获得标签
ele = soup.find('div',class_='book-page-nav')    #按照参数div取div段，名称是class_指定的
# ele = soup.find('div',class_='chapter_content')
# ele = soup.find('div',class_='chapter_content')
# print(ele)
content = ele.text #获取标签中的数据值
print(content)