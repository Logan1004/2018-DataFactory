package top.guitoubing;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.*;
import java.sql.*;
import java.util.ArrayList;
import java.util.Objects;

/**
 * 思路：
 * 当获取到一个MovieData信息时，即电影、导演和演员
 * 三者应该有以下关系：
 *      执导：导演->电影   关系应包含属性：次数
 *      参演：演员->电影   关系应包含属性：次数
 *      合作(双向关系)：导演<->演员    关系应包含属性：次数
 * 每次添加三者时，询问数据库中是否有该导演、电影和演员，若没有则创建
 * 而后为三者建立如上关系
 */

public class Main {

//    private static String folderPath = "D:\\datawarehouse\\";
    private static String folderPath = "/Users/tanrui/Desktop/1/";

    /**
     *
     */
    static class MovieData{
        private String title;
        private String director;
        private ArrayList<String> actors;

        public MovieData() {
            title = "";
            director = "";
            actors = new ArrayList<String>();
        }

        public MovieData(String title, String director, ArrayList<String> actors) {
            this.title = title;
            this.director = director;
            this.actors = actors;
        }

        public String getTitle() {
            return title;
        }

        public void setTitle(String title) {
            this.title = title;
        }

        public String getDirector() {
            return director;
        }

        public void setDirector(String director) {
            this.director = director;
        }

        public ArrayList<String> getActors() {
            return actors;
        }

        public void setActors(ArrayList<String> actors) {
            this.actors = actors;
        }

        public boolean addActors(String actor){
            if (actor.equals("")){
                return false;
            }else {
                actors.add(actor);
                return true;
            }
        }

        @Override
        public String toString() {
            StringBuilder data = new StringBuilder();
            data.append("Title : ").append(title).append("\n")
                    .append("Director : ").append(director).append("\n")
                    .append("Actors : ");
            for (String actor : actors){
                data.append(actor).append("、");
            }
            data.replace(data.length()-1, data.length(), "\n");
            return data.toString();
        }
    }

    public static void main(String[] args) throws SQLException, IOException {
        // 连接到neo4j
        Connection con = ConnectToNeo4j();

        File folder = new File(folderPath + "data_1.txt");

        File out = new File(folderPath + "out.txt");
        FileWriter fileWriter = new FileWriter(out);

        int count = 0;

        if (folder.exists()){
            for (File file : Objects.requireNonNull(folder.listFiles())){
                // 解析文件
                Document doc = Jsoup.parse(ParseFile(file));
                MovieData data = ParseDoc(doc);

                if (data == null){
                    count++;
//                    System.out.println("Null");
                }else {
//                    System.out.println(data);
//                    fileWriter.write(data.toString());
                    Query(con, data);
                }
            }
        }
        System.out.print(count);

        fileWriter.close();


//        // 获取文件
//        File file = new File("/Users/tanrui/Desktop/1/0001517791.html");
//        // 解析文件
//        Document doc = Jsoup.parse(ParseFile(file));
//        MovieData data = ParseDoc(doc);
//
//        if (data == null){
//            System.out.println("Null");
//        }else {
//            System.out.println(data);
//        }

        // 执行query
//        Statement stmt = con.createStatement();
//        ResultSet rs = stmt.executeQuery("MATCH (n:D1) RETURN n");
//        while (rs.next()) {
//            System.out.println(rs.getString(1));
//        }
    }

    /**
     *
     * @return 返回neo4j数据库连接
     * @throws SQLException 抛出连接异常
     */
    public static Connection ConnectToNeo4j() throws SQLException {
        return DriverManager.getConnection("jdbc:neo4j://localhost:7474","neo4j","tanrui");
    }


