### 零、写在前面

- 这个笔记只是用自己的话整理了一下Beautiful Soup的官方文档。

  文档链接🔗 https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/

  英文文档🔗https://www.crummy.com/software/BeautifulSoup/bs4/doc/

### 一、什么是Beautiful Soup

- Beautiful Soup是一个可以从HTML或XML文件中提取数据的Python库.它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.Beautiful Soup会帮你节省数小时甚至数天的工作时间。

### 二、Beautiful Soup解析器

- `BeautifulSoup` 第一个参数应该是要被解析的文档字符串或是文件句柄,第二个参数用来标识怎样解析文档.如果第二个参数为空,那么Beautiful Soup根据当前系统安装的库自动选择解析器,解析器的优先数序: lxml, html5lib, Python标准库

- Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器,其中一个是 lxml.另一个可供选择的解析器是纯Python实现的 html5lib , html5lib的解析方式与浏览器相同。

- 如果不加入第二个参数创建Beautiful Soup，例如soup = BeautifulSoup(html_doc)则Beautiful Soup选择最合适的解析器来解析这段文档,如果手动指定解析器，例如soup = BeautifulSoup(html_doc, '**lxml**')那么Beautiful Soup会选择指定的解析器lxml来解析文档
- 推荐使用lxml作为解析器,因为效率更高. 在Python2.7.3之前的版本和Python3中3.2.2之前的版本,必须安装lxml或html5lib, 因为那些Python版本的标准库中内置的HTML解析方法不够稳定.

|      解析器      |                           使用方法                           |                         优势                          |                      劣势                       |
| :--------------: | :----------------------------------------------------------: | :---------------------------------------------------: | :---------------------------------------------: |
|   Python标准库   |            `BeautifulSoup(markup, "html.parser")`            |     Python的内置标准库执行速度适中文档容错能力强      | Python 2.7.3 or 3.2.2)前 的版本中文档容错能力差 |
| lxml HTML 解析器 |               `BeautifulSoup(markup, "lxml")`                |                 速度快文档容错能力强                  |                 需要安装C语言库                 |
| lxml XML 解析器  | `BeautifulSoup(markup, ["lxml-xml"])``BeautifulSoup(markup, "xml")` |               速度快唯一支持XML的解析器               |                 需要安装C语言库                 |
|     html5lib     |             `BeautifulSoup(markup, "html5lib")`              | 最好的容错性以浏览器的方式解析文档生成HTML5格式的文档 |              速度慢不依赖外部扩展               |

## 三、格式化输出

```python
# encoding=utf-8
from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>

<body>
    <p class="title"><b>一个小故事</b></p>

    <p class="story">从前,有三个小妹妹;他们的名字是
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 和
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        他们住在井底.
    </p>

    <p class="story">...1</p>
    <p class="story">...2</p>
    <p class="story">...3</p>
    <a href="http://example.com/elsie" class="sister">1</a>
    <a href="http://example.com/elsie" class="sister">2</a>
    <a href="http://example.com/elsie" class="sister">3</a>
    <a href="http://example.com/elsie" class="sister aa" id="1">4</a>
    <a href="http://example.com/elsie" class="sister aa" id="2">4</a>
    <a href="http://example.com/elsie">4</a>
    <a href="http://example.com/aaa">4</a>
    <a href="http://example.com/aaa/bbb">4</a>
    <a href="">4</a>
    <div data-foo="value" a="b">foo!</div>
</body>

</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')
prettify = soup.prettify()
print(prettify)  # 格式化输出HTML
```

①使用.prettify()函数实现格式化

②BeautifulSoup` 对象和它的tag节点都可以调用 `prettify()` 方法

③`prettify()` 方法将Beautiful Soup的文档树格式化后以Unicode编码输出,每个XML/HTML标签都独占一行

### 四、Beautiful Soup的类型

​		Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: Tag 、NavigableString、BeautifulSoup、Comment

#### 1、Tag类型

```python
# encoding=utf-8
from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>

<body>
    <p class="title"><b>一个小故事</b></p>

    <p class="story">从前,有三个小妹妹;他们的名字是
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 和
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        他们住在井底.
    </p>

    <p class="story">...</p>
