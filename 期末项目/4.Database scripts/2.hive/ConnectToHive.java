package Connections;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConnectToHive {

    private static Connection connection = null;

    private static final String URL = "jdbc:hive2://10.60.42.201:10001";

    private static final String name = "root";
    private static final String pwd = "root";

    public static Connection getConnection() throws ClassNotFoundException, SQLException {
        if (connection == null){
            Class.forName("org.apache.hive.jdbc.HiveDriver");
            connection = DriverManager.getConnection(URL, name, pwd);
        }
        return connection;
    }

}
