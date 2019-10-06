
## 说明

这个项目是从github项目[JavaGuide](https://github.com/Snailclimb/JavaGuide)复制过来的，有心做一个与Python相关的项目，主要是为了面试复习所用。正在更改与完善中。


## 目录

- [Python](#Python)
- [网络](#网络)
- [操作系统](#操作系统)
    - [Linux相关](#linux相关)
- [数据结构与算法](#数据结构与算法)
    - [数据结构](#数据结构)
    - [算法](#算法)
- [数据库](#数据库)
    - [MySQL](#mysql)
    - [Redis](#redis)
- [系统设计](#系统设计)
    - [常用框架(Spring/SpringBoot、Zookeeper ... )](#常用框架)
    - [权限认证](#权限认证)
    - [设计模式(工厂模式、单例模式 ... )](#设计模式)
    - [数据通信(消息队列、Dubbo ... )](#数据通信)
    - [网站架构](#网站架构)
- [面试指南](#面试指南)
    - [备战面试](#备战面试)
    - [常见面试题总结](#常见面试题总结)
    - [面经](#面经)
- [工具](#工具)
    - [Git](#git)
    - [Docker](#Docker)
- [资源](#资源)
    - [书单](#书单)
    - [Github榜单](#Github榜单)
- [待办](#待办)
- [说明](#说明)

## Python

### 基础

* **[Python 基础知识回顾](docs/Python)**

## 网络

* [计算机网络常见面试题](docs/计算机网络/计算机网络.md)
* [计算机网络基础知识总结](docs/计算机网络/干货：计算机网络知识总结.md)
* [HTTPS中的TLS](docs/计算机网络/HTTPS中的TLS.md)

## 操作系统

### Linux相关

* [后端程序员必备的 Linux 基础知识](docs/操作系统/Linux基础知识.md)  
* [Shell 编程入门](docs/操作系统/Shell.md) 

## 数据结构与算法

### 数据结构

- [数据结构知识学习与面试](docs/数据结构与算法/数据结构.md)

### 算法

- [算法学习资源推荐](docs/数据结构与算法/算法学习资源推荐.md)  
- [几道常见的字符串算法题总结 ](docs/数据结构与算法/几道常见的子符串算法题.md)
- [几道常见的链表算法题总结 ](docs/数据结构与算法/几道常见的链表算法题.md)   
- [剑指offer部分编程题](docs/数据结构与算法/剑指offer部分编程题.md)
- [公司真题](docs/数据结构与算法/公司真题.md)
- [回溯算法经典案例之N皇后问题](docs/数据结构与算法/Backtracking-NQueens.md)

## 数据库

### MySQL

* **[MySQL 学习与面试](docs/数据库/MySQL.md)**
* **[一千行MySQL学习笔记](docs/数据库/一千行MySQL命令.md)**
* [MySQL高性能优化规范建议](docs/数据库/MySQL高性能优化规范建议.md)
* [数据库索引总结](docs/数据库/MySQL%20Index.md)
* [事务隔离级别(图文详解)](docs/数据库/事务隔离级别(图文详解).md)
* [一条SQL语句在MySQL中如何执行的](docs/数据库/一条sql语句在mysql中如何执行的.md)

### Redis

* [Redis 总结](docs/数据库/Redis/Redis.md)
* [Redlock分布式锁](docs/数据库/Redis/Redlock分布式锁.md)
* [如何做可靠的分布式锁，Redlock真的可行么](docs/数据库/Redis/如何做可靠的分布式锁，Redlock真的可行么.md)

## 系统设计

### 常用框架

#### Spring/SpringBoot

- [Spring 学习与面试](docs/系统设计/framework/spring/Spring.md)
- **[Spring 常见问题总结](docs/系统设计/framework/spring/SpringInterviewQuestions.md)**
- **[SpringBoot 指南/常见面试题总结](https://github.com/Snailclimb/springboot-guide)**
- [Spring中bean的作用域与生命周期](docs/系统设计/framework/spring/SpringBean.md)
- [SpringMVC 工作原理详解](docs/系统设计/framework/spring/SpringMVC-Principle.md)
- [Spring中都用到了那些设计模式?](docs/系统设计/framework/spring/Spring-Design-Patterns.md)

#### ZooKeeper

- [ZooKeeper 相关概念总结](docs/系统设计/framework/ZooKeeper.md)
- [ZooKeeper 数据模型和常见命令](docs/系统设计/framework/ZooKeeper数据模型和常见命令.md)

### 权限认证

- **[权限认证基础:区分Authentication,Authorization以及Cookie、Session、Token](docs/系统设计/authority-certification/basis-of-authority-certification.md)**
- **[适合初学者入门 Spring Security With JWT 的 Demo](https://github.com/Snailclimb/spring-security-jwt-guide)**

### 设计模式

- [设计模式系列文章](docs/系统设计/设计模式.md)

### 数据通信

- [数据通信(RESTful、RPC、消息队列)相关知识点总结](docs/系统设计/data-communication/summary.md)
- [Dubbo 总结：关于 Dubbo 的重要知识点](docs/系统设计/data-communication/dubbo.md)
- [消息队列总结](docs/系统设计/data-communication/message-queue.md)
- [RabbitMQ 入门](docs/系统设计/data-communication/rabbitmq.md)
- [RocketMQ的几个简单问题与答案](docs/系统设计/data-communication/RocketMQ-Questions.md)
- [Kafka系统设计开篇-面试看这篇就够了](docs/系统设计/data-communication/Kafka系统设计开篇-面试看这篇就够了.md)

### 网站架构

- [一文读懂分布式应该学什么](docs/系统设计/website-architecture/分布式.md)
- [8 张图读懂大型网站技术架构](docs/系统设计/website-architecture/8%20张图读懂大型网站技术架构.md)
- [【面试精选】关于大型网站系统架构你不得不懂的10个问题](docs/系统设计/website-architecture/【面试精选】关于大型网站系统架构你不得不懂的10个问题.md)

## 面试指南

### 备战面试

* **[【备战面试1】程序员的简历就该这样写](docs/简历与面经/PreparingForInterview/程序员的简历之道.md)**
* **[【备战面试2】初出茅庐的程序员该如何准备面试？](docs/简历与面经/PreparingForInterview/interviewPrepare.md)**
* **[【备战面试3】7个大部分程序员在面试前很关心的问题](docs/简历与面经/PreparingForInterview/JavaProgrammerNeedKnow.md)**
* **[【备战面试4】Github上开源的Java面试/学习相关的仓库推荐](docs/简历与面经/PreparingForInterview/JavaInterviewLibrary.md)**
* **[【备战面试5】如果面试官问你“你有什么问题问我吗？”时，你该如何回答](docs/简历与面经/PreparingForInterview/如果面试官问你"你有什么问题问我吗？"时，你该如何回答.md)**
* **[【备战面试6】美团面试常见问题总结（附详解答案）](docs/简历与面经/PreparingForInterview/美团面试常见问题总结.md)**

### 常见面试题总结

* [第一周（2018-8-7）](docs/简历与面经/MostCommonJavaInterviewQuestions/第一周（2018-8-7）.md) (为什么 Java 中只有值传递、==与equals、 hashCode与equals)
* [第二周（2018-8-13）](docs/简历与面经/MostCommonJavaInterviewQuestions/第二周(2018-8-13).md)(String和StringBuffer、StringBuilder的区别是什么？String为什么是不可变的？、什么是反射机制？反射机制的应用场景有哪些？......)
* [第三周（2018-08-22）](docs/java/collection/Java集合框架常见面试题.md) （Arraylist 与 LinkedList 异同、ArrayList 与 Vector 区别、HashMap的底层实现、HashMap 和 Hashtable 的区别、HashMap 的长度为什么是2的幂次方、HashSet 和 HashMap 区别、ConcurrentHashMap 和 Hashtable 的区别、ConcurrentHashMap线程安全的具体实现方式/底层具体实现、集合框架底层数据结构总结）
* [第四周(2018-8-30).md](docs/简历与面经/MostCommonJavaInterviewQuestions/第四周(2018-8-30).md) （主要内容是几道面试常问的多线程基础题。）

### 面经

- [5面阿里,终获offer(2018年秋招)](docs/简历与面经/BATJrealInterviewExperience/5面阿里,终获offer.md)
- [蚂蚁金服2019实习生面经总结(已拿口头offer)](docs/简历与面经/BATJrealInterviewExperience/蚂蚁金服实习生面经总结(已拿口头offer).md)
- [2019年蚂蚁金服、头条、拼多多的面试总结](docs/简历与面经/BATJrealInterviewExperience/2019alipay-pinduoduo-toutiao.md)

## 工具

### Git

* [Git入门](docs/tools/Git.md)

### Docker

* [Docker 入门](docs/tools/Docker.md)
* [一文搞懂 Docker 镜像的常用操作！](docs/tools/Docker-Image.md)