</body>

</html>
"""
soup = BeautifulSoup(html_doc, 'lxml')
print(soup.b)  # 获取首个b标签,获取不到返回None,获取到就返回Tag对象
print(type(soup.b))  # 类型是bs4.element.Tag
print(soup.b.name)  # 获取Tag的名字
soup.b.name = 'my_div'  # 修改Tag的名字,这会影响所有通过当前BeautifulSoup对象生成的HTML文档
# 测试打印soup,会发现首个b标签已经变成my_div标签了
print(soup.a)  # 获取首个a标签,获取不到返回None,获取到就返回Tag对象
print(soup.a.attrs)  # 获取首个a标签的所有属性（Tag的所有属性）,返回是dict类型
print(soup.a.attrs.get('class'))  # 获取首个a标签的class属性,返回list
print(soup.a.get('class'))  # 获取首个a标签的class属性,返回list
print(soup.a['class'])  # 获取首个a标签的class属性,返回list
print(soup.a.get('href'))  # 获取首个a标签的href属性,返回字符串
print(soup.a.get('href1'))  # 获取首个a标签的href1属性,返回None
print(soup.a['href'])  # 获取首个a标签的href属性,返回字符串
"""
Tag的属性可以被添加,删除或修改.再说一次,Tag的属性操作方法与字典一样
获取Tag属性时,返回类型是不唯一的,多值属性返回list,单值属性返回字符串,例如class返回list,href返回字符串,id返回字符串
如果某个属性看起来好像有多个值,但在任何版本的HTML定义中都没有被定义为多值属性,那么Beautiful Soup会将这个属性作为字符串返回
"""
```

①每个tag都有自己的名字,通过 `.name` 来获取

- 如果改变了tag的name,那将影响所有通过当前Beautiful Soup对象生成的HTML文档

②使用.attrs获取属性

- Tag的属性可以被添加,删除或修改.再说一次,Tag的属性操作方法与字典一样
- 获取Tag属性时,返回类型是不唯一的,多值属性返回list,单值属性返回字符串,例如class返回list,href返回字符串,id返回字符串
- 如果某个属性看起来好像有多个值,但在任何版本的HTML定义中都没有被定义为多值属性,那么Beautiful Soup会将这个属性作为字符串返回

#### 2、NavigableString类型

```python
# encoding=utf-8

from bs4 import BeautifulSoup
from idna import unicode

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>

<body>
    <p class="title"><b>一个小故事</b></p>

    <p class="story">从前,有三个小妹妹;他们的名字是
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 和
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        他们住在井底.
    </p>

    <p class="story">...</p>
</body>

</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')
b = soup.b  # 获取b标签,b标签是一个Tag类型
print(b.string)  # 获取b标签的文本
print(type(b.string))  # b标签的文本类型是NavigableString
# 字符串常被包含在tag内.Beautiful Soup用 NavigableString 类来包装tag中的字符串
unicode_string = unicode(b.string)  # 编码为string类型
"""
如果想在Beautiful Soup之外使用 NavigableString 对象,需要调用 unicode() 方法,
将该对象转换成普通的Unicode字符串,否则就算Beautiful Soup已方法已经执行结束,该对象的输出也会带有对象的引用地址.这样会浪费内存.
"""
print(unicode_string)  # 一个小故事
print(type(unicode_string))  # <class 'str'>
```

①字符串常被包含在tag内.Beautiful Soup用 `NavigableString` 类来包装tag中的字符串

②一个 `NavigableString` 字符串与Python中的Unicode字符串相同, 通过 `unicode()` 方法可以直接将 `NavigableString` 对象转换成Unicode字符串，如果想在Beautiful Soup之外使用 `NavigableString` 对象,需要调用 `unicode()` 方法,将该对象转换成普通的Unicode字符串,否则就算Beautiful Soup已方法已经执行结束,该对象的输出也会带有对象的引用地址.这样会浪费内存.

#### 3、BeautifulSoup类型

```python
# encoding=utf-8

from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>

<body>
    <p class="title"><b>一个小故事</b></p>

    <p class="story">从前,有三个小妹妹;他们的名字是
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 和
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        他们住在井底.
    </p>

    <p class="story">...</p>
</body>

</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')
"""
BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象
因为 BeautifulSoup 对象并不是真正的HTML或XML的tag,所以它没有name和attribute属性.但有时查看它的 .name 
属性是很方便的,所以 BeautifulSoup 对象包含了一个值为 “[document]” 的特殊属性 .name
"""
print(soup.name)  # 获取名称
print('*' * 20)
print(soup.string)  # 获取文本
"""
如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点
如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同
如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
"""
print('*' * 20)
print(soup.text)  # 获取所有文字内容
print('*' * 20)
print(soup.get_text())  # 获取所有文字内容
```

①`BeautifulSoup` 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 `Tag` 对象。

②因为 `BeautifulSoup` 对象并不是真正的HTML或XML的tag,所以它没有name和attribute属性.但有时查看它的 `.name` 属性是很方便的,所以 `BeautifulSoup` 对象包含了一个值为 “[document]” 的特殊属性 `

#### 4、Comment类型

```python
# encoding=utf-8
from bs4 import BeautifulSoup

markup = """<b><!--Hey, buddy. Want to buy a used parser?--></b>"""
soup = BeautifulSoup(markup, 'lxml')
print(soup.prettify())  # 格式化HTML
print('*' * 18)
comment = soup.b
print(comment)  # <b><!--Hey, buddy. Want to buy a used parser?--></b>
print('*' * 18)
print(comment.string)  # Hey, buddy. Want to buy a used parser?
print(type(comment.string))  # 注释类型是<class 'bs4.element.Comment'>
"""
Tag , NavigableString , BeautifulSoup 几乎覆盖了html和xml中的所有内容,但是还有一些特殊对象.容易让人担心的内容是文档的注释部分
Comment 对象是一个特殊类型的 NavigableString 对
"""
```

①`Tag` , `NavigableString` , `BeautifulSoup` 几乎覆盖了html和xml中的所有内容,但是还有一些特殊对象.容易让人担心的内容是文档的注释部分

②`Comment` 对象是一个特殊类型的 `NavigableString` 对象

### 五、遍历文档树

```python
# encoding=utf-8
from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>

<body>
    <p class="title"><b>一个小故事</b></p>

    <p class="story">从前,有三个小妹妹;他们的名字是
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 和
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        他们住在井底.
    </p>

    <p class="story">...</p>
</body>

</html>
"""
soup = BeautifulSoup(html_doc, 'lxml')
print(soup.head)  # 根据Tag的名字直接获取该Tag对象
print(soup.title)  # 根据Tag的名字直接获取该Tag对象
print(soup.p)  # 根据Tag的名字直接获取该Tag对象
print(soup.body.p)  # 根据Tag的名字直接获取该Tag对象,可以连续获取

