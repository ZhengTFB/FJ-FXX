# 定义检查模块是否存在的函数
def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True
