# wb-spider

新浪微博爬虫，用python爬取新浪微博近30天文章数据

本程序可以连续爬取30天微博号的文章数据，并将结果信息写入文件。写入信息包括文章的内容、发布时间、点赞量、转发量等数据。此版本为免cookie版，也可加上cookie。
写入文件类型为json文件（默认)
<h2>获取到的字段</h2>
微博信息
<ul>
<li>微博内容：微博正文</li>
<li>头条文章url：微博中头条文章的url，若微博中不存在头条文章，则值为''</li>
<li>微博发布时间：微博发布时的时间</li>
<li>点赞数：微博被赞的数量</li>
<li>转发数：微博被转发的数量</li>
<li>评论数：微博被评论的数量</li>
<li>来源：微博文章来源自哪里</li>
</ul>
<h2>运行环境</h2>
<ul>
<li>开发语言：python3</li>
<li>系统： Windows/Linux/Centos7</li>
</ul>
<h2>使用说明</h2>
<b>源码安装</b></br>

	$ git clone https://github.com/zhs-py/wb-spider.git
	$ cd wb-spider
	$ pip install -r requirements.txt

<b>运行程序</b></br>
在wb-spider目录运行如下命令</br>
	
	$ python3 weibo_spider.py