for content in soup.head.contents:  # tag的 .contents 属性可以将tag的直接子节点以列表的方式输出
    print(f'content:{content}')
for child in soup.head.children:  # 通过tag的 .children 生成器,可以对tag的直接子节点进行循环
    print(f'child:{child}')
```

①根据Tag的名字直接获取该Tag对象

②tag的 `.contents` 属性可以将tag的直接子节点以列表的方式输出

③通过tag的 `.children` 生成器,可以对tag的直接子节点进行循环

```python
# encoding=utf-8
from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head><title>标题</title></head>

<body>
    <p class="title"><b>一个小故事</b></p>

    <p class="story">从前,有三个小妹妹;他们的名字是
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 和
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        他们住在井底.
    </p>

    <p class="story">...</p>
</body>

</html>
"""
soup = BeautifulSoup(html_doc, 'lxml')
print(soup.head)  # 根据Tag的名字直接获取该Tag对象
print(soup.title)  # 根据Tag的名字直接获取该Tag对象
print(soup.p)  # 根据Tag的名字直接获取该Tag对象
print(soup.body.p)  # 根据Tag的名字直接获取该Tag对象,可以连续获取

for content in soup.body.contents:  # tag的 .contents 属性可以将tag的直接子节点以列表的方式输出
    print(f'content:{content}')  # 会遍历出body的直接子节点,不包括a标签
print('*' * 20)
for child in soup.body.descendants:  # .descendants 属性可以对所有tag的子孙节点进行递归循环
    print(f'child:{child}')  # 会遍历出body的所有子孙节点,包括a标签

print(soup.title.string)  # 根据Tag的名字直接获取该Tag对象
print(type(soup.title.string))  # 根据Tag的名字直接获取该Tag对象 bs4.element.NavigableString
# 如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点
print(soup.head)
print(soup.head.string)  # 可以看到能获取到子节点的文本 #标题
# 如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同
# 如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
```

④Tag的`.descendants` 属性可以对所有的子孙节点进行递归循环 

- `.contents` 和 `.children` 属性仅包含tag的直接子节点,而`.descendants` 属性可以遍历所有的子孙节点

⑤如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点

- 如果一个tag仅有一个子节点,那么这个tag也可以使用 `.string` 方法,输出结果与当前唯一子节点的 `.string` 结果相同

  ```html
  <head><title>标题</title></head>
  ```

  这样soup.head.string == soup.head.title.string

```html
<head>
  <title>标题</title>
</head>
```

​		这样soup.head.string != soup.head.title.string ， 前者是None，后者是”标题“

因为前者中有\n换行符，这也是代表一个节点的，所以head的子节点就不是唯一一个title了

- 如果tag包含了多个子节点,tag就无法确定 `.string` 方法应该调用哪个子节点的内容, `.string` 的输出结果是 `None` 

```python
# encoding=utf-8
from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>

<body>
    <p class="title"><b>一个小故事</b></p>

    <p class="story">从前,有三个小妹妹;他们的名字是
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 和
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        他们住在井底.
    </p>

    <p class="story">...</p>
</body>

</html>
"""
soup = BeautifulSoup(html_doc, 'lxml')
for obj in soup.strings:  # 如果tag中包含多个字符串,可以使用 .strings 来循环获取
    print(repr(obj))
