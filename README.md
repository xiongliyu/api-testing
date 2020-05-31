# api-testing



> 这是一个练习接口测试的demo

##### 第一步：下载该项目

`cd your project`

`git clone https://github.com/xiongliyu/api-testing.git`



##### 第二步：创建一个虚拟环境



> 这一步可以跳过，不会影响项目运单。建议还是创建一个独立环境

- 2.1 (全局)安装虚拟环境：`pip install virtualenv`

- 2.2 进入到项目根目录: `cd api-testing `

- 2.3 然后cmd环境下创建虚拟环境: `virtualenv venv`

- 2.4 此时，根目录中多了一个目录**venv**，这是我们创建的虚拟环境

- 2.5 进入虚拟环境：`.\venv\Scripts\activate`,目录前多了一个`（venv）`就可以了





##### 第三步：下载测试服务

> 测试服务是我在某教材中看到的，所以需要安装

`cd testingServices ` 进入依赖服务下载目录

`git clone https://github.com/xiongliyu/Battle.git`

##### 第四部：根据依赖服务，安装依赖包 

``` 
pip install -r requirements.txt
```



安装完成后环境就搭建好了，如何使用可以查看src里面的README