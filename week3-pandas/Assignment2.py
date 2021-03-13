# 1.交易传输指令经常需要验证完整性，比如以下的例子
# { request :
# { order# : 1,
#    Execution_details: ['a', 'b', 'c'],
# request_time: "2020-10-10T10:00EDT"
# },
#     checksum:1440
# ...
# }
# 可以通过很多种方式验证完整性，假设我们通过判断整个文本中的括号 比如 '{}', '[]', '()' 来判断下单是否为有效的。
# 比如 {{[],[]}}是有效的，然而 []{[}](是无效的。
# 写一个python 程序来进行验证。
#  def checkOrders(orders: [str]) -> [bool]:
#  return a list of True or False.
# checkOrders(["()", "(", "{}[]", "[][][]", "[{]{]"] return [True, False, True, True, False]

def checkOrders(orders:[str]) -> [bool]:
    if

# 2.判断最慢的broker公司。
# 我们在进行交易的时候通常会选择一家broker公司而不是直接与交易所交易。
# 假设我们有20家broker公司可以选择，通过一段时间的下单表现(完成交易的时间)，我们希望找到最慢的broker公司并且考虑与其解除合约。
# 我们用简单的数据结构表达broker公司和下单时间: [[broker#, 此时秒数]]
# [[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]
# 解读:
# Broker 0 使用了0s - 2s = 2s
# Broker 1 使用了5 - 2 = 3s
# Broker 2 使用了7 - 5 = 2s
# Broker 0 使用了16-7 = 9s
# Broker 3 使用了19-16=3s
# Broker 4 使用了25-19=6s
# Broker 2 使用了35-25=10s
# 综合表现，是broker2出现了最慢的交易表现。
#
# Def slowest(orders: [[]]) -> int:
#
# slowest([[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]) return 2
# slowest([[0,1],[0,3]])

