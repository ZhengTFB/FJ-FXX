# 🚀FJ-FXX 
#### ✨一个数据库型机器人✨
![alt FJ-FXX](https://github.com/zhengtfb/FJ-FXX/blob/main/FJ-FXX%E5%AE%A3%E4%BC%A0%E5%9B%BE.png)

### 0.名字的由来
~~班里有个同学叫樊剑~~

### 1.总体介绍
FJ-FXX是正钛汾钸在2023.3.18发布的数据库型机器人框架
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
### 3.提供Levenshtein和vague两种文本💬比对方式
- Levenshtein对语义识别敏感    
- vague注重文本自身相似度比较    
### 4.FJ-FXX重写计划🔄
关于FJ-FXX的重写计划，我不得不承认上一次并未如愿，留下了许多智障问题   
我深感歉意💦，所以我希望重构   
如果你有兴趣，邀请您加入我的重写计划，与我一同改进和升级FJ-FXX，让它在未来的发展中变得更加完善    
您可以通过QQ号3568869968或Discord #2223联系我，贡献您的建议和意见。   
让我们共同致力于把智障机器人改为智能机器人，由衷感谢您的支持   
- [x] FJ-FXX 1.0已完成
- [ ] FJ-FXX重写计划    
