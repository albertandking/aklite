## Introduction

AKLite is a lite version of AKShare, which will be used in the future to support the AKShare project.

[Documentation](https://aklite.readthedocs.io/)
[中文文档](https://aklite.readthedocs.io/zh_CN/latest/)

AKLite Features:
1. Small, Fast and Powerful
2. High performance
3. Easy to ues

## Installation

```shell
pip install aklite --upgrade -i https://pypi.org/simple
```

## Usage

```python
import aklite as ai

stock_zh_a_hist_obj = ai.stock_zh_a_hist(symbols=["000001", "000002"],
                                         period="daily",
                                         start_date="20220101", 
                                         end_date="20230601",
                                         adjust="hfq",
                                         timeout=5,
                                         proxies={})
print(stock_zh_a_hist_obj.data)
print(stock_zh_a_hist_obj.columns)
print(stock_zh_a_hist_obj.url)
print(stock_zh_a_hist_obj.desc)
print(stock_zh_a_hist_obj.symbols)
print(stock_zh_a_hist_obj.start_date)
print(stock_zh_a_hist_obj.end_date)
print(stock_zh_a_hist_obj.adjust)
```

```shell
           date  symbol  ...  price_change  turnover_rate
0    2022-01-04  000001  ...         29.26           0.60
1    2022-01-05  000001  ...         79.63           1.01
2    2022-01-06  000001  ...         -4.87           0.57
3    2022-01-07  000001  ...         13.00           0.58
4    2022-01-10  000001  ...         -1.62           0.47
..          ...     ...  ...           ...            ...
677  2023-05-26  000002  ...          2.62           0.42
678  2023-05-29  000002  ...        -23.56           0.46
679  2023-05-30  000002  ...         43.20           0.91
680  2023-05-31  000002  ...        -15.71           0.46
681  2023-06-01  000002  ...        -31.42           0.48
[682 rows x 12 columns]
```

## Contributing

## Translate

```shell
cd docs
sphinx-build -b gettext ./source build/gettext
sphinx-intl update -p ./build/gettext -l zh_CN
```

## Publish

```shell
hatch build
hatch publish
```
