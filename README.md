# sinablog-collect-python-cmd
新浪博客文章下载工具,简单有效的下载命令行小工具,采用获取前一篇的方式下载所有文章

### 运行说明
先确保运行环境已经安装了python 3.x版本(建议使用win7及以上的系统,xp存在一定的问题比如还需要更新pip和安装vc 2010,动手能力强自行折腾)  
程序依赖第三方库BeautifulSoup和lxml,如果环境没有,请先在命令行执行 pip install bs4 和 pip install lxml 进行安装(如果无法执行pip,请将python目录和其下的Scripts添加到环境变量中)  
然后运行sinablog_collect.py  
命令行提示后输入需要开始下载博文的地址,回车执行即可  
下载完成后到文件所在目录下查看对应的时间戳目录,程序按照执行时刻创建时间戳目录,不会重复,目录下存放下载好的html文件

测试地址参考: http://blog.sina.com.cn/s/blog_62e211ef0100rsu1.html

友情提示: 由于是批量下载,对新浪博客网站存在一定的压力,因此可能触发反爬虫机制,用多了会造成一定时间的被禁止访问(当然了,停一会就会恢复),因此不要在短时间内太过频繁的使用该软件


### 建议和改进
1. github提issue
2. 发送邮件到 bituplink@protonmail.com


### 捐助
如果觉得程序对你有帮助或者想要支持我,可以小额赞助下

方式一: 支付宝捐助
* ![alipay](http://www.bituplink.com/assets/img/alipay.png)

方式二: 微信捐助
* ![wxpay](http://www.bituplink.com/assets/img/wxpay.png)

