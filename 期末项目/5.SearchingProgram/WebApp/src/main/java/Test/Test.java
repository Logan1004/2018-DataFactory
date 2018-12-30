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
import java.text.Format;
import java.util.*;

public class Test {

    public static void main(String [] args) throws Exception {
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
//        HiveService hiveService = new HiveService(ConnectToHive.getConnection());
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
//        ConnectToInfluxdb influxDB = new ConnectToInfluxdb();
//        influxDB.getInfluxDB();
//        String sql="SELECT max(\"sum_watchNum\") FROM (SELECT sum(\"watchNum\") AS \"sum_watchNum\" FROM \"mydb\".\"autogen\".\"test\" WHERE time >= '2000-01-01 00:00:00' AND time <='2012-12-31 23:59:59' AND \"genre\"=~ /Action/ group by time(30d))";
//        for(int i=0;i<10;i++){
//            long start = new java.util.Date().getTime();
//            QueryResult results = (QueryResult) influxDB.query(sql);
//            long end =  new java.util.Date().getTime();
//            System.out.println((end-start));
//            if(results.getResults() == null){
//                System.out.println("fail");
//                return;
//            }
//        }
//        Neo4jService neo4jService = new Neo4jService(ConnectToNeo4j.getConnection());
//
//        System.out.println("English"+" "+neo4jService.getMovieNumByLanguage("English"));
//        System.out.println("Spanish"+" "+neo4jService.getMovieNumByLanguage("Spanish"));
//        System.out.println("Chinese"+" "+neo4jService.getMovieNumByLanguage("Chinese"));
//        System.out.println("Arabic"+" "+neo4jService.getMovieNumByLanguage("Arabic"));
//        System.out.println("Portuguese"+" "+neo4jService.getMovieNumByLanguage("Portuguese"));
//        System.out.println("Japanese"+" "+neo4jService.getMovieNumByLanguage("Japanese"));
//        System.out.println("Russian"+" "+neo4jService.getMovieNumByLanguage("Russian"));
//        System.out.println("German"+" "+neo4jService.getMovieNumByLanguage("German"));
//        System.out.println("Italian"+" "+neo4jService.getMovieNumByLanguage("Italian"));
//        System.out.println("French"+" "+neo4jService.getMovieNumByLanguage("French"));
        MysqlService mysqlService = new MysqlService(ConnectToMysql.getConnection());


//        System.out.println(mysqlService.getMovieCountByYearAndMonth(2001, 2));

//        HashMap<String,Integer> hashMap = mysqlService.anyTime(2001,2003);
//        System.out.println(hashMap);
//        for (Map.Entry<String, Integer> entry : hashMap.entrySet()){
//            System.out.println("                                        <tr>\n" +
//                    "                                            <td>" + entry.getKey() + "</td>\n" +
//                    "                                            <td>" + entry.getValue() + "</td>\n" +
//                    "                                        </tr>");
//        }
//        for (int i=2000;i<=2008;i++){
//
//        }
//        HashMap<String,Integer> hashMap = mysqlService.anyFormat();
//        System.out.println(hashMap);
//        int count = 0;
//        for (Map.Entry<String, Integer> entry : hashMap.entrySet()){
//            if (entry.getKey().length() < 3 || entry.getKey().length() > 20){
//                continue;
//            }
//            if (count++ == 100){
//                break;
//            }
//            System.out.println("                                        <tr>\n" +
//                    "                                            <td>" + entry.getKey() + "</td>\n" +
//                    "                                            <td>" + entry.getValue() + "</td>\n" +
//                    "                                        </tr>");
//        }


//        Neo4jService neo4jService = new Neo4jService(ConnectToNeo4j.getConnection());
//        ArrayList<String> arrayList = (ArrayList<String>) mysqlService.getActors();
//        HashMap<String,String> hashMap = new HashMap<String, String>();
//        int count = 0;
//        for (int i=0;i<100;i++ ){
//            if (count>=50) break;
//            String s = arrayList.get(i);
//            int num1 = neo4jService.getStarMovieByActorName(arrayList.get(i).replace("\r",""));
//            int num2 = neo4jService.getSupportMovieByActorName(arrayList.get(i).replace("\r",""));
//            hashMap.put(s.replace("\r",""),num2+"(参演)/"+num1+"(主演)");
//          // System.out.println(s.replace("\r","")+" "+ neo4jService.getMovieByDirectorName(arrayList.get(i).replace("\r","")));
//            count++;
//        }
//
//        for (Map.Entry<String, String> entry : hashMap.entrySet()){
////            if (entry.getKey().length() < 3 || entry.getKey().length() > 20){
////                continue;
////            }
//            System.out.println("                                        <tr>\n" +
//                    "                                            <td>" + entry.getKey() + "</td>\n" +
//                    "                                            <td>" + entry.getValue() + "</td>\n" +
//                    "                                        </tr>");
//        }
        ConnectToInfluxdb influxdb=new ConnectToInfluxdb();
        ConnectToInfluxdb.getInfluxDB();
        Scanner sc=new Scanner(System.in);
        String starttime="2002-01-01 00:00:00";
        String endtime="2012-01-01 00:00:00";
        String grouptime="30d";




        HashMap<String,Integer> hashMap = new HashMap<String, Integer>();
        ArrayList<String> arrayList = mysqlService.getAllGenre();
        for (int i=0;i<arrayList.size();i++){
            hashMap.put(arrayList.get(i),mysqlService.getMoviesByGenre(arrayList.get(i)+"\r"));
        }
        for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
            String genre=entry.getKey();
            System.out.print(genre+"\t");
            QueryResult results=influxdb.getWatchNumTop(genre,grouptime,starttime,endtime);

            if(results==null){

            }
            else{
                for(QueryResult.Result result : results.getResults()){
                    List<QueryResult.Series> series = result.getSeries();
                    if(series!=null){
                    for(QueryResult.Series serie : series) {
                        List<List<Object>> values = serie.getValues();//字段字集he
                        double max = 0.0;
                        for (List<Object> n : values) {
                            String temp=n.get(0).toString();
                            temp=temp.substring(5,7);
                            System.out.println(temp);
                        }
                    }}
                }
        }
//        Neo4jService neo4jService = new Neo4jService(ConnectToNeo4j.getConnection());
//        System.out.println(neo4jService.getCooperate());


//
//        ConnectToInfluxdb influxdb=new ConnectToInfluxdb();
//        ConnectToInfluxdb.getInfluxDB();
//        Scanner sc=new Scanner(System.in);
//        String starttime;
//        String endtime;
//        String grouptime;
//        String genre;
//        System.out.println("genre:");
//        genre= sc.nextLine();
//        System.out.println("grouptime");
//        grouptime=sc.nextLine();
//        System.out.println("starttime");
//        starttime=sc.nextLine();
//        System.out.println("endtime");
//        endtime=sc.nextLine();
//        QueryResult results=influxdb.getWatchNumTop(genre,grouptime,starttime,endtime);
//        results.getResults();
//        for(QueryResult.Result result : results.getResults()){
//            List<QueryResult.Series> series = result.getSeries();
//            for(QueryResult.Series serie : series) {
//                List<List<Object>> values = serie.getValues();//字段字集合
//                List<String> colums = serie.getColumns();//字段名
//                System.out.println("colums:" + colums);
//                for (List<Object> n : values) {
//                    System.out.println(n);
//                }
//            }}



    }}
}
