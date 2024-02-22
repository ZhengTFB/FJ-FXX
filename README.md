# 🚀FJ-FXX 
#### ✨一个数据库型机器人✨

### 1.总体介绍
- 是您的贴心智能助手🤗，通过Python编程语言和数据库，为您提供快速高效的问题解答
- FJ-FXX的多线程和异步函数保证了您的问题能够被高速响应💨
- 具备易于操作的命令行🖥️界面，FJ-FXX让您和机器的交流变得更加简单和顺畅🎯
- 支持中文模糊匹配🔍
- 数据库🗄️修改简单
- ~~智障~~

### 2.代码介绍
#### 1.使用异步函数、多线程实现快到起飞🛩️地运行效率
    import threading   
    import asyncio
#### 2.库安装检测🤩
自带库检测功能，未安装的库自动安装

    if not It_Ck.module_exists('jieba'):
        print('检测到你未安装 jieba 库，正在自动安装，请稍等...')
        subprocess.run(['pip', 'install', 'jieba'])
        print('jieba 安装完成')
    else:
        import jieba

    if not It_Ck.module_exists('Levenshtein'):
        print('检测到你未安装 Levenshtein 库，正在自动安装，请稍等...')
        subprocess.run(['pip', 'install', 'python-Levenshtein'])
        print('Levenshtein 安装完成')
    else:
        import Levenshtein
### 3.提供Levenshtein和vague两种文本💬比对方式
- Levenshtein对语义识别敏感    
- vague注重文本自身相似度比较
 
