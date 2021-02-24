def checkorders(orders: [str]) -> [bool]:
    results = []
    for i in orders:
        flag = True
        stock = []
        for j in i:
            if j in '([{':
                stock.append(j)
            else:
                if stock == []:
                    flag = False
                    break
                symbol = stock.pop()
                if not match(symbol, j):
                    flag = False
                    break
        if stock != []:
            flag = False
        results.append(flag)
    return results

def match(opens,closers):
    return '([{'.index(opens) == ')]}'.index(closers)

print(checkorders(['()','(','{}[]','[][][]','[{]{]']))
