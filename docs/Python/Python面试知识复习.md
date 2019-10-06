## 1、行为面试

### 0.自我介绍！

### 1.讲讲最有难度的一个项目？
    项目整个流程，项目亮点。

### 2.遇到的困难？（项目、学习）如何解决的？


## 2、Python基础

### 1.Python语言特性
    静态语言 or 动态语言：确定变量类型在编译期间->静态，运行期间确定类型->动态
    强类型 or 弱类型：会发生隐式类型转换->弱类型
    解释性 or 编译性：
    
### 2.Python语言优点、缺点
    胶水语言，轮子多，应用广泛，语言灵活，生产力高，快速构建项目
    性能可能不如静态语言，动态语言通病：代码维护较难，重构吃力，Python2/3不兼容

### 3.鸭子类型
    关注点在对象的行为，对象有哪些接口、方法，而不关注其具体是哪种对象，不同的对象可能有相同的方法，我们就可以简单的把他们看作是一样的。
    比如定义了__iter__魔法方法的对象就可以用for去迭代，这个时候就不用在意他具体是什么类型对象了。

### 4.猴子补丁（monkey patch）
    在运行时替换方法、属性等
    在不修改第三方代码的情况下增加原来不支持的功能
    在运行时为内存中的对象增加patch而不是在磁盘的源代码中增加

Ps：如果两个模块同时打了猴子补丁，只有后打的补丁才有效

示例：
```python
from SomeOtherProduct.SomeModule import SomeClass

def speak(self):
    return "ook ook eee eee eee!"

SomeClass.speak = speak #打补丁
```
很多代码用到 import json，后来发现ujson性能更高，如果觉得把每个文件的import json 改成 import ujson as json成本较高，或者说想测试一下用ujson替换json是否符合预期，只需要在入口加上：
```python
import json  
import ujson  

def monkey_patch_json():  
    json.__name__ = 'ujson'  
    json.dumps = ujson.dumps  
    json.loads = ujson.loads  

monkey_patch_json() 
```

另外就是在代码单元测试的时候，取代某些暂时无法调用的接口，类似unnittest中的接口替换

### 5.Python自省
    运行时判断对象类型。
    Python中比较常见的自省（introspection）机制(函数用法)有： dir()，type(), hasattr(), isinstance()，通过这些函数，我们能够在程序运行时得知对象的类型，判断对象是否存在某个属性，访问对象的属性。
    id()返回内存地址，is关键字判断内存地址是否相同。判断None：None是单例，常用 is 而非 ==

### 6.Python2/3 差异
|Python2|Python3|
|-----------------------------------------------|--------------------------------------------|
|print是关键字|print是函数，能传入参数使输出更加灵活|
|编码是unicode,中文用u'中文汉字'|编码统一使用utf-8|
|/是整除，非整除实现用小数做除数或被除数|/是非整除，新增//是整除|
|无|增加类型注解，可限定传输参数类型，返回类型，方便错误检查|
|无|对super进行了优化，更加简单|
|无|增加 高级解包操作符号 *|
|无|关键字参数|
|返回列表（如xrange()）|返回迭代器/可迭代对象（去除xrange(),只有range()）|
|生成的字节码文件(pyc文件)在当前目录（文件混乱）|统一放到__pycache__目录下|
|其他内置库的修改：urllib,selector等等|

其他Python3新增：
yield from 连接生成器
asyncio内置库来支持异步编程，（使用async/await原生协程来支持）
其他新增库：enum,mock,ipaddress,concurrent,futures
其他性能优化

### 7.Python2/3兼容工具
    six模块
    2to3模块，转换代码


## 3、Python函数常考点

### 1.函数传参
    传参方式：共享传参
    Python一切皆对象，故传参是对对象的引用（非c语言的引用传递）。参数是可变对象，则会改变原值，若是不可变对象，则复制原值加以改变。
不可变对象：bool,int,float,tuple,str,frozenset
可变对象：list,set,dict
不可变对象tuple中若有元素是可变对象，tuple保存的对其的引用不变。可变对象中元素还是可变的。

Ps：函数中可变对象作为默认参数（默认参数只会计算一次）

### 2.可变参数*args 与 关键字参数**kwargs
    *args接收n个位置参数被打包成tuple给函数体调用
    **kwargs接收n个关键字参数被打包成dict给函数体调用
    *args与**kwargs同时存在时，*args在前。
    


## 4、Python面向对象

### 1.面向对象编程
面向对象编程是指把事物抽象成一个个类，其中包含成员（属性）和操作（方法）。程序中不再是一个个函数，而是通过类创建实例（也就是对象），在程序中调用这些实例的方法。