print('---------------------\n')
for obj in soup.body.strings:  # 如果tag中包含多个字符串,可以使用 .strings 来循环获取
    print(repr(obj))
print('￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥\n')

soup = BeautifulSoup(html_doc, 'lxml')
for obj in soup.stripped_strings:  # 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容
    print(repr(obj))
print('---------------------\n')
for obj in soup.body.stripped_strings:  # 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容
    print(repr(obj))
print('---------------------\n')
```

⑥如果tag中包含多个字符串,可以使用 .strings 来循环获取

- 输出的字符串中可能包含了很多空格或空行,使用 `.stripped_strings`  可以去除多余空白内容
- 全部是空格的行会被忽略掉,段首和段末的空白会被删除

```python
# encoding=utf-8
from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>

<body>
    <p class="title"><b>一个小故事</b></p>

    <p class="story">从前,有三个小妹妹;他们的名字是
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 和
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        他们住在井底.
    </p>

    <p class="story">...</p>
</body>

</html>
"""
soup = BeautifulSoup(html_doc, 'lxml')
obj = soup.a  # 获取Tag a标签
print(obj)  # a标签
print(obj.parent)  # 通过 .parent 属性来获取某个元素的父节点
print(soup.title.string.parent)  # title标签的文本是NavigableString,父节点是title
print(soup.html.parent.name)  # 文档的顶层节点比如<html>的父节点是 BeautifulSoup 对象
print(soup.parent)  # BeautifulSoup 对象的 .parent 是None
print('-' * 20)
for tag in soup.a.parents:  # 通过元素的 .parents 属性可以递归得到元素的所有父辈节点
    print(tag.name)
```

⑦通过 `.parent` 属性来获取某个元素的父节点

- 文档的顶层节点比如<html>的父节点是 BeautifulSoup 对象
- BeautifulSoup 对象的 .parent 是None

⑧通过元素的 `.parents` 属性可以递归得到元素的所有父辈节点

```python
# encoding=utf-8
from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>

<body><p class="title"><b>一个小故事</b></p><div>我是div</div><p class="story">从前,有三个小妹妹;他们的名字是
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 和
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        他们住在井底.
    </p>

    <p class="story">...</p>
</body>

</html>
"""
soup = BeautifulSoup(html_doc, 'lxml')
obj = soup.body
for tag in obj.children:
    if tag.name is not None:
        print(tag.name)  # 他们是兄弟节点
