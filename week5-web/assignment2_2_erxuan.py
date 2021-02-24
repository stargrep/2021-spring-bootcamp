def slowest(orders: [[]]) -> int:
    broker_dict = {}
    for item in orders:
        if orders.index(item) == 0:
            broker_dict[item[0]] = [item[1]]
        else:
            if item[0] not in broker_dict:
                broker_dict[item[0]] = [item[1] - orders[(orders.index(item) - 1)][1]]
            else:
                broker_dict[item[0]].append(item[1] - orders[(orders.index(item) - 1)][1])
    broker_dict2 = {}
    for key,value in broker_dict.items():
        broker_dict2[key] = max(value)

    m_max = max(list(broker_dict2.values()))
    for key,value in broker_dict2.items():
        if value == m_max:
            return key


print(slowest([[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]))