#### 1.面向对象三大特征

面向对象三大特征：封装、继承、多态

**封装：**

通过对象隐藏程序的具体实现细节，将数据与操作包装在一起，对象与对象之间通过方法调用实现交换信息。具体的说就是通过类的方法操作数据成员。

**继承：**

类之间可以继承，通过继承得到的类称为子类，被继承的类为父类，子类相对于父类一般更加具体化，子类可以继承父类的所有代码。子类继承父类，可以实现代码复用。

**多态：**

不同类型的对象上的相同的操作或函数、过程可以获得不同的结果。不同的对象，收到同一消息可以产生不同的结果，这种现象称为多态性。比如子类重写父类的方法，父类子类的这个方法名相同，但被调用时可以返回不同的结构。

**Ps：**在使用类时：组合与继承的选择 --> 在使用组合与继承都能达到目的时，优先使用组合，这样可以保持代码简单。

#### 2.Python类中三种方法

**类方法：**类的方法，可以不实例化直接通过类名调用，类的实例也可以调用。使用"@classmethod"装饰。被装饰的方法的形参为cls表示类本身。

**实例方法：**是类实例化后才能调用的方法，其形参为self表示实例化出来的对象本身。

**静态方法：**是一个任意的函数，不过写在了类里，与类没有什么关系，没有cls或self这种形参。用"@staticmethod"装饰，可通过类名直接调用也可以通过实例化后的对象调用。


### 2.元类

元类（Metaclass）即创建类的类。在Python源码中有这样一个类：
```python
class type(object):
    """
    type(object_or_name, bases, dict)
    type(object) -> the object's type
    type(name, bases, dict) -> a new type
    """
```
他是用来创建类的，它的类初始化方法__init__(cls, what, bases=None, dict=None)接受四个参数。
参数cls：表示接收type类本身作为参数
参数what：创建类的名字
参数bases：是一个元组，表示我们创建出来的这个类继承于那些类
参数dict：是一个字典，表示创建的这个类的属性和方法

如下，我们可以这样来定义一个类：
```python
# 一般定义类的方式：
a = 123

class ClassA(object):
    pass

def function():
    pass

# 通过元类定义类
MyBaseClass = type('MyClass', (ClassA,), {"a": a, "func": function})

# 创建类：
MyClassA = MyBaseClass()
```

#### 自定义元类

元类的主要目的就是为了当创建类时能够自动地改变类。

第一步：继承type
第二步：重写__new__方法实现自己的逻辑
第三步：有需要还可以重写__init__方法

```python
class Metaclass(type):
    def __new__(cls, name, bases, dict):
        attrs = ((name, value) for name, value in dict.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(Metaclass, cls).__new__(cls, name, bases, uppercase_attr)
```
**使用自定义元类：**

在用 class 语句自定义类时，默认 metaclass 是 type，我们也可以指定 metaclass 来创建类。 由于 python3 和 python2 在指定类的 metaclass 语法不兼容，下面分别示例 python2 和 python3 两个版本。


```python

# python2 版本：

class Bar(object):
    __metaclass__ = MetaClass

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

# python3 版本：

class Bar(object, metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

```



## 5、迭代器与生成器
迭代器与生成器：https://www.cnblogs.com/ChangAn223/p/10731104.html



## 6、装饰器

装饰器入门：
https://blog.51cto.com/13885935/2162154

类装饰器：
重写类的__call__方法


## 7、函数式编程

函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。
而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。
函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。Python支持部分函数式编程特性：高阶函数map,reduce,filter

#### 1.高阶函数

map接受一个函数和一个可迭代对象，将可迭代对象的每个元素传入函数得到计算结果，最终返回一个包含这些结果的列表。
reduce同样接受一个函数和一个可迭代对象，将可迭代对象的元素依次传入函数，得到的结果在与后一个元素一起传入函数，最终返回一个结果。
filter同样接受一个函数和一个可迭代对象，将可迭代对象的每个元素传入函数，如果这个函数的计算结果为True则返回该元素，为False则不返回。是个过滤器。

#### 2.闭包

在一个函数中再定义一个函数，再函数里的函数叫内部函数，若内部函数使用了函数外的变量，则称他为闭包，即绑定了外部作用域的变量的函数。
即是离开外部作用域，若闭包任然可见，则绑定变量不会被销毁。每次运行外部函数会重新创建闭包。


## 8、Python异常机制

错误：语法错误又称解析错误
异常：打破程序正常执行流程的一些事件
区别：语句或表达式在语法上是正确的，但在尝试执行时，它仍可能会引发错误。 在执行时检测到的错误被称为异常