print(repr(soup.body.p.previous_sibling))  # p标签的前一个兄弟,没有就算None
print(repr(soup.body.p.next_sibling))  # p标签的后一个兄弟,没有就算None
# 在文档树中,使用 .next_sibling 和 .previous_sibling 属性来查询兄弟节点
# 实际文档中的tag的 `.next_sibling` 和 `.previous_sibling` 属性通常是字符串或空白,因为通常标签之间是顿号和换行符
print('====================')
for i in soup.body.p.next_siblings:  # 通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出
    print(i)
print('___________________')
for i in soup.body.contents[3].previous_siblings:  # 通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出
    print(i)
```

⑨在文档树中,使用 `.next_sibling` 和 `.previous_sibling` 属性来查询兄弟节点

- 实际文档中的tag的 `.next_sibling` 和 `.previous_sibling` 属性通常是字符串或空白,因为通常标签之间是顿号和换行符

⑩通过 `.next_siblings` 和 `.previous_siblings` 属性可以对当前节点的兄弟节点迭代输出

```python
# encoding=utf-8
from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>

<body><p class="title"><b>一个小故事</b></p><div>我是div</div><p class="story">从前,有三个小妹妹;他们的名字是
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 和
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        他们住在井底.</p><p class="story">...</p>
</body>

</html>
"""
soup = BeautifulSoup(html_doc, 'lxml')

print(repr(soup.body.p.previous_element.name))  # p标签的前一个被解析的对象,没有就是None
print(repr(soup.body.p.next_element.name))  # p标签的后一个被解析的对象,没有就是None
print('====================')
# .next_element 属性指向解析过程中下一个被解析的对象(字符串或tag),结果可能与 .next_sibling 相同,但通常是不一样的.
for i in soup.body.p.next_elements:
    # 通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样
    if i.name is not None:
        print(i.name)
print('___________________')
for i in soup.body.p.previous_elements:
    # 通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样
    if i.name is not None:
        print(i.name)
```

假设html是这样子的

```html
<html><head><title>The Dormouse's story</title></head>
<p class="title"><b>The Dormouse's story</b></p>
```

HTML解析器把这段字符串转换成一连串的事件: “打开html标签”,”打开一个head标签”,”打开一个title标签”,”添加一段字符串”,”关闭title标签”,”打开p标签”,等等.Beautiful Soup提供了重现解析器初始化过程的方法.

⑪`.next_element` 属性指向解析过程中下一个被解析的对象(字符串或tag),结果可能与 `.next_sibling` 相同,但通常是不一样的,因为通常标签之间是顿号和换行符

⑫通过 `.next_elements` 和 `.previous_elements` 的迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样

### 六、搜索文档树

```python
# encoding=utf-8
import re

from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>

<body>
    <p class="title"><b>一个小故事</b></p>

    <p class="story">从前,有三个小妹妹;他们的名字是
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 和
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        他们住在井底.
    </p>

    <p class="story">...1</p>
    <p class="story">...2</p>
    <p class="story">...3</p>
    <a href="http://example.com/elsie" class="sister">1</a>
    <a href="http://example.com/elsie" class="sister">2</a>
    <a href="http://example.com/elsie" class="sister">3</a>
    <a href="http://example.com/elsie" class="sister">4</a>
    <a href="http://example.com/elsie">4</a>
    <a href="http://example.com/aaa">4</a>
    <a href="http://example.com/aaa/bbb">4</a>
    <a href="">4</a>
</body>

</html>
"""
soup = BeautifulSoup(html_doc, 'lxml')
ret = soup.find_all('p')  # 传入Tag的名字,查找当前直接子节点中所有的Tag标签
for r in ret:
    print(r)
print('=================')
ret = soup.find_all(re.compile('^b'))  # 传入正则表达式,查找当前直接子节点中所有符合正则搜索条件的Tag标签
for r in ret:
    print(r)
print('=================')
ret = soup.find_all(['a', 'p'])  # 传入list,查找当前直接子节点中所有在list中的Tag标签
for r in ret:
    print(r)
