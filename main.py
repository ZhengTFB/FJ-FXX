import json
import threading
import asyncio
import subprocess
import random
import It_Ck
import meg
import xsd


# 没有安装自动安装 jieba 库
if not It_Ck.module_exists('jieba'):
    print('检测到你未安装 jieba 库，正在自动安装，请稍等...')
    subprocess.run(['pip', 'install', 'jieba'])
    print('jieba 安装完成。')
else:
    # 引入 jieba 库
    import jieba
    #禁止显示jieba输出
    import logging
    logging.disable(logging.WARNING)

#没有安装自动安装 Levenshtein 库
if not It_Ck.module_exists('Levenshtein'):
    print('检测到你未安装 Levenshtein 库，正在自动安装，请稍等...')
    subprocess.run(['pip', 'install', 'python-Levenshtein'])
    print('Levenshtein 安装完成。')
else:
    # 引入文本相似度匹配库
    import Levenshtein

# 加载 json 数据文件
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义机器人类
class Bot:
    def __init__(self):
        self.quit = False  # 是否退出程序的标志

    # 判断输入的问题是否能从 json 数据中得到回答
    def find_answer(self, question):
        answers = []
        for item in data['questions']:
            # 使用 jieba 分词对问题进行处理
            question_words = list(jieba.cut(question))
            item_words = list(jieba.cut(item['question']))
            # 计算问题与库中每个问题的相似度
            sim = Levenshtein.ratio(' '.join(question_words), ' '.join(item_words))
            # 如果相似度高于设定阈值，将对应答案加入候选答案列表中
            if sim > 0.7:
                answers.extend(item['answers'])
        # 如果候选答案列表非空，从其中随机选择一条返回
        if answers:
            return random.choice(answers)
        # 从默认答案中随机选择一条返回
        else:
            default_answers = ['你能再换个问题吗？', '有点困惑，没听懂呢','额，我没听懂...', '人类的语言真是博大精深，我没听懂你在说什么','能换个说法吗？', '真不好意思，我还不够智能，没听懂你的话']
            return random.choice(default_answers)


    # 交互的主循环
    async def interact(self):
        while not self.quit:
            question = input('请输入问题>>>')
            if question == '退出':
                self.quit = True
                break
            elif xsd.vague(question,'你好')>=0.30 :
                answers =[ "你好啊，今天过的怎么样？","你好！很高兴认识你","您好，我是FJ-FXX，一个能回答您问题的智能机器人。","FJ-FXX在，怎么了么？"]
                answer='FJ-FXX:'+random.choice(answers)
            elif xsd.vague(question,'您好')>=0.30 :
                answers =[ "你好啊，今天过的怎么样？","你好！很高兴认识你","您好，我是FJ-FXX，一个能回答您问题的智能机器人。","FJ-FXX在，怎么了么？"]
                answer='FJ-FXX:'+random.choice(answers)
            else:
                answer = self.find_answer(question)
                answer='FJ-FXX:' +answer
            meg.yanshi(answer,0.1)
meg.yanshi('===============================================',0.007)
meg.yanshi('''欢迎使用FJ-FXX！
这是一个免费、开源的数据库型的ai
开源地址：https://github.com/zhengtfb/FJ-FXX/
版本号：1.0.1   作者：正钛汾钸
如果你想加入这个智障机器人的重写计划，欢迎qq联系作者:3568869968''',0.01)
meg.yanshi('===============================================',0.007)
bot = Bot()
asyncio.run(bot.interact())
