

## ETL脚本说明

ETL脚本共分为4个文件夹，各文件夹下脚本含义如下：

1. 源数据处理

   - 处理原始的9G评论数据，从中提取出产品的相关信息，其中：

     - **ExtractProductID.cpp  ExtractProductID(java).java** 用于获取商品的asin

     - **ExtractInfo(Initial).py** 用于获取商品的评价，评分，时间等信息

     - **ExtractInfo(Film).cpp** 用于处理筛选后电影的评价，评分，时间等信息

       ​

2. 爬虫

   - 通过爬虫的手段抓取网页相关信息，其中

     - **自开线程式爬虫(伪多线程)**
       - 通过单线程请求抓取网页，如果访问被阻止，自动新建进程，更换请求头和ip来尝试访问

   - 通过爬虫抓取Amazon原始html网页，方便后面HTML处理

     ​

3. 处理HTML文件

   - 对获取到的HTML的文件进行处理，通过imdb等信息进行电影的筛选

     - **judge_film.py**：通过imdb等信息进行电影的筛选

   - 处理界面，提取电影关键信息

     - **process_page.py**:对从获取到的产品原始数据进行分别处理，提取出电影的版本、actor、director、binding、studio、starring、genre、title、date等字段信息

     ​

4. 数据库导入

   - mysql
     - ​
   - hive
   - neo4j
     - LoadtoNeo4j(movieinfo).py 
       - 建立电影关系表，根据和电影有关的一系列信息，新建actor、director、studio、starring等节点，并相应建立各自的关系信息
     - LoadtoNeo4j(cooperateInfo).py
       - 建立合作关系表，根据合作关系，新建actor、director、starring、genre等节点，并相应建立各自的关系信息，统计相互的合作次数以及导演风格。
   - influxdb

   ​