print('=================')
ret = soup.find_all(True)  # 传入True 可以查找到所有的tag
for r in ret:
    print(r.name)
print('*****************')
for i in soup.find_all('a'):  # 找到所有的a标签
    print(f'标签:{i}')


def filter_tag(tag):
    # 找到带有class属性,但是不带有id的a标签
    return tag.name == 'a' and tag.has_attr('class') and not tag.has_attr('id')


print('*****************')
for i in soup.find_all(filter_tag):  # 传入自定义Tag过滤器函数 可以查找到所有符合函数条件的tag
    print(f'带有class属性,但是不带有id的a标签:{i}')


def filter_href(href):
    return href and 'aaa' in href and 'bbb' not in href


print('*****************')
for i in soup.find_all(href=filter_href):  # 传入自定义Tag属性过滤器函数 可以查找到所有符合函数条件的tag
    print(f'href属性中含有aaa字符串但不含有bbb字符串的Tag标签:{i}')
```

①find_all()方法调用

- 传入Tag的名字,查找当前直接子节点中所有的Tag标签
- 传入正则表达式,查找当前直接子节点中所有符合正则搜索条件的Tag标签
- 传入list,查找当前直接子节点中所有在list中的Tag标签
- 传入True 可以查找到所有的tag
- 传入自定义Tag过滤器函数 可以查找到所有符合函数条件的tag
- 传入自定义Tag属性过滤器函数 可以查找到所有符合函数条件的tag

```python
# encoding=utf-8

from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>

<body>
    <p class="title"><b>一个小故事</b></p>

    <p class="story">从前,有三个小妹妹;他们的名字是
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 和
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        他们住在井底.
    </p>

    <p class="story">...1</p>
    <p class="story">...2</p>
    <p class="story">...3</p>
    <a href="http://example.com/elsie" class="sister">1</a>
    <a href="http://example.com/elsie" class="sister">2</a>
    <a href="http://example.com/elsie" class="sister">3</a>
    <a href="http://example.com/elsie" class="sister aa" id="1">4</a>
    <a href="http://example.com/elsie" class="sister aa" id="2">4</a>
    <a href="http://example.com/elsie">4</a>
    <a href="http://example.com/aaa">4</a>
    <a href="http://example.com/aaa/bbb">4</a>
    <a href="">4</a>
    <div data-foo="value" a="b">foo!</div>
</body>

