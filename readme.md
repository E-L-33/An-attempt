# Developing documents
------------------------------------
### Modified version 2018/12/19 blog
* 修改首页布局,修改文章内容页面布局
* 修改requirments文件-删除bs4,request,urllib2,添加django-mdeditor,Markdown和django-suit
* 规划网页内容,修改分类
* 3.Uenfinished:

    <1> .文章detail页面的评论数要改,改views,加锚点

    <2>.主页的模态框需要写,而且调用模态框时怎么计数(可以另外写一篇blog)

    <3>.主页中间的搜索框怎么能让他在xs时显示, 而在其他屏幕隐藏

    <4>.废弃掉blog_list,重写Technology Stack(面包屑)

    <5>.blog_detail右侧可以加时间轴

    <6>.主页的user信息下面可以加上vue里面的那个动态动物

    <7>.主页的key word参考http://www.scrapyd.cn/的热搜词

    <8>.主页的总结和留言板加锁

    <9>.主页的登录注册修复

    <10>.主页的网站阅读记录使用有格式的弹出框,Unfinished

    <11>.主页的七天热门文章

    <12>.换一个有交互效果的导航栏

    <13>.解决文章分类,一文对多标签的问题
    
    <14>.解决django-suit的显示格式问题

------------------------------------
### Modified version 2018/12/08 blog
* 并无太大改动，规范
* db-backup.sql是定期备份的mysql文件

------------------------------------
### Modified version 2018/10/20 master
* 修改了首页布局和一些一些界面优化
* 修改了登录和注册页面
* 预计加入留言池，将个人记录的部分内容移入
* 预计加入资源栏目
* 修复了七天热门阅读下文章后不能正确显示阅读数量的bug

------------
### Initial Version 2018/10/16 master
完成了基础的网站建设，止步于ajax，还存在以下bug：
* 计数和日期归档不能正常运行
