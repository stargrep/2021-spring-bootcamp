# Question 1
# checkOrders(["()", "(", "{}[]", "[][][]", "[{]{]"] return [True, False, True, True, False]
#
# SYMBOLS = {'}': '{', ']': '[', ')': '(', '>': '<'}
# SYMBOLS_L, SYMBOLS_R = SYMBOLS.values(), SYMBOLS.keys()
# def check_orders(s):
#     q = 0
#     w = 0
#     arr = []
#     result = []
#     for i in s:
#         for c in i:
#             if c in SYMBOLS_L:
#                 arr.append(c)
#                 q += 1
#             elif c in SYMBOLS_R:
#                 w += 1
#                 if arr and arr[-1] == SYMBOLS[c]:
#                     arr.pop()
#                 else:
#                     result.append(False)
#                     break
#         if q == w:
#             result.append(True)
#         else:
#             result.append(False)
#
#     print(result)
# a = ["()", "(", "{}[]", "[][][]", "[{]{]"]
# check_orders(a)

#两个函数
sym = {'}': '{', ']': '[', ')': '(', '>': '<'}
sym_l, sym_r = sym.values(), sym.keys()
def check_orders(str):
    q = 0
    w = 0
    stack = []
    for char in str:
        # 如果是左括号
        if char in sym_l:
            # 入栈
            stack.append(char)
            q += 1
        # 右括号
        elif char in sym_r:
            w += 1
            if stack and stack[-1] == sym[char]:
                # 出栈
                stack.pop()
            # 匹配成功
            else:
                return False
    if q != w:
        return False
    else:
        return True

def orders(lis):
    result = []
    for i in lis:
        result.append(check_orders(i))
    return result



# Question 2
def slowest(orders):
    brokers_second = []
    for i in range(len(orders)):
        b_second = [orders[i][0]]
        if i == 0:
            time = orders[i][1]
            b_second.append(time)
        else:
            time = orders[i][1] - orders[i-1][1]
            b_second.append(time)
        brokers_second.append(b_second)
    for j in range(len(brokers_second)-1):
        for k in range(len(brokers_second)-j-1):
            if brokers_second[k][1] > brokers_second[k+1][1]:
                a = brokers_second[k]
                brokers_second[k] = brokers_second[k + 1]
                brokers_second[k + 1] = a
    return brokers_second[-1][0]

