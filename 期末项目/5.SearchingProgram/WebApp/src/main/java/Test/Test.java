package Test;

import Connections.ConnectToHive;
import Connections.ConnectToInfluxdb;
import Connections.ConnectToMysql;
import Connections.ConnectToNeo4j;
import Service.CombinedService;
import Service.HiveService;
import Service.MysqlService;
import Service.Neo4jService;
import org.influxdb.InfluxDB;
import org.influxdb.dto.QueryResult;

import java.sql.*;

public class Test {

    public static void main(String [] args) throws ClassNotFoundException, SQLException {
        // 连接mysql
//        Connection connection = ConnectToMysql.getConnection();
//        PreparedStatement preparedStatement = connection.prepareStatement("select  count(1) from director");
//        ResultSet resultSet = preparedStatement.executeQuery();
//        while (resultSet.next()){
//            System.out.println(resultSet.getInt(1));
//        }
//        resultSet.close();
//        preparedStatement.close();
//        connection.close();
        // 连接hive
//        Connection connection = ConnectToHive.getConnection();
//        PreparedStatement preparedStatement = connection.prepareStatement("select * from test");
//        ResultSet resultSet = preparedStatement.executeQuery();
//        while (resultSet.next()){
//            System.out.println(resultSet.getString(1));
//        }
//        resultSet.close();
//        preparedStatement.close();
//        connection.close();
        // 连接neo4j
//        Connection connection = ConnectToNeo4j.getConnection();
//        PreparedStatement preparedStatement = connection.prepareStatement("MATCH (a)-[b]-(c) return a,b,c limit 100");
//        ResultSet resultSet = preparedStatement.executeQuery();
//        while (resultSet.next()){
//            System.out.println(resultSet.getString(1) + "-" + resultSet.getString(2) + "-" + resultSet.getString(3));
//        }
        // 连接influxdb
//        InfluxDB influxDB = ConnectToInfluxdb.getInfluxDB();
//        System.out.println(HiveService.TimeToTimestamp(2011, 1, 1, 1, 1, 1));
        HiveService hiveService = new HiveService(ConnectToHive.getConnection());
//        System.out.println(hiveService.getMovieCountBeforeTime(2011, 1, 1, 1, 1, 1));
//        System.out.println(hiveService.getMovieCountByYear(2011));
//        System.out.println(hiveService.getMovieCountByYearAndMonth(2011, 1));
//        System.out.println(hiveService.getMovieCountByYearAndMonth(2011, 2));
//        System.out.println(hiveService.getMovieCountByYearAndMonth(2011, 3));
//        System.out.println(hiveService.getMovieCountByYearAndQuarter(2011, 1));
//        System.out.println(hiveService.getMovieCountByDate(2011, 1,1));
//        Neo4jService neo4jService = new Neo4jService(ConnectToNeo4j.getConnection());
//        MysqlService mysqlService = new MysqlService(ConnectToMysql.getConnection());
//        for (int i=0;i<12;i++){
//            System.out.println(neo4jService.getCooperated("Nicole Kidman","Ed Harris"));
//        }
//
//        System.out.println(neo4jService.getMovieByDirectorName("Oliver Stone"));
//        System.out.println(neo4jService.getMovieVersion(".*Carmen.*"));
//        System.out.println(neo4jService.getStarMovieByActorName("Greg Finley"));
//        System.out.println(neo4jService.getSupportMovieByActorName("Greg Finley"));
//        System.out.println(neo4jService.getMovieByGenre("Action"));
//        System.out.println(neo4jService.getCooperatedMovieAD("Nicole Kidman","Robert Benton"));
//        System.out.println(neo4jService.getCooperatedMovieAA("Nicole Kidman","Ed Harris"));
//        System.out.println(neo4jService.getCooperated("Nicole Kidman","Ed Harris"));
//        CombinedService combinedService = new CombinedService(hiveService, neo4jService,mysqlService);
//        System.out.println(combinedService.maxCoorWithDirectors("Nicole Kidman", mysqlService.getDirectors()));
        ConnectToInfluxdb influxDB = new ConnectToInfluxdb();
        influxDB.getInfluxDB();
        String sql="SELECT max(\"sum_watchNum\") FROM (SELECT sum(\"watchNum\") AS \"sum_watchNum\" FROM \"mydb\".\"autogen\".\"test\" WHERE time >= '2000-01-01 00:00:00' AND time <='2012-12-31 23:59:59' AND \"genre\"=~ /Action/ group by time(30d))";
        for(int i=0;i<10;i++){
            long start = new java.util.Date().getTime();
            QueryResult results = (QueryResult) influxDB.query(sql);
            long end =  new java.util.Date().getTime();
            System.out.println((end-start));
            if(results.getResults() == null){
                System.out.println("fail");
                return;
            }
        }


    }
}