</html>
"""
soup = BeautifulSoup(html_doc, 'lxml')
# def find_all(self, name=None, attrs={}, recursive=True, text=None,limit=None, **kwargs)
# find_all的形参
"""
name 参数可以查找所有名字为name的Tag
重申: 搜索 name 参数的值可以使任一类型的 过滤器 ,字符窜,正则表达式,列表,方法或是 True
"""
"""
keyword 参数
如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索
例如
find_all(id='aa')返回id属性为aa的Tag对象
find_all(class_='aa')返回class_属性包含aa的Tag对象
find_all(href='aa')返回href属性是aa的Tag对象
find_all(href=True)返回有href属性的Tag对象
find_all(class_='aa',id='1')  # 返回class_属性包含aa且id是1的Tag对象（可以同时使用过滤多个条件）
"""
"""
按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,使用 class 做参数会导致语法错误.从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag
"""
ret = soup.find_all(id='aa')  # 返回id属性为aa的Tag对象
print(ret)
ret = soup.find_all(class_='aa')  # 返回class_属性包含aa的Tag对象
print(ret)
ret = soup.find_all(href='aa')  # 返回href属性是aa的Tag对象
print(ret)
ret = soup.find_all(href=True)  # 返回有href属性的Tag对象
print(ret)
ret = soup.find_all(class_='aa', id='1')  # 返回class_属性包含aa且id是1的Tag对象
print(ret)

"ret = soup.find_all(data-foo = 'value')  # 有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性"
ret = soup.find_all(attrs={'data-foo': 'value'})  # 但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag
print(ret)
```

②find_all()方法的解析

❶定义：

- def find_all(self, name=None, attrs={}, recursive=True, text=None,limit=None, **kwargs)


❷name 参数可以查找所有名字为name的Tag

- 重申: 搜索 name 参数的值可以使任一类型的 过滤器 ,字符窜,正则表达式,列表,方法或是 True

❸keyword 参数

- 如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索
  例如
  find_all(id='aa')返回id属性为aa的Tag对象
  find_all(class_='aa')返回class_属性包含aa的Tag对象
  find_all(href='aa')返回href属性是aa的Tag对象
  find_all(href=True)返回有href属性的Tag对象
  find_all(class_='aa',id='1')  # 返回class_属性包含aa且id是1的Tag对象（可以同时使用过滤多个条件）

- 按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,使用 class 做参数会导致语法错误.从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag

  - class_` 参数同样接受不同类型的 `过滤器` ,字符串,正则表达式,方法或 `True

  - tag的 `class` 属性是 [多值属性](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id15) .按照CSS类名搜索tag时,可以分别搜索tag中的每个CSS类名:
  - 搜索 `class` 属性时也可以通过CSS值完全匹配，完全匹配 `class` 的值时,如果CSS类名的顺序与实际不符,将搜索不到结果

```python
# encoding=utf-8

from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>

<body>
    <p class="title"><b>一个小故事</b></p>

    <p class="story">从前,有三个小妹妹;他们的名字是
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 和
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        他们住在井底.
    </p>

    <p class="story">...1</p>
    <p class="story">...2</p>
    <p class="story">...3</p>
    <a href="http://example.com/elsie" class="sister">1</a>
    <a href="http://example.com/elsie" class="sister">2</a>
    <a href="http://example.com/elsie" class="sister">3</a>
    <a href="http://example.com/elsie" class="sister aa" id="1">4</a>
    <a href="http://example.com/elsie" class="sister aa" id="2">4</a>
    <a href="http://example.com/elsie">4</a>
    <a href="http://example.com/aaa">4</a>
    <a href="http://example.com/aaa/bbb">4</a>
    <a href="">4</a>
    <div data-foo="value" a="b">嘿嘿 呵呵 哈哈</div>
    <div data-foo="value" a="b">嘿嘿  哈哈!</div>
    <div data-foo="value" a="b"> 呵呵 哈哈!</div>
    <div data-foo="value" a="b">哈哈</div>
    <div data-foo="value" a="b">嘿嘿</div>
    <div ><a href="">啥啥啥</a></div>
    
    
</body>

</html>
"""
soup = BeautifulSoup(html_doc, 'lxml')
# def find_all(self, name=None, attrs={}, recursive=True, text=None,limit=None, **kwargs)
# find_all的形参
"""
name 参数可以查找所有名字为name的Tag
重申: 搜索 name 参数的值可以使任一类型的 过滤器 ,字符窜,正则表达式,列表,方法或是 True
"""
"""
通过 string 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, string 参数接受 字符串 , 正则表达式 , 列表, True
返回是NavigableString对象
"""
ret = soup.find_all(string='哈哈')
print(ret)
ret = soup.find_all(string=['哈哈', '嘿嘿'])
print(ret)


def filter_string(string):
    # 找到"哈哈"在字符串但"嘿嘿"不在字符串的Tag标签
    return '哈哈' in string and '嘿嘿' not in string


ret = soup.find_all(string=filter_string)  # 通过 string 参数可以搜搜文档中的字符串内容，返回NavigableString对象
print(ret)
for i in ret:
    print(i)
    print(type(i))  # NavigableString对象
    print(i.parent)  # 父亲节点
print('*****************')
ret = soup.find_all('div', string=filter_string)  # 可以和其他参数一起过滤
print(ret)