BaseException
    基类异常，Python中所有异常都继承它
Exception
    除非系统退出类异常的其他异常的基类，我们自定义的异常继承它。

**Python层次**
```python
BaseException
 +-- SystemExit     # 解释器请求退出
 +-- KeyboardInterrupt  # 用户中断执行(通常是输入^C)
 +-- GeneratorExit  # 生成器(generator)发生异常来通知退出
 +-- Exception      # 常规错误的基类
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      ......
```

### 1.异常处理

When ？什么时候要捕获异常？
```python
网络请求（超时，链接错误等）
资源访问（权限问题，资源不存在等）
代码逻辑（越界，keyError等）

```

How ？怎么处理异常？
```python
try:
    # 可能发生异常的代码
except 异常种类(一个或多个) as e:
    # 异常处理
else:
    # 没有异常时的操作
finally:
    # 不论有没有异常都会执行的代码

```

### 2.自定义异常
异常通常应该直接或间接地从 Exception 类派生。大多数异常都定义为名称以“Error”结尾，类似于标准异常的命名。

示例：
```python
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

```

抛出自定义的异常：raise

**自定义为什么通常不继承 BaseException ?**
    如果继承BaseException，在捕获多个自定义异常时，通常在except处写他们的父类，这样的话，就会把其他系统推出类异常捕获到进行处理。
    如 ctrl c 中断程序这个异常被捕获，是我们在想要中断程序运行时按 ctrl c 失效。
    我们继承Exception，就可以直接捕获到Exception下所有子类异常包括我们自定义的异常。


## 9、线程、进程、协程

**进程：**程序运行的过程。是计算机中的程序关于某数据集合上的一次运行活动。
**线程：**进程内的一个实际执行单位。一条线程指的是进程中一个单一顺序的控制流。
**协程：**由程序（用户）自己控制的一个子程序/函数，再运行时其内部可中断转而执行别的子程序，再适当的时候再返回来接着执行。

**进程与线程区别、联系：**
 - 调度：进程的调度实际上实际上是调度其内部的线程去运行。线程是cpu调度和分配的基本单位。
 - 并发性：进程之间可以并发执行，线程之间也可以并发执行。
 - 拥有资源：进程是拥有系统资源的基本单位。由操作系统为其分配系统资源（cpu时间片、内存等）。线程基本不拥有资源，（但有一点自己的堆栈和局部变量），线程共享所属进程的所有资源。
 - 系统开销：在创建或者撤销进程时，由于操作系统要为其分配和回收资源，所以进程创建撤销的开销大于线程。在进程切换时系统开销也大于线程（同一进程下线程切换）。
 - 一个进程可有多个线程，但至少有一个线程（主线程），一个线程只属于一个进程。

**与协程：**
 - 一个线程可有多个协程
 - 同一线程下的多个协程没有进程线程切换的开销，不存在线程安全故不需要锁机制，所以效率更高。
 - 线程进程都是同步机制，协程是异步机制。

### Python进程：multiprocessing.Process

#### 创建进程


#### 多进程、进程池


#### 进程实现生产者消费者模型


#### 守护进程？ deamon



### Python线程：threading.Thread


#### 创建线程



#### 多线程、线程池



#### 线程安全



### Python协程


#### 原生协程


#### async模块


#### 协程实现生产者消费者模型


## 10、Python网络编程

socket编程


## 11、Python内存管理与垃圾回收机制

https://www.cnblogs.com/ChangAn223/p/10943963.html

https://blog.csdn.net/xiongchengluo1129/article/details/80462651



## 12、Python性能分析及优化

### 1.GIL — Global Interpreter LOck(全局解释器锁，Cpython解释器)

如Java有虚拟机，Python也有"虚拟机"，但其实它叫解释器。
Python解释器将源码转换为字节码，然后再由解释器来执行这些字节码。：源代码--->字节码--->解释执行
Python默认解释器时Cpython，他们的内存管理不是线程安全的，为保护多线程之间数据完整性和状态同步，Cpython使用锁机制，于是有了GIL这把超级大锁，使得在任意时刻只有一个线程在解释器中运行。
GIL是一个防止本机多个线程同时执行Python字节码的互斥锁。锁的是解释器（Cpython）。
只有当线程获取到全局解释器锁后才能运行，而全局解释器锁只有一个，因此即使在多核的情况下也只能发挥出单核的功能。

**多线程环境中，python解释器按照以下方式执行：**

1.设置GIL
2.切换到一个线程去执行
2.运行代码，这里有两种机制：
    - 指定数量的字节码指令（100个，有个ticks在计数）
    - 固定时间15ms线程主动让出控制
