# 数据库查询说明

项目功能需求说明：

1. 按照时间进行查询及统计
2. 按照电影名称进行查询及统计
3. 按照导演进行查询及统计
4. 按照演员进行查询及统计
5. 按照电影类别进行查询及统计
6. 按照导演-演员的合作关系，或者演员-演员的合作关系进行查询
7. 按照电影上映时间进行查询及统计



数据库查询共分为5个文件夹，各文件夹下代码含义分别如下：

1. mysql：

- **ConnectToMysql.java**：获取mysql数据库的连接会话
- **MysqlService.java**: 集成mysql查询功能，完成功能点：1，2，3，4，5，6

2. hive：

- **ConnectToHive.java**：获取hive数据库的连接会话
- **HiveService.java**：集成hive查询功能，完成功能点：1，2，3，4

3. neo4j：

- **ConnectToNeo4j.java**：获取Neo4j数据库的连接会话
- **Neo4jService.java**：集成neo4J查询功能，完成功能点：2，3，4，5，6

4. influxdb：

- **ConnectToInfluxdb.java**：获取influxdb，集成indluxdb查询功能，完成功能点：1，5，7

5. combined：

- **CombinedService.java**：混合查询，完成功能点​



