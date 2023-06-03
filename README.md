## Introduction

AKLite is a lite version of AKShare, which will be used in the future to support the AKShare project.

## Installation

```shell
pip install aklite
```

## Usage

```python
import aklite as ai

stock_hist_em_df = ai._stock_zh_a_hist()
print(stock_hist_em_df)
```

```shell
              日期     开盘     收盘     最高  ...    振幅    涨跌幅   涨跌额   换手率
0     1991-04-03  49.00  49.00  49.00  ...  0.00  22.50  9.00  0.00
1     1991-04-04  48.76  48.76  48.76  ...  0.00  -0.49 -0.24  0.00
2     1991-04-05  48.52  48.52  48.52  ...  0.00  -0.49 -0.24  0.00
3     1991-04-06  48.28  48.28  48.28  ...  0.00  -0.49 -0.24  0.00
4     1991-04-08  48.04  48.04  48.04  ...  0.00  -0.50 -0.24  0.00
          ...    ...    ...    ...  ...   ...    ...   ...   ...
7677  2023-05-29  12.11  11.98  12.13  ...  1.49  -0.99 -0.12  0.29
7678  2023-05-30  11.98  11.87  11.99  ...  1.59  -0.92 -0.11  0.39
7679  2023-05-31  11.82  11.60  11.84  ...  2.19  -2.27 -0.27  0.61
7680  2023-06-01  11.60  11.59  11.68  ...  1.55  -0.09 -0.01  0.38
7681  2023-06-02  11.68  11.93  11.97  ...  2.85   2.93  0.34  0.63
[7682 rows x 11 columns]
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