"""
limit 参数
find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.
效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.
"""
ret = soup.find_all('a')
print(ret)
ret = soup.find_all('a', limit=1)
print(ret)
"""
recursive 参数
调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,
如果只想搜索tag的直接子节点,可以使用参数 recursive=False
"""
print('$$$$$$$$$$$$$$$$4')
ret = soup.body.find_all('a')
print(ret)
ret = soup.body.find_all('a', recursive=False)
print(ret)
```

❹`string`参数

- 通过 string 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, string 参数接受 字符串 , 正则表达式 , 列表, True
- 返回是NavigableString对象
- 可以和其他参数一起过滤Tag

❺`limit` 参数

`find_all()` 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 `limit` 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 `limit` 的限制时,就停止搜索返回结果.

❻recursive 参数
调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False

❼`find_all()` 几乎是Beautiful Soup中最常用的搜索方法,所以我们定义了它的简写方法. `BeautifulSoup` 对象和 `tag` 对象可以被当作一个方法来使用,这个方法的执行结果与调用这个对象的 `find_all()` 方法相同,下面代码是等价的

soup.find_all("a")和soup("a")

soup.title.find_all(string=True)和soup.title(string=True)

③find()方法

- `find_all()` 方法将返回文档中符合条件的所有tag,尽管有时候我们只想得到一个结果.比如文档中只有一个<body>标签,那么使用 `find_all()` 方法来查找<body>标签就不太合适, 使用 `find_all` 方法并设置 `limit=1` 参数不如直接使用 `find()` 方法.

- 唯一的区别是 `find_all()` 方法的返回结果是值包含一个元素的列表,而 `find()` 方法直接返回结果.

- find_all()` 方法没有找到目标是返回空列表, `find()` 方法找不到目标时,返回 `None
- `soup.head.title` 是 tag的名字.属性的简写.这个简写的原理就是多次调用当前tag的 `find()` 方法

④其他搜索函数

- find_all() 和 find() 搜索当前节点的所有子节点和孙子节点. 以下方法都类似于find_all()函数和find()函数
-  find_parents() 和 find_parent() 用来搜索当前节点的父辈节点，搜索父辈节点的方法实际上就是对 .parents 属性的迭代搜索
- find_next_siblings() 和 find_next_sibling() 用来搜索当前节点后面的兄弟节点，搜索兄弟节点的方法实际上就是对 .next_siblings 属性的迭代搜索
- find_previous_siblings() 和 find_previous_sibling() 用来搜索当前节点前面的兄弟节点，搜索兄弟节点的方法实际上就是对 .previous_sibling 属性的迭代搜索
- find_all_next() 和 find_next() 用来搜索当前节点后面的解析节点，搜索解析节点的方法实际上就是对 .next_elements 属性的迭代搜索
- find_all_previous() 和 find_previous() 用来搜索当前节点前面的解析节点，搜索解析节点的方法实际上就是对 .previous_element 属性的迭代搜索

### 七、写在最后

①编码

- 任何HTML或XML文档都有自己的编码方式,比如ASCII 或 UTF-8,但是使用Beautiful Soup解析后,文档都被转换成了Unicode

- Beautiful Soup用了 编码自动检测子库来识别当前文档编码并转换成Unicode编码. `BeautifulSoup` 对象的 `.original_encoding` 属性记录了自动识别编码的结果

- 编码自动检测功能大部分时候都能猜对编码格式,但有时候也会出错.有时候即使猜测正确,也是在逐个字节的遍历整个文档后才猜对的,这样很慢.如果预先知道文档编码,可以设置编码参数来减少自动检查编码出错的概率并且提高文档解析速度.在创建 `BeautifulSoup` 对象的时候设置 `from_encoding` 参数

  ```python
  soup = BeautifulSoup(markup, from_encoding="iso-8859-8")
  ```

- 如果仅知道文档采用了Unicode编码, 但不知道具体编码. 可以先自己猜测, 猜测错误(依旧是乱码)时, 可以把错误编码作为 `exclude_encodings` 参数, 这样文档就不会尝试使用这种编码了解码了.  在没有指定编码的情况下, BS会自己猜测编码, 把不正确的编码排除掉, BS就更容易猜到正确编码.

- 通过Beautiful Soup输出文档时,不管输入文档是什么编码方式,输出编码均为UTF-8编码,如果不想用UTF-8编码输出,可以将编码方式传入 `prettify()` 方法，还可以调用 `BeautifulSoup` 对象或任意节点的 `encode()` 方法,就像Python的字符串调用 `encode()` 方法一样

```python
  soup.p.encode("latin-1")
  # '<p>Sacr\xe9 bleu!</p>'
  
  soup.p.encode("utf-8")
  # '<p>Sacr\xc3\xa9 bleu!</p>'
```

