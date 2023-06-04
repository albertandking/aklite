.. meta::
   :title: AKLite
   :description: AKLite is a lite version of AKShare
   :google-site-verification: XJpTXQaAdlEb2eAbndHa2ZmaUiOixSMaRusk-kKVKOQ

.. title:: AKLite is a lite version of AKShare

================
AKLite
================

.. raw:: html

   <section class="shields">
      <a href="https://www.python.org/">
         <img src="https://img.shields.io/badge/python-v3-brightgreen.svg"
            alt="python">
      </a>
      <a href="https://github.com/jindaxiang/aklite/">
         <img src="https://img.shields.io/github/stars/jindaxiang/aklite?style=social" alt="Github stars">
      </a>
   </section>


AKLite is a lite version of AKShare
=======================================

Are you looking to enhance your trading strategies with the power of Python and
machine learning? Then you need to check out **PyBroker**! This Python framework
is designed for developing algorithmic trading strategies, with a focus on
strategies that use machine learning. With PyBroker, you can easily create and
fine-tune trading rules, build powerful models, and gain valuable insights into
your strategy's performance.

Key Features
============

* A super-fast backtesting engine built in `NumPy <https://numpy.org/>`_  and accelerated with `Numba <https://numba.pydata.org/>`_.
* The ability to create and execute trading rules and models across multiple instruments with ease.
* Access to historical data from `Alpaca <https://alpaca.markets/>`_, `Yahoo Finance <https://finance.yahoo.com/>`_, `AKShare <https://github.com/akfamily/akshare>`_, or from `your own data provider <https://www.pybroker.com/en/latest/notebooks/7.%20Creating%20a%20Custom%20Data%20Source.html>`_.
* The option to train and backtest models using `Walkforward Analysis <https://www.pybroker.com/en/latest/notebooks/6.%20Training%20a%20Model.html#Walkforward-Analysis>`_, which simulates how the strategy would perform during actual trading.
* More reliable trading metrics that use randomized `bootstrapping <https://en.wikipedia.org/wiki/Bootstrapping_(statistics)>`_ to provide more accurate results.
* Caching of downloaded data, indicators, and models to speed up your development process.
* Parallelized computations that enable faster performance.

With PyBroker, you'll have all the tools you need to create winning trading
strategies backed by data and machine learning. Start using PyBroker today and
take your trading to the next level!

A Quick Example
===============

Get a glimpse of what backtesting with PyBroker looks like with these code
snippets:

**Rule-based Strategy**::

   from pybroker import Strategy, YFinance, highest

   def exec_fn(ctx):
      # Get the rolling 10 day high.
      high_10d = ctx.indicator('high_10d')
      # Buy on a new 10 day high.
      if not ctx.long_pos() and high_10d[-1] > high_10d[-2]:
         ctx.buy_shares = 100
         # Hold the position for 5 days.
         ctx.hold_bars = 5
         # Set a stop loss of 2%.
         ctx.stop_loss_pct = 2

   strategy = Strategy(YFinance(), start_date='1/1/2022', end_date='7/1/2022')
   strategy.add_execution(
      exec_fn, ['AAPL', 'MSFT'], indicators=highest('high_10d', 'close', period=10))
   # Run the backtest after 20 days have passed.
   result = strategy.backtest(warmup=20)

**Model-based Strategy**::

   import pybroker
   from pybroker import Alpaca, Strategy

   def train_fn(train_data, test_data, ticker):
      # Train the model using indicators stored in train_data.
      ...
      return trained_model

   # Register the model and its training function with PyBroker.
   my_model = pybroker.model('my_model', train_fn, indicators=[...])

   def exec_fn(ctx):
      preds = ctx.preds('my_model')
      # Open a long position given my_model's latest prediction.
      if not ctx.long_pos() and preds[-1] > buy_threshold:
         ctx.buy_shares = 100
      # Close the long position given my_model's latest prediction.
      elif ctx.long_pos() and preds[-1] < sell_threshold:
         ctx.sell_all_shares()

   alpaca = Alpaca(api_key=..., api_secret=...)
   strategy = Strategy(alpaca, start_date='1/1/2022', end_date='7/1/2022')
   strategy.add_execution(exec_fn, ['AAPL', 'MSFT'], models=my_model)
   # Run Walkforward Analysis on 1 minute data using 5 windows with 50/50 train/test data.
   result = strategy.walkforward(timeframe='1m', windows=5, train_size=0.5)

To learn how to use AKLite, see the notebooks under the *User Guide*:

.. toctree::
   :maxdepth: 1
   :caption: User Guide

   notebooks/stock

`The notebooks above are also available on Github
<https://github.com/jindaxiang/aklite/tree/master/docs/notebooks>`_.


   Index <genindex>

Recommended Reading
===================

The following is a list of essential books that provide background information
on quantitative finance and algorithmic trading:

* Lingjie Ma, `Quantitative Investing: From Theory to Industry <https://www.amazon.com/Quantitative-Investing-Industry-Lingjie-Ma/dp/3030472019/>`_

* Timothy Masters, `Testing and Tuning Market Trading Systems: Algorithms in C++ <https://www.amazon.com/Testing-Tuning-Market-Trading-Systems/dp/148424172X/>`_

* Stefan Jansen, `Machine Learning for Algorithmic Trading, 2nd Edition <https://www.amazon.com/Machine-Learning-Algorithmic-Trading-alternative/dp/1839217715/>`_

* Ernest P. Chan, `Machine Trading: Deploying Computer Algorithms to Conquer the Markets <https://www.amazon.com/Machine-Trading-Deploying-Computer-Algorithms-ebook/dp/B01N7NKVG0/>`_

* Perry J. Kaufman, `Trading Systems and Methods, 6th Edition <https://www.amazon.com/Trading-Systems-Methods-Wiley-ebook/dp/B08141BBXR/>`_

