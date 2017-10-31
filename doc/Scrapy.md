# Scrapy

##### CSS Selector css的语法来定位标签

##### Xpath 是一门路径提取语言，常用于从 `html/xml` 文件中提取信息。

| 表达式      | 描述                            |
| -------- | ----------------------------- |
| nodename | 选取此节点的所有子节点。                  |
| /        | 从根节点选取。                       |
| //       | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。 |
| .        | 选取当前节点。                       |
| ..       | 选取当前节点的父节点。                   |
| @        | 选取属性。                         |

```HTML
<div id='images'>
   <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
   <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
 </div>
```

```Python3 
# extract 函数执行提取操作，返回一个列表
# extract_first 返回列表的第一个

# 提取文字部分
response.css('dev#images a::text').extract()
response.xpath('//div[@id="images"]/a/text()').extract()
# 提取url
resopnse.css('div#images a::attr(href)').extract()
response.xpath('//div[@id="images"]/a/@href').extract()
# 提取图片链接
response.css('div#images a img::attr(src)').extract()
response.xpath('//div[@id="images"]/a/img/@src').extract()
```

##### re 和 re_first

`re()` 和 `re_first()` 方法可以用于 `css()` 或者 `xpath()`方法返回的对象。使用正则表达式对提取的内容做进一步的处理。

匹配文本中的文字：`re_first('[^\d]*(\d*)[^\d]*')`

