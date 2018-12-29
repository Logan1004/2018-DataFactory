package Service;

import java.sql.*;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class MysqlService {

    private Connection connection = null;

    public MysqlService(Connection connection) {
        this.connection = connection;
    }

    public Connection getConnection() {
        return connection;
    }

    public void setConnection(Connection connection) {
        this.connection = connection;
    }

    /**
     * 输入起止日期，获取该日期内的电影数量
     * @param start 查询起始时间
     * @param end 查询截止时间
     * @return 电影数量
     */
    private Integer getMovieBetweenStartAndEnd(Long start, Long end){
        String sql = "select count(1) from movie where date_<? and date_>?";
        PreparedStatement preparedStatement = null;
        int count = 0;
        try {
            preparedStatement = connection.prepareStatement(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        try {
            preparedStatement.setLong(1, end);
            preparedStatement.setLong(2, start);
            Long d1 = new Date().getTime();
            ResultSet resultSet = preparedStatement.executeQuery();
            Long d2 = new Date().getTime();
            if (resultSet.next()){
                count = resultSet.getInt(1);
            }
            System.out.println(d2 - d1 + "ms");
            resultSet.close();
            preparedStatement.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return count;
    }

    /**
     * 输入年月日时分秒，获取早于该时间的电影数量
     * @param y 年
     * @param m 月
     * @param d 日
     * @param h 时
     * @param M 分
     * @param s 秒
     * @return 电影数量
     */
    public Integer getMovieCountBeforeTime(int y, int m, int d, int h, int M, int s) {
        Long time = TimeToTimestamp(y,m,d,h,M,s);
        Long start = Long.valueOf(0);
        return getMovieBetweenStartAndEnd(start, time);
    }

    /**
     * 输入年份，获取该年度的电影数量
     * @param y 年份
     * @return 电影数量
     */
    public Integer getMovieCountByYear(int y) {
        Long end = TimeToTimestamp(y,12,30,23,59,59);
        Long start = TimeToTimestamp(y, 1,1,0,0,0);
        return getMovieBetweenStartAndEnd(start, end);
    }

    /**
     * 输入年份和月份，获取该月份的电影数量
     * @param y 年份
     * @param m 月份
     * @return 电影数量
     */
    public Integer getMovieCountByYearAndMonth(int y, int m) {
        Long end = TimeToTimestamp(y, m+1, 1, 0, 0, 0);
        Long start = TimeToTimestamp(y, m, 1, 0, 0, 0);
        return getMovieBetweenStartAndEnd(start, end);
    }

    /**
     * 输入年份和季度，获取该季度的电影数量
     * @param y 年份
     * @param q 月份
     * @return 电影数量
     */
    public Integer getMovieCountByYearAndQuarter(int y, int q){
        if (q < 1 || q > 4) { q = 1; }
        Long end = TimeToTimestamp(y, q*3, 30, 23, 59, 59);
        Long start = TimeToTimestamp(y, q*3-2, 1, 0, 0, 0);
        return getMovieBetweenStartAndEnd(start, end);
    }

    /**
     * 输入年月日，获取该日新增的电影数量
     * @param y 年
     * @param m 月
     * @param d 日
     * @return 电影数量
     */
    public Integer getMovieCountByDate(int y, int m, int d){
        Long end = TimeToTimestamp(y, m, d, 23, 59, 59);
        Long start = TimeToTimestamp(y, m, d, 0, 0,0);
        return getMovieBetweenStartAndEnd(start, end);
    }

    /**
     * 输入年月日时分秒，转换为时间戳值
     * @param y 年
     * @param m 月
     * @param d 日
     * @param h 时
     * @param M 分
     * @param s 秒
     * @return 电影数量
     */
    public static Long TimeToTimestamp(int y, int m, int d, int h, int M, int s){
        if (m > 12 || m < 1) { m = 1;}
        if (d > 30 || d < 1) { d = 1;}
        if (h > 24 || h < 1) { h = 1;}
        if (M > 60 || M < 0) { M = 0;}
        if (s > 60 || s < 0) { s = 0;}
        String time = y + "-" + m + "-" + d + " " + h + ":" + M + ":" + s;
        return StringToTimestamp(time);
    }

    /**
     * 输入通过形如yyyy-mm-dd hh:mm:ss的时间字符串，返回时间戳值
     * @param date 时间字符串
     * @return 时间戳值
     */
    private static Long StringToTimestamp(String date){
        Timestamp timestamp = null;
        timestamp = Timestamp.valueOf(date);
//        System.out.println(timestamp);
        Date d = timestamp;
//        System.out.println(d.getTime());
        return (d.getTime()/1000);
    }

    /**
     * 通过名称和sql，去除重复代码
     * @param name preparedStatement所set的值
     * @param sql sql语句
     * @return
     */
    public Integer getCountsByName(String name, String sql){
        int count = 0;
        try {
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, name);
            Long d1 = new Date().getTime();
            ResultSet resultSet = preparedStatement.executeQuery();
            Long d2 = new Date().getTime();
            if (resultSet.next()){
                count = resultSet.getInt(1);
            }
            System.out.println(d2 - d1 + "ms");
            resultSet.close();
            preparedStatement.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return count;
    }

    /**
     * 输入电影名称，输出该电影的版本数量
     * @param name 电影名字
     * @return 版本数量
     */
    public Integer getFormatsByMovieName(String name){
        name = "%" + name + "%";
        String sql = "select count(1) from movie, movie_has_format where movie.name like ? and movie_has_format.movie_id=movie.id";
        return getCountsByName(name, sql);
    }

    /**
     * 输入导演名称，输出该导演执导的电影数量
     * @param name 导演名称
     * @return 电影数量
     */
    public Integer getMoviesByDirector(String name){
        name = "%" + name + "%";
        String sql = "select count(1) from director, director_direct_movie where director.name like ? and director.id = director_direct_movie.director_id";
        return getCountsByName(name, sql);
    }

    /**
     * 输入类型名称，输出该类型的电影数量
     * @param name 类型名称
     * @return 电影数量
     */
    public Integer getMoviesByGenre(String name){
        String sql = "select count(1) as sum from genre inner join movie_has_genre g on genre.id = g.genre_id where type like ?";
        return getCountsByName(name, sql);
    }

    /**
     * 输入演员名称，输出该演员参演的电影数量
     * @param name 演员名称
     * @return 电影数量
     */
    public Integer getMoviesByActor(String name){
        name = "%" + name + "%";
        String sql = "select count(1) from actor, actor_act_movie where actor.name like ? and actor_act_movie.actor_id = actor.id";
        return getCountsByName(name, sql);
    }

    /**
     * 输入演员名称，输出该演员主演的电影数量
     * @param name 演员名称
     * @return 电影数量
     */
    public Integer getMovieByStarring(String name){
        name = "%" + name + "%";
        String sql = "select count(1) from star_starring_movie, actor where actor.name like ? and star_starring_movie.actor_id = actor.id";
        return getCountsByName(name, sql);
    }

    /**
     * 返回所有的演员姓名列表
     * @return 演员姓名列表
     * @throws SQLException
     */
    public List<String> getActors() throws SQLException {
        String sql = "select actor.name from actor";
        PreparedStatement preparedStatement = connection.prepareStatement(sql);
        ResultSet resultSet = preparedStatement.executeQuery();
        ArrayList<String> actors = new ArrayList<String>();
        while (resultSet.next()){
            actors.add(resultSet.getString(1));
        }
        resultSet.close();
        preparedStatement.close();
        return actors;
    }

    /**
     * 返回所有的导演姓名列表
     * @return 导演姓名列表
     * @throws SQLException
     */
    public List<String> getDirectors() throws SQLException {
        String sql = "select director.name from director";
        PreparedStatement preparedStatement = connection.prepareStatement(sql);
        ResultSet resultSet = preparedStatement.executeQuery();
        ArrayList<String> directors = new ArrayList<String>();
        while (resultSet.next()){
            directors.add(resultSet.getString(1));
        }
        resultSet.close();
        preparedStatement.close();
        return directors;
    }


}
