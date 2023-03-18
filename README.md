# FJ-FXX
#### 一个数据库型机器人
![alt FJ-FXX](https://github.com/zhengtfb/FJ-FXX/blob/main/FJ-FXX%E5%AE%A3%E4%BC%A0%E5%9B%BE.png)

### 0.名字的由来
~~班里有个同学叫樊剑~~

### 1.总体介绍
FJ-FXX是正钛汾钸在2023.3.18发布的数据库型机器人框架
- 支持中文模糊匹配
- 数据库修改简单
- ~~智障~~

### 2.代码介绍
#### 1.使用异步函数、多线程实现快到起飞地运行效率
    import threading   
    import asyncio
#### 2.库安装检测
自带库检测功能，未安装的库自动安装
    # 没有安装自动安装 jieba 库
    if not It_Ck.module_exists('jieba'):
        print('检测到你未安装 jieba 库，正在自动安装，请稍等...')
        subprocess.run(['pip', 'install', 'jieba'])
        print('jieba 安装完成。')
    else:
        # 引入 jieba 库
        import jieba

    # 没有安装自动安装 Levenshtein 库
    if not It_Ck.module_exists('Levenshtein'):
        print('检测到你未安装 Levenshtein 库，正在自动安装，请稍等...')
        subprocess.run(['pip', 'install', 'python-Levenshtein'])
        print('Levenshtein 安装完成。')
    else:
        # 引入文本相似度匹配库
        import Levenshtein
### 提供Levenshtein和vague两种文本比对方式
- Levenshtein对语义识别敏感    
    import Levenshtein
- vague注重文本自身相似度比较    


    
