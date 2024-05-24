Crawler Strategy
==============================================================================
这个文档描述了我们爬虫的策略.

1. 到 https://www.unitedstateszipcodes.org/zip-code-database/ 下载免费版的数据库的 CSV 文件. 里面有所有的 Zipcode 的列表以及一些基本的 lat lng 信息. 这里的重点是 zipcode 的列表. 有了 zipcode 就可以用 ``https://www.unitedstateszipcodes.org/{zipcode}/`` 来构建 zipcode 详细信息页面的 URL 了.
2. 选择一个数据库系统, 为每个 zipcode 创建一条数据用于追踪爬虫抓取的状态. 我倾向于使用 Amazon DynamoDB + `Status Tracking <https://pynamodb-mate.readthedocs.io/en/latest/06-Status-Tracker/index.html>`_ 功能. DynamoDB 是 Serverless 的, 无需管理运维, 并且用多少读写流量就付多少钱, 对于我们这个应用来说流量根本不值一提. 而 Status Tracking 可以帮助我们确保每个 zipcode 都被抓取到.
3. 我们的爬虫会先从数据库中拿出来所有没有被爬取的 zipcode, 然后依次爬取. 这个爬取的目标是网页的 HTML 文件, 只要我们拿到了 HTML 数据, 我们之后可以慢慢的优化我们的 Parser, 从 HTML 中提取我们需要的数据, 后这个后续的提取数据就可以离线进行了.
4. 这个网站的 HTML 中会把所有的数据放在 ``<script>`` 标签下用 JavaScript 的数据格式写下来, 然后网站的 UI 会将数据 render 成一个个的图表. 举例 ``var data = [{"key":"Data","values":[{"x":2005,"y":5049},{"x":2006,"y":5299},{"x":2007,"y":5401},{"x":2008,"y":5591},{"x":2009,"y":5780},{"x":2010,"y":6039},{"x":2011,"y":6338},{"x":2012,"y":6050},{"x":2013,"y":5850},{"x":2014,"y":6050},{"x":2015,"y":6300},{"x":2016,"y":6040},{"x":2017,"y":6250},{"x":2018,"y":6320},{"x":2019,"y":6130},{"x":2020,"y":5840}]}];`` 这个就是 UI 里面每年的人口变化底层的数据. 总的来说, 只要把 HTML 抓下来, 后面的数据提取就是一个离线的工作了, 可以慢慢做.
