package Service;

import Connections.ConnectToHive;
import Connections.ConnectToMysql;
import Connections.ConnectToNeo4j;

import java.sql.SQLException;
import java.util.Date;
import java.util.List;

public class CombinedService {

    private HiveService hiveService = null;
    private Neo4jService neo4jService = null;
    private MysqlService mysqlService = null;

    public CombinedService() throws SQLException, ClassNotFoundException {
        this.hiveService = new HiveService(ConnectToHive.getConnection());
        this.neo4jService = new Neo4jService(ConnectToNeo4j.getConnection());
        this.mysqlService = new MysqlService(ConnectToMysql.getConnection());
    }

    public CombinedService(HiveService hiveService, Neo4jService neo4jService, MysqlService mysqlService) {
        this.hiveService = hiveService;
        this.neo4jService = neo4jService;
        this.mysqlService = mysqlService;
    }

    public HiveService getHiveService() {
        return hiveService;
    }

    public Neo4jService getNeo4jService() {
        return neo4jService;
    }

    public MysqlService getMysqlService() {
        return mysqlService;
    }

    public Integer maxCoorWithActors(String actorName, List<String> actors){
        Integer max = 0;
        long start = new Date().getTime();
        for (String actor : actors){
            Integer tmp = neo4jService.getCooperatedMovieAA(actorName, actor);
            max = max < tmp ? tmp : max;
        }
        long end = new Date().getTime();
        System.out.println(end-start + "ms");
        return max;
    }

    public Integer maxCoorWithDirectors(String actorName, List<String> directors){
        Integer max = 0;
        long start = new Date().getTime();
        for (String director : directors){
            Integer tmp = neo4jService.getCooperatedMovieAD(actorName, director);
            max = max < tmp ? tmp : max;
        }
        long end = new Date().getTime();
        System.out.println(end-start + "ms");
        return max;
    }

}
