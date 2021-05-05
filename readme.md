# Cryptocurrency profit

This tool is used to calculate each cryptocurrency profit in Binace.

## requirements
```
prettytable
binance
```

## usage

```
python crypto_profit/profit.py

optional arguments:
-h, --help            show this help message and exit
--key KEY             the binance api key.
--secret SECRET       the binace api secret
--symbols SYMBOLS [SYMBOLS ...]
                        the symbols to calcuate
```

## examples

``` bash
python crypto_profit/profit.py --key {replace with your binance api key} \
--secret {replace with your binance api secret} \
--symbols BTCUSDT CHZUSDT DOGEUSDT LINKUSDT ADAUSDT FILUSDT MANAUDST NANOUSDT SUPERUSDT CHRUSDT
```

the result should be like this:

``` bash
+-----------+---------------------+----------------+--------------------+--------------------+--------------------+---------------------+---------------------+
|    名称   |      持仓成本价     |    当前价格    |      持仓数量      |    持仓成本总价    |      当前总价      |       持仓收益      |      持仓收益率     |
+-----------+---------------------+----------------+--------------------+--------------------+--------------------+---------------------+---------------------+
|  DOGEUSDT |         0.27        |   0.65957546   | 740.6000000000001  | 199.96200000000005 | 488.48158567600007 |    288.519585676    |  144.28720740740738 |
|  LINKUSDT |        37.024       |  48.71868101   |       10.803       |     399.970272     | 526.3079109510301  |  126.33763895103004 |  31.586757265557463 |
| SUPERUSDT |        2.307        |   2.48316647   |       51.902       |     119.737914     |  128.88130612594   |  9.143392125939997  |  7.6361712180320795 |
|  CHZUSDT  |  0.4916440873015874 |   0.51042738   |       882.0        | 433.63008500000007 |    450.19694916    |  16.56686415999991  |  3.8205061717523408 |
|  ADAUSDT  |  1.3302302008914944 |   1.33738024   |       163.77       | 217.85180000000005 | 219.02276190480003 |  1.1709619047999809 |  0.5375038924626685 |
|  NANOUSDT |         10.0        |   9.82731951   |       15.88        |       158.8        | 156.05783381880002 |  -2.742166181199991 |  -1.726804899999994 |
|  BTCUSDT  |       56750.71      | 55303.93435996 |      0.00236       |    133.9316756     | 130.5172850895056  | -3.4143905104943997 | -2.5493524927529467 |
|  FILUSDT  |        158.58       |  149.24712278  |       1.2611       | 199.98523800000004 | 188.21554653785805 | -11.769691462141992 |  -5.885280123596923 |
|  CHRUSDT  | 0.43028000000000005 |   0.37330434   | 232.39999999999998 |     99.997072      | 86.75592861599999  | -13.241143384000011 | -13.241531096030497 |
+-----------+---------------------+----------------+--------------------+--------------------+--------------------+---------------------+---------------------+
```