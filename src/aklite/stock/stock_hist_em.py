from functools import lru_cache

import pandas as pd
import httpx
from typing import Union


@lru_cache()
def _code_id_map_em() -> dict:
    """
    东方财富-股票和市场代码
    http://quote.eastmoney.com/center/gridlist.html#hs_a_board
    :return: 股票和市场代码
    :rtype: dict
    """
    url = "http://80.push2.eastmoney.com/api/qt/clist/get"
    params = {
        "pn": "1",
        "pz": "50000",
        "po": "1",
        "np": "1",
        "ut": "bd1d9ddb04089700cf9c27f6f7426281",
        "fltt": "2",
        "invt": "2",
        "fid": "f3",
        "fs": "m:1 t:2,m:1 t:23",
        "fields": "f12",
        "_": "1623833739532",
    }
    r = httpx.get(url, params=params)
    data_json = r.json()
    if not data_json["data"]["diff"]:
        return dict()
    temp_df = pd.DataFrame(data_json["data"]["diff"])
    temp_df["market_id"] = 1
    temp_df.columns = ["sh_code", "sh_id"]
    code_id_dict = dict(zip(temp_df["sh_code"], temp_df["sh_id"]))
    params = {
        "pn": "1",
        "pz": "50000",
        "po": "1",
        "np": "1",
        "ut": "bd1d9ddb04089700cf9c27f6f7426281",
        "fltt": "2",
        "invt": "2",
        "fid": "f3",
        "fs": "m:0 t:6,m:0 t:80",
        "fields": "f12",
        "_": "1623833739532",
    }
    r = httpx.get(url, params=params)
    data_json = r.json()
    if not data_json["data"]["diff"]:
        return dict()
    temp_df_sz = pd.DataFrame(data_json["data"]["diff"])
    temp_df_sz["sz_id"] = 0
    code_id_dict.update(dict(zip(temp_df_sz["f12"], temp_df_sz["sz_id"])))
    params = {
        "pn": "1",
        "pz": "50000",
        "po": "1",
        "np": "1",
        "ut": "bd1d9ddb04089700cf9c27f6f7426281",
        "fltt": "2",
        "invt": "2",
        "fid": "f3",
        "fs": "m:0 t:81 s:2048",
        "fields": "f12",
        "_": "1623833739532",
    }
    r = httpx.get(url, params=params)
    data_json = r.json()
    if not data_json["data"]["diff"]:
        return dict()
    temp_df_sz = pd.DataFrame(data_json["data"]["diff"])
    temp_df_sz["bj_id"] = 0
    code_id_dict.update(dict(zip(temp_df_sz["f12"], temp_df_sz["bj_id"])))
    return code_id_dict


class StockZhAHist:
    def __init__(self,
                 symbols: str | list[str] = "000001",
                 period: str = "daily",
                 start_date: str = "19700101",
                 end_date: str = "20500101",
                 adjust: str = "",
                 *args, **kwargs
                 ):
        self.symbols = symbols
        self.period = period
        self.start_date = start_date
        self.end_date = end_date
        self.adjust = adjust
        self.extra_args = args
        self.extra_kwargs = kwargs

    def _fetch_data(self, *args, **kwargs):
        code_id_dict = _code_id_map_em()
        adjust_dict = {"qfq": "1", "hfq": "2", "": "0"}
        period_dict = {"daily": "101", "weekly": "102", "monthly": "103"}
        url = "http://push2his.eastmoney.com/api/qt/stock/kline/get"
        big_df = pd.DataFrame()
        if type(self.symbols) == str:
            self.symbols = [self.symbols]
        for symbol in self.symbols:
            params = {
                "fields1": "f1,f2,f3,f4,f5,f6",
                "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f116",
                "ut": "7eea3edcaed734bea9cbfc24409ed989",
                "klt": period_dict[self.period],
                "fqt": adjust_dict[self.adjust],
                "secid": f"{code_id_dict[symbol]}.{symbol}",
                "beg": self.start_date,
                "end": self.end_date,
                "_": "1623766962675",
            }
            timeout = self.extra_kwargs.get("timeout", None)
            proxies = self.extra_kwargs.get("proxies", None)
            r = httpx.get(url, params=params, timeout=timeout, proxies=proxies)
            data_json = r.json()
            if not (data_json["data"] and data_json["data"]["klines"]):
                return pd.DataFrame()
            temp_df = pd.DataFrame(
                [item.split(",") for item in data_json["data"]["klines"]]
            )
            big_df = pd.concat([big_df, temp_df], ignore_index=True)
        return big_df

    def _process_data(self, *args, **kwargs):
        fetched_data = self._fetch_data()
        fetched_data.columns = [
            "日期",
            "开盘",
            "收盘",
            "最高",
            "最低",
            "成交量",
            "成交额",
            "振幅",
            "涨跌幅",
            "涨跌额",
            "换手率",
        ]
        fetched_data.index = pd.to_datetime(fetched_data["日期"])
        fetched_data.reset_index(inplace=True, drop=True)
        fetched_data["开盘"] = pd.to_numeric(fetched_data["开盘"], errors="coerce")
        fetched_data["收盘"] = pd.to_numeric(fetched_data["收盘"], errors="coerce")
        fetched_data["最高"] = pd.to_numeric(fetched_data["最高"], errors="coerce")
        fetched_data["最低"] = pd.to_numeric(fetched_data["最低"], errors="coerce")
        fetched_data["成交量"] = pd.to_numeric(fetched_data["成交量"], errors="coerce")
        fetched_data["成交额"] = pd.to_numeric(fetched_data["成交额"], errors="coerce")
        fetched_data["振幅"] = pd.to_numeric(fetched_data["振幅"], errors="coerce")
        fetched_data["涨跌幅"] = pd.to_numeric(fetched_data["涨跌幅"], errors="coerce")
        fetched_data["涨跌额"] = pd.to_numeric(fetched_data["涨跌额"], errors="coerce")
        fetched_data["换手率"] = pd.to_numeric(fetched_data["换手率"], errors="coerce")
        return fetched_data

    def data(self) -> pd.DataFrame:
        """
        返回数据
        :return: pandas.DataFrame
        """
        return self._process_data(self)

    @property
    def columns(self) -> list:
        """
        返回数据
        :return: pandas.DataFrame
        """
        return ['日期', '开盘', '收盘', '最高', '最低', '成交量', '成交额', '振幅', '涨跌幅', '涨跌额', '换手率']

    def __str__(self):
        return "通过调用 .data() 方法返回数据；通过调用 .columns 属性返回数据的列名"

    def __call__(self, *args, **kwargs):
        self._process_data(self)


if __name__ == '__main__':
    stock_zh_a_hist = StockZhAHist
    proxies = {
        "http://": "http://127.0.0.1:7890",
        "https://": "http://127.0.0.1:7890",
    }
    stock_zh_a_hist_df = stock_zh_a_hist(
        symbols=["430090", "000001", "000002"],
        period="daily",
        start_date="20000516",
        end_date="20220722",
        adjust="hfq",
        timeout=2.111,
        proxies=proxies
    )
    print(stock_zh_a_hist_df.data())
    print(stock_zh_a_hist_df)
