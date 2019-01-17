# -*- coding: utf-8 -*-
import scrapy
from p1.items import P1Item
from scrapy.linkextractors import LinkExtractor


class TestSpider(scrapy.Spider):
    # 爬虫后，启动爬虫时需要的参数*必须
    name = 'test'
    # 爬取域范围，允许爬虫在这个域名下进行爬取(可选)
    allowed_domains = ['http://www.itcast.cn/']
    # url列表，爬虫执行后第一批请求，将从这个列表里获取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#acaaa']

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item = P1Item()
            # extract()将xpath对象转换为Unicode字符串
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            # 返回提取到的每个item数据，给管道文件处理，同时还会回来继续执行后面的代码
            yield item

            # 提取链接
            """
            # 使用Selector
            next_url = response.xpath('').extract_first()
            if next_url:
                # 如果找到下一页的url，得到绝对路径，构造新的Request对象
                next_url = response.urljoin(next_url)
                yield scrapy.Request(next_url, callback=self.parse)
            """
            """
            # 使用LinkExtractor
            le = LinkExtractor()
            links = le.extract_links(response)
            if links:
                next_url = links[0].url
                yield scrapy.Request(next_url, callback=self.parse)
            """
            """
            由于页面中的下一页链接只有一个，因此用links[0]获取Link对象，Link对象的url属性便是链接
            页面的绝对url地址
            
            如果不传递任何参数就提取页面中的所有链接
            
            LinkExtractor构造器的参数有：
            allow: 接收一个正则表达式或列表，提取绝对url与正则匹配的链接
            deny: 接收一个正则表达式或列表，排除绝对url与正则匹配的链接
            allow_domains: 接收一个域名或域名列表，提取到指定域的链接
            deny_domains: 排除到指定域的链接
            restrict_xpaths: 接收一个XPath表达式或列表，提取XPath表达式选中区域下的链接
            restrict_css: 接收一个css选择器或一个列表，提取css选择器选中区域下的链接
            tags: 接收一个标签(字符串)或一个标签列表，提取指定标签内的链接，默认为['a', 'area']
            attrs: 接收一个属性(字符串)或一个属性列表，提取指定属性内的链接，默认为['href']
            process_value: 接收一个形如func(value)的回调函数。如果传递了该参数，LinkExtractor将
                           调用该回调函数对提取的每一个链接进行处理，回调函数正常情况下应该返回
                           一个字符串(处理结果)，想要抛弃所处理的链接时，返回None
            """