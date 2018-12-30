package Service;

import Connections.ConnectToNeo4j;

import java.io.IOException;
import java.sql.*;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

public class Neo4jService {
    private Connection connection = null;

    public Neo4jService(Connection connection) {
        this.connection = connection;
    }

    public Connection getConnection() {
        return connection;
    }

    public void setConnection(Connection connection) {
        this.connection = connection;
    }

    public int timeConsuming(PreparedStatement preparedStatement){
        int count=0;
        try {
            Long d1 = new Date().getTime();
            ResultSet resultSet = preparedStatement.executeQuery();
            Long d2 = new Date().getTime();
            if (resultSet.next()) {
                count = resultSet.getInt(1);
            }
            //System.out.println(d2 - d1 + "ms");
            resultSet.close();
        }catch (SQLException e){
            e.printStackTrace();
        }
        return count;
    }


    /**
     * 输入电影名字，返回电影的版本数
     * @param name 电影名字
     * @return 电影版本数量
     */
    public Integer getMovieVersion(String name){
        String sql = "Match (n:Movie) where n.name =~ {1} return count(n)";
        PreparedStatement preparedStatement = null;
        int count = 0;
        try {
            preparedStatement = connection.prepareStatement(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        try {
            preparedStatement.setString(1, name);
            count=timeConsuming(preparedStatement);
            preparedStatement.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return count;
    }


    /**
     * 输入导演名字，返回导演指导过的电影数目
     * @param name 导演名字
     * @return 电影数量
     */
    public Integer getMovieByDirectorName(String name){
        String sql = "Match (n:Director)-[]-(m:Movie) where n.name={1} return count(m)";
        PreparedStatement preparedStatement = null;
        int count = 0;
        try {
            preparedStatement = connection.prepareStatement(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        try {
            preparedStatement.setString(1, name);
            count = timeConsuming(preparedStatement);
            preparedStatement.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return count;
    }

    /**
     * 输入演员名字，返回演员主演电影数目
     * @param name 演员名字
     * @return 电影数量
     */
    public Integer getStarMovieByActorName(String name){
        String sql = "Match (n:Starring)-[]-(m:Movie) where n.name={1} return count(m)";
        PreparedStatement preparedStatement = null;
        int count = 0;
        try {
            preparedStatement = connection.prepareStatement(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        try {
            preparedStatement.setString(1,name);
            count = timeConsuming(preparedStatement);
            preparedStatement.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return count;
    }

    /**
     * 输入演员名字，返回演员参演电影数目
     * @param name 演员名字
     * @return 电影数量
     */
    public Integer getSupportMovieByActorName(String name){
        String sql = "Match (n:Actor)-[]-(m:Movie) where n.name={1} return count(m)";
        PreparedStatement preparedStatement = null;
        int count = 0;
        try {
            preparedStatement = connection.prepareStatement(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        try {
            preparedStatement.setString(1,name);
            count = timeConsuming(preparedStatement);
            preparedStatement.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return count;
    }

    /**
     * 输入电影类型，返回该类型的电影数目
     * @param name 电影类型
     * @return 电影数量
     */
    public Integer getMovieByGenre(String name){
        String sql = "Match (n:Movie)-[]-(m:Genre) where m.name={1} return count(n)";
        PreparedStatement preparedStatement = null;
        int count = 0;
        try {
            preparedStatement = connection.prepareStatement(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        try {
            preparedStatement.setString(1,name);
            count = timeConsuming(preparedStatement);
            preparedStatement.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return count;
    }

    /**
     * 输入演员名字导演名字，返回合作数目
     * @param nameActor 演员名字 nameDirector 导演名字
     * @return 合作数量
     */
    public Integer getCooperatedMovieAD(String nameActor, String nameDirector){
        String sql = "Match (n:Actor)-[]-(t:Movie)-[]-(m:Director) where n.name={1} and m.name = {2} return count(t)";
        PreparedStatement preparedStatement = null;
        int count = 0;
        try {
            preparedStatement = connection.prepareStatement(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        try {
            preparedStatement.setString(1,nameActor);
            preparedStatement.setString(2,nameDirector);
            count = timeConsuming(preparedStatement);
            preparedStatement.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return count;
    }

    /**
     * 输入演员和演员名字，返回合作数目
     * @param nameActor1 演员名字 nameActor 演员名字2
     * @return 合作数量
     */
    public Integer getCooperatedMovieAA(String nameActor1, String nameActor2){
        String sql = "Match (n:Actor)-[]-(t:Movie)-[]-(m:Actor) where n.name={1} and m.name = {2} return count(t)";
        PreparedStatement preparedStatement = null;
        int count = 0;
        try {
            preparedStatement = connection.prepareStatement(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        try {
            preparedStatement.setString(1,nameActor1);
            preparedStatement.setString(2,nameActor2);
            count = timeConsuming(preparedStatement);
            preparedStatement.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return count;
    }

    /**
     * 输入演员和演员名字，返回合作数目
     * @param nameActor1 演员名字 nameActor 演员名字2
     * @return 合作数量
     */
    public Integer getCooperated(String nameActor1, String nameActor2){
        String sql = "Match (n:Actor)-[t]-(m:Actor) where n.name={1} and m.name = {2} return count(t)";
        PreparedStatement preparedStatement = null;
        int count = 0;
        try {
            preparedStatement = connection.prepareStatement(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        try {
            preparedStatement.setString(1,nameActor1);
            preparedStatement.setString(2,nameActor2);
            count = timeConsuming(preparedStatement);
            preparedStatement.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return count;
    }

    /**
     * 输入语言 返回电影数目
     * @param language 语言
     * @return 电影数目
     */
    public Integer getMovieNumByLanguage(String language){
        String sql = "MATCH (n:Language)-[]-(m:Movie) where n.name = {1} return count(m)";
        PreparedStatement preparedStatement = null;
        int count = 0;
        try {
            preparedStatement = connection.prepareStatement(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        try {
            preparedStatement.setString(1,language);
            count = timeConsuming(preparedStatement);
            preparedStatement.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return count;
    }
//    Match (n:Director)-[t]-(m:Actor) where t.times > 3 return n,t.times,m limit 100
    public ArrayList<String> getCooperate() {
        ArrayList<String> arrayList = new ArrayList<String>();
        String sql = "Match (n:Director)-[t]-(m:Actor) where t.times > 3 return n,t.times,m limit 100";
        PreparedStatement preparedStatement = null;

        try {
            preparedStatement = connection.prepareStatement(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        try {
            ResultSet resultSet = preparedStatement.executeQuery();

            while (resultSet.next()) {
                String director = resultSet.getString(1).replace("\r","");
                String actor = resultSet.getString(3).replace("\r","");
                int count = resultSet.getInt(2);
                arrayList.add(director + "/" + count + "/" + actor);
            }
            //System.out.println(d2 - d1 + "ms");
            resultSet.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return arrayList;
    }





}
