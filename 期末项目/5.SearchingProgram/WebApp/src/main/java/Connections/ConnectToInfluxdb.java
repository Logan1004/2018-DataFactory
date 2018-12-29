package Connections;

import java.util.Map;
import org.influxdb.InfluxDB;
import org.influxdb.InfluxDBFactory;
import org.influxdb.dto.Point;
import org.influxdb.dto.Point.Builder;
import org.influxdb.dto.Pong;
import org.influxdb.dto.Query;
import org.influxdb.dto.QueryResult;

public class ConnectToInfluxdb {


    private static String URL = "http://10.60.42.201:8086";
    private static String name = "admin";
    private static String pwd = "1234";
    private static String db = "newdb";
    private static String mesurement = "test";

    private static InfluxDB influxDB;

    public static InfluxDB getInfluxDB(){
        if (influxDB == null){
            influxDB = InfluxDBFactory.connect(URL, name, pwd);
            Pong pong = influxDB.ping();
            if (pong != null){
                System.out.println(pong + "：连接成功");
            }else {
                System.out.println("连接失败");
                influxDB = null;
            }
        }
        return influxDB;
    }
    /**
     * 设置数据保存策略
     * defalut 策略名 /database 数据库名/ 30d 数据保存时限30天/ 1  副本个数为1/ 结尾DEFAULT 表示 设为默认的策略
     */
    public void createRetentionPolicy(){
        String command = String.format("CREATE RETENTION POLICY \"%s\" ON \"%s\" DURATION %s REPLICATION %s DEFAULT",
                "defalut", db, "30d", 1);
        this.query(command);
    }

    /**
     * 查询
     * @param command 查询语句
     * @return
     */
    public QueryResult query(String command){
        return influxDB.query(new Query(command, db));
    }

    /**
     * 插入
     * @param tags 标签
     * @param fields 字段
     */
    /**
     * 删除
     * @param command 删除语句
     * @return 返回错误信息
     */
    public String deleteMeasurementData(String command){
        QueryResult result = influxDB.query(new Query(command, db));
        return result.getError();
    }

    /**
     * 创建数据库
     * @param dbName
     */
    public void createDB(String dbName){
        influxDB.createDatabase(dbName);
    }

    /**
     * 删除数据库
     * @param dbName
     */
    public void deleteDB(String dbName){
        influxDB.deleteDatabase(dbName);
    }

    public String getUsername() {
        return name;
    }

    public void setUsername(String username) {
        this.name = username;
    }

    public String getPassword() {
        return pwd;
    }

    public void setPassword(String password) {
        this.pwd = password;
    }

    public String getOpenurl() {
        return URL;
    }

    public void setOpenurl(String openurl) {
        this.URL = openurl;
    }

    public void setDatabase(String database) {
        this.db = database;
    }
}


