import requests
from bs4 import BeautifulSoup

# 配置请求头
headers={
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
     }

# 网站诗词内容下载
def neirong(url):
    #获取标题正文页数据
    gethtml = requests.get(url,headers=headers).text
    soup = BeautifulSoup(gethtml,'html.parser')
    #解析获得标签
    ele = soup.find('div',class_='chapter_content')
    content = ele.text #获取标签中的数据值
    return content

if __name__ == "__main__":
     url = 'http://www.shicimingju.com/book/hongloumeng.html'
     reponse = requests.get(url=url,headers=headers)
     page_text = reponse.text

     #创建soup对象
     soup = BeautifulSoup(page_text,'html.parser')
     #解析数据
     mulu = soup.select('.book-mulu > ul > li > a')   #过滤目录含文字-->列表中
     print(mulu)
     cap = 1
     # for i in mulu:
     #     print(i.string,i['href'])
     for ele in mulu:
         print('开始下载第%d章节'%cap)
         cap+=1
         title = ele.string          #取列表中的字符串，并没有取字母，很智能，比re进步了许多
         wanzheng_url = 'http://www.shicimingju.com'+ele['href'] #取变量的值 =
         content = neirong(wanzheng_url)

         with open('.\\红楼梦.txt','a',encoding='utf-8') as fp:
             fp.write(title+":"+content+'\n\n\n\n\n')
             print('结束下载第%d章节'%cap)