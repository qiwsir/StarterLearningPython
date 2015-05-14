#《零基础学python》（第二版）
#第壹季 基础
* [第零章 预备](Chapter0/README.md)
    - [关于python的故事](Chapter0/01.md)
    - [从小工到专家](Chapter0/02.md)
    - [安装python的开发环境](Chapter0/03.md)
    - [集成开发环境](Chapter0/101.md)==>集成开发环境；python的IDE
* [第壹章 基本数据类型](Chapter1/README.md)
    - [数和四则运算](Chapter1/102.md)==>整数和浮点数；变量；整数溢出问题；
    - [除法](Chapter1/103.md)==>整数、浮点数相除；`from __future__ import division`；余数；四舍五入；
    - [常用数学函数和运算优先级](Chapter1/104.md)==>math模块，求绝对值，运算优先级
    - [写一个简单程序](Chapter1/105.md)==>程序和语句，注释
    - [字符串(1)](Chapter1/106.md)==>字符串定义，转义符，字符串拼接，str()与repr()区别
    - [字符串(2)](Chapter1/107.md)==>raw_input,print，内建函数，原始字符串，再做一个小程序
    - [字符串(3)](Chapter1/108.md)==>字符串和序列，索引，切片，基本操作
    - [字符串(4)](Chapter1/109.md)==>字符串格式化，常用的字符串方法
    - [字符编码](Chapter1/110.md)==>编码的基础知识，python中避免汉字乱码
    - [列表(1)](Chapter1/111.md)==>列表定义，索引和切片，列表反转，元素追加，基本操作
    - [列表(2)](Chapter1/112.md)==>列表append/extend/index/count方法，可迭代的和判断方法，列表原地修改
    - [列表(3)](Chapter1/113.md)==>列表pop/remove/reverse/sort方法
    - [回顾列表和字符串](Chapter1/114.md)==>比较列表和字符串的相同点和不同点
    - [元组](Chapter1/115.md)==>元组定义和基本操作，使用意义
    - [字典(1)](Chapter1/116.md)==>字典创建方法、基本操作（长度、读取值、删除值、判断键是否存在）
    - [字典(2)](Chapter1/117.md)==>字典方法:copy/deepcopy/clear/get/setdefault/items/iteritems/keys/iterkeys/values/itervalues/pop/popitem/update/has_key
    - [集合(1)](Chapter1/118.md)==>创建集合，集合方法：add/update,pop/remove/discard/clear，可哈希与不可哈希
    - [集合(2)](Chapter1/119.md)==>不可变集合，集合关系
* [第贰章 语句和文件](Chapter2/README.md)
    - [运算符](Chapter2/120.md)==>算数运算符，比较运算符，逻辑运算符/布尔类型
    - [语句(1)](Chapter2/121.md)==>print, import, 赋值语句、增量赋值
    - [语句(2)](Chapter2/122.md)==>if...elif...else语句，三元操作
    - [语句(3)](Chapter2/123.md)==>for循环，range()，循环字典
    - [语句(4)](Chapter2/124.md)==>并行迭代：zip()，enumerate()，list解析
    - [语句(5)](Chapter2/125.md)==>while循环，while...else，for...else
    - [文件(1)](Chapter2/126.md)==>文件打开，读取，写入
    - [文件(2)](Chapter2/127.md)==>文件状态，read/readline/readlines，大文件读取，seek
    - [迭代](Chapter2/128.md)==>迭代含义，iter()
    - [练习](Chapter2/129.md)==>通过四个练习，综合运用以前所学
    - [自省](Chapter2/130.md)==>自省概念，联机帮助，dir()，文档字符串，检查对象，文档
* [第叁章 函数](Chapter3/README.md)
    - [函数(1)](Chapter3/201.md)==>定义函数方法，调用函数方法，命名方法，使用函数注意事项
    - [函数(2)](Chapter3/202.md)==>函数返回值，函数文档，形参和实参，命名空间，全局变量和局部变量
    - [函数(3)](Chapter3/203.md)==>收集参数:`*`和`**`，及其逆过程，复习参数知识
    - [函数(4)](Chapter3/204.md)==>递归和filter、map、reduce、lambda、yield
    - [函数练习](Chapter3/205.md)==>解一元二次方程，统计考试成绩，找素数
