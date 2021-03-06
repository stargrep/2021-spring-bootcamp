""" DO NOT EDIT (BEGIN) """
import pandas as pd
import datetime as dt

RAW_DATA_NAME = "data/QQQ.csv"
ANALYSIS_RESULT_DATA_NAME = "data/QQQ-result.csv"


def read_data() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_NAME)


def write_data(data: pd.DataFrame) -> None:
    return data.to_csv(ANALYSIS_RESULT_DATA_NAME, index=False)


def is_monday(day: str) -> bool:
    return dt.datetime.strptime(day, '%Y-%m-%d').strftime('%A') == 'Monday'


# 从年数，回报倍数得到年化收益. e.g. 0.1 -> 10% 年化收益
def annual_return(num_of_year: int, times: float) -> float:
    return pow(times, 1 / num_of_year) - 1.0


""" DO NOT EDIT (END) """
read_data()
a = read_data()
print(is_monday(a.iloc[0,8]))

# -- TODO: Part 1 (START)
def calculate_scheduled_investment(data: pd.DataFrame) -> {}:
    shares = 10  # 每次购买 10 share QQQ
    positions = [0.0]
    cost = [0.0]
    assets = [0.0]
    for i in range(1, len(data)):
        open_price = data.iloc[i]['OPEN']
        if is_monday(data.iloc[i,8]):
            positions.append(shares)
            asset_price = open_price * positions[i]
            cost_price = cost[i-1] + open_price * 10
            assets.append(asset_price)
            cost.append(cost_price)
            shares += 10
        else:
            positions.append(positions[i-1])
            cost.append(cost[i-1])
            assets.append(open_price*positions[i])
        # 实现计算方程，每个周一购买shares，其他日期不购买
        #   如果购买，需要增加position仓位，增加cost花费
        #   如果不购买，append前日仓位和花费
        #   然后总需要根据open_price计算asset, 并且加入assets
    return positions, cost, assets

# print(calculate_scheduled_investment(a)[1])

# -- TODO: Part 1 (END)

# print(calculate_scheduled_investment(a)[2])
# -- TODO: Part 2 (START)
def export_result() -> float:
    orig = read_data()
    write_data(orig)
    orig['POSITIONS'] = calculate_scheduled_investment(a)[0]
    write_data(orig)
    orig['COST'] = calculate_scheduled_investment(a)[1]
    write_data(orig)
    orig['ASSETS'] = calculate_scheduled_investment(a)[2]
    write_data(orig)
    # 生成 QQQ-result.csv, 目标是跟QQQ-result-expected.csv 一致
    # 在这里调用 calculate_scheduled_investment, 并且赋值
    # 到asset 和cost.
    # 最后返回十年的年化率
    asset = [1]  # replace
    asset.extend(calculate_scheduled_investment(a)[2])
    cost = [1]  # replace
    cost.extend(calculate_scheduled_investment(a)[1])
    print(asset[-1],cost[-1])
    return annual_return(10, asset[-1] / cost[-1])  # 10 years


# -- TODO: Part 2 (END)


if __name__ == '__main__':
    print("Investment Return: ", export_result())