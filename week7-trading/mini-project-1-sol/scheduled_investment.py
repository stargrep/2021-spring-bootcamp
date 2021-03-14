""" DO NOT EDIT (BEGIN) """
import pandas as pd
import datetime

RAW_DATA_NAME = "data/QQQ.csv"
ANALYSIS_RESULT_DATA_NAME = "data/QQQ-result.csv"


def read_data() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_NAME)


def write_data(data: pd.DataFrame) -> None:
    return data.to_csv(ANALYSIS_RESULT_DATA_NAME, index=False)


def is_monday(day: str) -> bool:
    return datetime.datetime.strptime(day, '%Y-%m-%d').strftime('%A') == 'Monday'


# 从年数，回报倍数得到年化收益. e.g. 0.1 -> 10% 年化收益
def annual_return(num_of_year: int, times: float) -> float:
    return pow(times, 1 / num_of_year) - 1.0


""" DO NOT EDIT (END) """


# -- TODO: Part 1 (START)
def calculate_scheduled_investment(data: pd.DataFrame) -> {}:
    shares = 2
    positions = [0.0]
    cost = [0.0]
    assets = [0.0]
    for i in range(1, len(data)):
        open_price = data.iloc[i]['OPEN']
        # 实现计算方程，每个周一购买shares，其他日期不购买
        #   如果购买，需要增加position仓位，增加cost花费
        #   如果不购买，append前日仓位和花费
        #   然后总需要根据open_price计算asset, 并且加入assets
        if is_monday(data.iloc[i]['DATES']):
            positions.append(positions[i - 1] + shares)
            cost.append(cost[i - 1] + shares * open_price)
        else:
            positions.append(positions[i - 1])
            cost.append(cost[i - 1])
        assets.append(positions[i] * open_price)
    return positions, cost, assets


# -- TODO: Part 1 (END)


def export_result() -> float:
    data = read_data()

    pos, cost, asset = calculate_scheduled_investment(data)
    data['POSITIONS'] = pos
    data['COST'] = cost
    data['ASSETS'] = asset
    write_data(data)
    return annual_return(10, asset[-1] / cost[-1])  # 10 years


if __name__ == '__main__':
    print("Investment Return: ", export_result())