    /**
     *
     * @param connection 数据库连接
     * @param data 数据对象
     * @throws SQLException
     */
    public static void Query(Connection connection, MovieData data) throws SQLException {

        String query;
        PreparedStatement preparedStatement;
        ResultSet resultSet;
        int times;

        boolean flagDir, flagAct, flagRel;

        // 第一步：查询导演节点是否存在
        query = "MATCH (n:Director) WHERE n.name={1} RETURN n";
        preparedStatement = connection.prepareStatement(query);
        preparedStatement.setString(1, data.getDirector());
        resultSet = preparedStatement.getResultSet();
        // 未找到该导演,创建一个节点
        if (resultSet == null){
            query = "CREATE (:Director{name:{1}})";
            preparedStatement = connection.prepareStatement(query);
            preparedStatement.setString(1, data.getDirector());
            preparedStatement.executeUpdate();
        }

        /**
         * 为节省空间，节点中不再存储电影
         */
//        // 第二步：查询电影节点是否存在
//        query = "MATCH (n:Movie) WHERE n.name={1} RETURN n";
//        preparedStatement = connection.prepareStatement(query);
//        preparedStatement.setString(1, data.getTitle());
//        resultSet = preparedStatement.getResultSet();
//        // 未找到该电影,创建一个节点
//        if (resultSet == null){
//            query = "CREATE (:Movie{name:{1}})";
//            preparedStatement = connection.prepareStatement(query);
//            preparedStatement.setString(1, data.getTitle());
//            preparedStatement.executeUpdate();
//        }

        // 第三步：查询演员节点是否存在
        for (String actor : data.getActors()){
            query = "MATCH (n:Actor) WHERE n.name={1} RETURN n";
            preparedStatement = connection.prepareStatement(query);
            preparedStatement.setString(1, actor);
            resultSet = preparedStatement.getResultSet();
            //未找到改演员,创建一个节点
            if (resultSet == null){
                query = "CREATE (:Actor{name:{1}})";
                preparedStatement = connection.prepareStatement(query);
                preparedStatement.setString(1, actor);
                preparedStatement.executeUpdate();
            }

            // 第四步：对每一个演员节点查询演员与导演的合作关系是否存在
            query = "MATCH (a:Actor)-[r:Coo]-(d:Director) WHERE a.name={1} and d.name={2} RETURN r";
            preparedStatement = connection.prepareStatement(query);
            preparedStatement.setString(1, actor);
            preparedStatement.setString(2, data.getDirector());
            resultSet = preparedStatement.getResultSet();
            if (resultSet != null){
                // 若关系存在，将合作次数增加1
                times = resultSet.getInt("times") + 1;
            }
            else {
                // 若关系不存在，合作次数置为1
                times = 1;
            }
            query = "MATCH (a:Actor{name:{1}}),(d:Director{name:{2}}) MERGE (a)-[r:Coo{times:{3}}]->(d)";
            preparedStatement = connection.prepareStatement(query);
            preparedStatement.setString(1, actor);
            preparedStatement.setString(2, data.getDirector());
            preparedStatement.setInt(3, times);
            preparedStatement.executeUpdate();
        }

    }


    /**
     *
     * @param document Jsoup解析文件
     * @return 生成一个MovieData实例
     */
    public static MovieData ParseDoc(Document document) throws NullPointerException{
        MovieData data = new MovieData();
        // 判断页面格式
        Elements e = document.select("[id=\"productTitle\"]");
        // Movie & DVD 页面
        if (e != null){
            // 设置标题
            data.setTitle(e.text().trim());
            // 获取导演、演员信息
            Elements elements = document.select("[id=\"detail-bullets\"]>table>tbody>tr>td>div>ul>li");
            // 判断是否为电影页面
            boolean flagActor = false, flagDirector = false;
            if (elements.get(0).text().contains("Actors"))    flagActor = true;
            if (elements.get(1).text().contains("Directors")) flagDirector = true;
            if (!(flagActor && flagDirector)) return null;
            // 设置导演
            data.setDirector(elements.get(1).select("a").text());
            // 添加演员
            Elements actors = elements.get(0).select("a");
            for (Element actor : actors){
                data.addActors(actor.text());
            }
        }
        // Prime Movie页面
        else {
            // 设置标题
            data.setTitle(document.select("[data-automation-id=\"title\"]").text());
            // 获取导演、演员信息
            Elements elements = document.select("[data-automation-id=\"meta-info\"] > dl");
            // 设置导演
            data.setDirector(elements.get(1).getElementsByClass("a-link-normal").text());
            // 添加演员
            Elements actors = elements.get(2).getElementsByClass("a-link-normal");
            for (Element actor : actors){
                data.addActors(actor.text());
            }
        }
        return data;
    }

    /**
     *
     * @param file 需要解析的文件
     * @return 返回文件内容到字符串中
     */
    public static String ParseFile(File file){
        String html = "";
        try {
            FileInputStream fileInputStream = new FileInputStream(file);
            int size = fileInputStream.available();
            byte[] buffer = new byte[size];
            fileInputStream.read(buffer);
            fileInputStream.close();
            html = new String(buffer, "GB2312");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return "<html><head></head><body><h>Error</h></body></html>";
        }
        finally {
            return html;
        }
    }
}
