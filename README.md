# 爬虫练习
 
## *注意* ##
在您运行爬虫前  
请明确相关法律条款  
以及道德约束  
本人不承担运行这些程序造成的**任何后果**  
  
*ps*:很多程序需要配置相关环境  
直接运行大概率会报错  
搞不定就联系我吧
## 指南 ##
个人练习用  
想要看看的自便  


----------

### basic文件夹 ###
基础语法训练  
没有多大价值  

----------

### 豆瓣top250 ###
**功能：**  
爬取豆瓣top250电影信息  
图片保存在本地  
信息输出在终端  
**技术点：**  
1. BeautifulSoup  
2. urllib.request + requests  
3. 伪装请求头  
4. 线程池

----------
### 当当top500 ###
**功能：**  
爬取当当图书top500  
图片保存在本地  
文字信息支持txt，xls写入  
**技术点：**  
1. 伪装  
2. 正则表达式  
3. requests

----------

### 哔哩哔哩自动搜索 ###
**功能：**  
使用者给出关键词  
自动搜索相关内容  
爬取相关信息（标题、链接……）  
xls文件保存在本地  
**技术点：**  
1. selenium + chrome （headless）/PhantomJS  
2. CSS_SELECTOR  
3. XPATH  
4. BeautifulSoup

----------
### 秋名山一号 ###  
**功能略**  
**技术点：**  
1. selenium + chrome （headless）/PhantomJS  
2. ProxyPool + redis  
（https://github.com/Python3WebSpider/ProxyPool）  
3. XPATH  
4. BeautifulSoup  
5. 伪装请求头  
6. 线程池  
7. requests




