因为集思录中的数据是用JS处理的，用requests是无法爬取其中的数据的。需要用到Selenium中的webdriver才能爬取其中的数据。

使用上面的代码，需要安装Selenium库，同时需要下载对应的Chrome WebDriver，把Chrome WebDriver放到和python.exe同一个文件下就好（最简单的方法）。

pip install selenium //安装selenium库