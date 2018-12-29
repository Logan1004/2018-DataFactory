package Connections;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConnectToMysql {

    private static Connection connection = null;

    private static final String URL = "jdbc:mysql://10.60.42.201:3307/movie";

    private static final String name = "root";
    private static final String pwd = "root";

    public static Connection getConnection() throws ClassNotFoundException, SQLException {
        if (connection == null){
            Class.forName("com.mysql.jdbc.Driver");
            connection = DriverManager.getConnection(URL, name, pwd);
        }
        return connection;
    }

}
