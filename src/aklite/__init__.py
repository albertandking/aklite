"""
0.0.1 init project
0.0.2 add stock_zh_a_hist interface
0.0.3 add httpx package
"""

__version__ = "0.0.3"
__author__ = "AKFamily"

__slot__ = ["__version__", "__author__", "stock_zh_a_hist"]

from aklite.stock.stock_hist_em import StockZhAHist

stock_zh_a_hist = StockZhAHist
