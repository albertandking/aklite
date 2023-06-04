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

AKLite will make the data fetch process more easy and fast. Now it focus on
stock data, and will support more data in the future.

Key Features
==============

* A super-fast request engine built in `HTTPX <https://www.python-httpx.org/>`_  and accelerated with `Asyncio <https://docs.python.org/3/library/asyncio.html>`_.
* The ability to fetch multiple stocks with ease.
* Access to historical data from main stream data source.

With AKLite, you'll have all the tools you need to fetch data. Start using AKLite today and
take your working to the next level!

A Quick Example
=================

Get a glimpse of what fetching with AKLite looks like with these code snippets:

**Fetching Stock Data**::

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

To learn how to use AKLite, see the notebooks under the *User Guide*:

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   notebooks/stock

`The notebooks above are also available on Github
<https://github.com/jindaxiang/aklite/tree/master/docs/notebooks>`_.

Recommended Reading
===================

The following is a list of essential books that provide background information
on quantitative finance and algorithmic trading:

* Lingjie Ma, `Quantitative Investing: From Theory to Industry <https://www.amazon.com/Quantitative-Investing-Industry-Lingjie-Ma/dp/3030472019/>`_

* Timothy Masters, `Testing and Tuning Market Trading Systems: Algorithms in C++ <https://www.amazon.com/Testing-Tuning-Market-Trading-Systems/dp/148424172X/>`_

* Stefan Jansen, `Machine Learning for Algorithmic Trading, 2nd Edition <https://www.amazon.com/Machine-Learning-Algorithmic-Trading-alternative/dp/1839217715/>`_

* Ernest P. Chan, `Machine Trading: Deploying Computer Algorithms to Conquer the Markets <https://www.amazon.com/Machine-Trading-Deploying-Computer-Algorithms-ebook/dp/B01N7NKVG0/>`_

* Perry J. Kaufman, `Trading Systems and Methods, 6th Edition <https://www.amazon.com/Trading-Systems-Methods-Wiley-ebook/dp/B08141BBXR/>`_

