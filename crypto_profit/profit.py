from binance.client import Client
from prettytable import PrettyTable
import argparse

def calcuate_roi(client, trades):
    """calcuate the symbol trade return of investment
    TODO: seperate the sell and holding
    Args:
        trades (list): trades log
    Return:
        avg_price (float): average price
        profit (float): total profit of this trade (in US Dollar)
        
    """
    holding_avg_price = 0
    holding_amount = 0 # 持仓总数量
    for idx, item in enumerate(trades):
        if item['isBuyer']:
            holding_avg_price = (holding_avg_price*holding_amount+float(item['price'])*float(item['qty']))/(holding_amount+float(item['qty']))
            holding_amount += float(item['qty'])
        else:
            holding_amount -= float(item['qty'])
            holding_avg_price = holding_avg_price
            
    # 持仓成本总金额=买入成本*买入数量-卖出成本*卖出数量
    holding_total = holding_amount*holding_avg_price
    
    # 当前成本价=api获取最新价格
    current_price = float(client.get_avg_price(symbol=trades[0]['symbol'])['price']) #TODO: 这里是5min均价的api接口，后续改成实时接口

    # **持仓收益**=当前成本价*持有总数量-持有成本总金额
    holding_profit = current_price*holding_amount - holding_total

    # **持仓收益率**=(当前成本价-持有成本价)/持有成本价
    holding_profit_percent = (current_price-holding_avg_price)/holding_avg_price*100

    return {'name': trades[0]['symbol'], #名称
            'holding_avg_price': holding_avg_price, #持仓成本价
            'current_price': current_price,  #当前价格
            'holding_amount': holding_amount, #持仓数量
            'holding_value': holding_avg_price*holding_amount, #持仓成本总价
            'current_value': current_price*holding_amount, #当前总价
            'holding_profit':holding_profit,   #持仓收益
            'holding_profit_percent':holding_profit_percent #持仓收益率
            }

def parse_args():
    parser = argparse.ArgumentParser('caucuate the binance holding profit.')
    parser.add_argument('--key', required=True, help='the binance api key.')
    parser.add_argument('--secret', required=True, help='the binace api secret')
    parser.add_argument('--symbols',
        type=str,
        nargs='+',
        default='BTCUSDT',
        help='the symbols to calcuate')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    client = Client(args.key, args.secret)
    
    # 1. get all trade symbol
    all_trade_symbols = client.get_all_tickers()
    
    # 2. iterrate all symbol
    filtered_trade_symbols = [x for x in all_trade_symbols if 'USDT' in x['symbol'] and x['symbol'] in args.symbols]
    roi_result = []
    for item in filtered_trade_symbols:
        symbol = item['symbol']
        trades = client.get_my_trades(symbol=symbol)
        if trades:
            roi_symbol = calcuate_roi(client, trades)
            roi_result.append(roi_symbol)
    roi_result = sorted(roi_result, key=lambda k: k['holding_profit_percent'], reverse=True) 
    summary_table = PrettyTable()
    summary_table.field_names = ['名称','持仓成本价','当前价格','持仓数量','持仓成本总价','当前总价','持仓收益','持仓收益率']
    for item in roi_result:
        summary_table.add_row([item['name'], 
                                item['holding_avg_price'], item['current_price'], 
                                item['holding_amount'], 
                                item['holding_value'], item['current_value'],
                                item['holding_profit'], item['holding_profit_percent']
                                ])
    print(summary_table)

if __name__ == '__main__':
    main()