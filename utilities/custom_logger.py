import inspect
import logging

"""
inspect.stack()返回当前的堆栈帧列表。
inspect.stack()[1]获取堆栈中的第二个元素，即调用customLogger函数的函数的帧。堆栈的第一个元素（inspect.stack()[0]）
通常是当前执行的帧（在这个例子中是customLogger函数自身的帧），而第二个元素则是调用customLogger的上一级函数的帧。
[3]从这个帧元组中获取第四个元素，即函数名。这是因为在帧元组中，函数名位于索引3的位置。
"""


def customLogger(logLevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %H:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    # 在添加日志处理器之前写入分界线
    with open("automation.log", "a") as logFile:
        logFile.write("\n---------------------\n")

    logger.addHandler(fileHandler)

    return logger
