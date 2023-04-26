"""
20230426修改
实现相加函数：
    计算范围为-99到99的整数和浮点数
    方法需要传递a和b两个参数
    若参数超出范围，打印提示语，返回提示信息
    传入在范围内的参数，方法返回a与b相加的结果
    就合法合规
"""

# 判断入参是否符合要求


def check_input(x):
    if not (isinstance(x, int)  or isinstance(x, float)):
        return "is invalid input due to data format."
    elif x < -99 or x > 99:
        return "is invalid input due to data value."
    else:
        return "OK"

# 相加函数


def add(a, b):
    if check_input(a) == "OK":
        if check_input(b) == "OK":
            return a + b
        else:
            return f"b {check_input(b)}"
    else:
        return f"a {check_input(a)}"


if __name__ == '__main__':
    print(add(1, 0)) # ab都是int
    print(add(-0.01, 0.02)) # ab都是float
    print(add(-0.01, 0)) # a float b int
    print(add(99.0011, 0)) # a不在范围
    print(add(1, -99.01)) # b不在范围
    print(add("文", 9.3)) # a非int 非 float, b数据类型符合要求
    print(add(10.01, "")) # b非int 非 float, a数据类型符合要求