3.线程进入阻塞状态
4.释放GIL
5.再次重复以上步骤

GIL缺点：
    限制了程序的多核执行，无法发挥多核机器的优势
    cpu密集型程序难以利用多核执行任务

GIL会根据执行的字节码行数和时间片来释放GIL，在遇到IO操作的时候会主动释放以给其他线程，其他线程之间竞争Gil锁。

### 2.规避GIL的影响
1. 区分IO密集型任务和CPU密集型任务，CPU密集型任务采用多进程、进程池的方式。IO密集型由于影响很小仍可以采用多线程执行任务。
2. 用其他解释器，如Jpython、IronPython，但这样失去了利用社区众多C语言模块有用特性的机会。

### 3.有了GIL还有关注线程安全？
是的，在Python中原子操作是线程安全的（因为Python解释器只有在一个机器指令完成后另一个机器指令未开始前进行线程切换）。但是非原子操作就需要我们自己来保证线程安全。
原子操作：被编译为单个字节码指令的操作，要么执行成功，要么执行失败并回退已执行的操作。使用dis包可以查看。
Python中相当大一部分操作都是原子的，即使像字典和类成员赋值这样的操作也是原子的。多条语句、运算符"+="等是非原子操作，例如"i=j+1"这样的单挑语句也不是原子操作。

在多线程任务中，非原子操作我们可以使用threading.Lock()来保证线程安全：

```python
import threading

#创建锁
mutex = threading.Lock()
#锁定
mutex.acquire()
#释放
mutex.release()
```
示例：
```python
import threading

lock = threading.Lock()
l = []

def test1(n):
    lock.acquire()
    l.append(n)
    print(l)
    lock.release()

def test(n):
    l.append(n)
    print(l)

def main():
    for i in range(0, 10):
        th = threading.Thread(target=test, args=(i,))
        th.start()
if __name__=="__main__":
    main()

```
结果：
```
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 4.提高Python程序性能的七个小技巧
1. 使用局部变量
尽可能使用局部变量替代全局变量，可以是程序易于维护并且有助于提高性能节约成本。

2. 减少函数调用的数量
当需要确定对象类型时，使用isinstance()方法最好，id()次之，type()最差。
为了避免重复计算，不要把重复操作作为参数放入循环中。
使用模块X中的函数或者对象Y时，应该用from X import Y，而不是import X; X.Y。因为，当使用Y时，可以减少一次查询（解析器不必先找到模块X，然后在模块X的字典中查找Y）。

3. 使用映射来替换条件搜索
映射（例如dict，等等）的搜索速度比条件语句（例如if，等等）快很多。在Python中没有select-case语句。

4. 直接迭代序列元素
对于序列（str, list, tuple, 等等），直接迭代序列元素比迭代元素索引要快。

5. 用生成器表达式替换列表解析
列表解析生成整个列表，会对大量数据的迭代产生负面作用。而生成器表达式不会。生成器表达式不会创建一个列表，相反返回一个生成器，在需要的时候生成具体值（延迟的），这种方式对内存友好。

6. 先编译后调用
当使用函数eval()和exec()来执行代码时，最好调用代码对象（通过compile()函数预先编译成字节码）而不是直接调用str，这样可以避免重复编译过程多次和提高程序的性能。
正则表达式模式匹配是类似的。 在执行比较和匹配之前，最好将正则表达式模式编译为正则表达式对象（通过re.complie()函数）

7. 模块编程的习惯
模块中最高级别的Python语句（无缩进代码）将在导入模块时执行（是否真的需要执行）。 因此，您应该尝试将模块的所有功能代码放入函数中（与主程序相关的功能代码也可以放入main()函数，主程序本身调用main()函数）。
测试代码可以写在模块的main()函数中。 将在主程序中检测__name__的值。 如果是"__main__"（表示模块是直接执行的），则调用main()函数进行测试; 如果它是模块的名称（表示模块被调用），则不会执行测试。

### 5.如何剖析程序性能？
各种profile工具，如内置的profile/cprofile等，其他的如uber开源的pyflame

### 6.从哪些方面优化服务端性能？ Web应用一般语言不是性能瓶颈
1.数据结构与算法的优化
2.数据库层：索引优化，消除慢查询，批量操作以减少IO，其他Nosql
3.网络IO：批量操作，pipline操作减少IO
4.缓存：客户端缓存，使用内存数据库redis等
5.异步：asyncio,celery
6.并发：gevent/多线程



## 13、Python单元测试

自底向上进行测试
保证代码逻辑的正确性
单元测试影响代码设计，容易测试的代码往往是高内聚低耦合的
回归测试，防止修改一处导致整个服务不可用

