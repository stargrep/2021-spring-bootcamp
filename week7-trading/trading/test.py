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


slowest([[1, 2], [2, 5], [5, 10], [1, 17]])