#第贰季 进阶
* [第肆章 类](Chapter4/README.md)
    - [类(1)](Chapter4/206.md)==>类的初步认识和基本概念理解：问题空间、对象、面向对象、类和实例化类
    - [类(2)](Chapter4/207.md)==>新式类和旧式类，类的命名，构造函数，实例化及方法和属性，self的作用
    - [类(3)](Chapter4/208.md)==>类属性和实例属性，类内外数据流转，命名空间、作用域
    - [类(4)](Chapter4/209.md)==>继承，多重继承，super函数
    - [类(5)](Chapter4/210.md)==>静态方法和类方法，两者的区别，类的文档
    - [多态和封装](Chapter4/211.md)==>多态，封装和私有化
    - [特殊方法(1)](Chapter4/212.md)==>`__dict__`和`__slots__`
    - [特殊方法(2)](Chapter4/213.md)==>`__getattr__`,`__setattr__`以及查找属性顺序
    - [迭代器](Chapter4/214.md)==>迭代器方法`__iter__`,`netx()`
    - [生成器](Chapter4/215.md)==>生成器定义，yield，生成器方法
* [第伍章 错误和异常](Chapter5/README.md)
    - [错误和异常(1)](Chapter5/216.md)==>什么是错误和异常，常见异常类型，处理异常(try...except...)
    - [错误和异常(2)](Chapter5/217.md)==>处理多个异常，else子句，finally子句
    - [错误和异常(3)](Chapter5/218.md)==>assert断言，异常小结
* [第陆章 模块](Chapter6/README.md)
    - [编写模块](Chapter6/219.md)==>模块是程序，模块的位置
    - [标准库(1)](Chapter6/220.md)==>引用模块的方式，dir()查看属性和方法，模块文档和帮助
    - [标准库(2)](Chapter6/221.md)==>sys，copy
    - [标准库(3)](Chapter6/222.md)==>os模块：操作文件、目录，查看修改属性，执行系统命令，打开网页
    - [标准库(4)](Chapter6/223.md)==>堆的基本知识，heapq模块，deque模块
    - [标准库(5)](Chapter6/224.md)==>calendar模块、time模块、datetime模块
    - [标准库(6)](Chapter6/225.md)==>urllib模块、urllib2模块
    - [标准库(7)](Chapter6/226.md)==>xml.etree.ElementTree模块：遍历查询、增删改查xml，应用实例
    - [标准库(8)](Chapter6/227.md)==>json模块：dumps(),loads(),dump(),load()，自定义类型数据的json编码和解码
    - [第三方库](Chapter6/228.md)==>第三方库的模块安装方法，以requests模块为例说明
* [第柒章 保存数据](Chapter7/README.md)
    - [将数据存入文件](Chapter7/229.md)==>pickle模块，shelve模块
    - [MySQL数据库(1)](Chapter7/230.md)==>MySQL概况，安装，python连接MySQL模块和方法
    - [MySQL数据库(2)](Chapter7/231.md)==>连接对象方法，游标对象方法：数据库的增删改查基本操作
    - [MongoDB数据库](Chapter7/232.md)==>mongodb的安装启动，pymongo模块：连接客户端，数据库的增删改查操作
    - [SQLite数据库](Chapter7/233.md)==>通过sqlite3模块操作SQLite数据库：连接对象方法，游标对象方法，数据库增删改查
    - [电子表格](Chapter7/234.md)==>python操作Excel文件的第三方库openpyxl使用方法，以及其它与Excel相关的第三方库
#第叁季 实战
* [引](./300.md)
* [第捌章 用Tornado做网站](Chapter8/README.md)
    - [为做网站而准备](Chapter8/301.md)==>开发框架，python的常用web框架，tornado框架介绍和安装
    - [分析Hello](Chapter8/302.md)==>发布tornado做的网站，并剖析基本结构
    - [用tornado做网站(1)](Chapter8/303.md)==>网站的基本结构，一个基于tornado框架的网站架子
* 第五部分：科学计算
* [附：网络文摘](appendix/README.md)
    - [如何成为python高手](appendix/n001.md)
    - [ASCII、Unicode、GBK和UTF-8字符编码的区别联系](appendix/n002.md)
