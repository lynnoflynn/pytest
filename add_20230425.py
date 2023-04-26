"""
20230425
实现相加函数：
    计算范围为-99到99的整数和浮点数
    方法需要传递a和b两个参数
    若参数超出范围，打印提示语，返回提示信息
    传入在范围内的参数，方法返回a与b相加的结果
    就合法合规
"""


def add_func(a, b):

    # 判断传入参数是否在范围内
    # 若不在范围打印提示语
    if a < -99 or a > 99 or b < -99 or b > 99:
        print("The input is out of range!\nIt should in [-99, 99]")
    # 若在范围内则返回a与b相加的结果
    else:
        print(a + b)


if __name__ == '__main__':
    # 定义输入
    a = -990
    b = 2
    # 调用函数（位置变量）
    add_func(a, b)
    # 定义输入
    a = -9.0
    b = 2
    # 调用函数（位置变量）
    add_func(a, b)
