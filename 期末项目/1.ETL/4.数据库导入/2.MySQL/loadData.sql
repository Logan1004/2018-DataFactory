load data infile '/var/lib/mysql-files/movie.csv'
into table movie
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;

load data infile '/var/lib/mysql-files/movie.csv'
into table movie
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;


load data infile '/var/lib/mysql-files/actor.csv'
into table actor
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;



load data infile '/var/lib/mysql-files/director.csv'
into table director
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;


load data infile '/var/lib/mysql-files/writer.csv'
into table writer
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;

-- !!!
load data infile '/var/lib/mysql-files/producer.csv'
into table producer
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;
-- ###

load data infile '/var/lib/mysql-files/language.csv'
into table language
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;



load data infile '/var/lib/mysql-files/subtitle.csv'
into table subtitle
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;


load data infile '/var/lib/mysql-files/format.csv'
into table format
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;

load data infile '/var/lib/mysql-files/genre.csv'
into table genre
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;



set FOREIGN_KEY_CHECKS=0; 
load data infile '/var/lib/mysql-files/direct_direct_movie.csv'
into table director_direct_movie
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;
set FOREIGN_KEY_CHECKS=1; 

set FOREIGN_KEY_CHECKS=0; 
load data infile '/var/lib/mysql-files/movie_has_subtitle.csv'
into table movie_has_subtitle
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;
set FOREIGN_KEY_CHECKS=1; 

set FOREIGN_KEY_CHECKS=0; 
load data infile '/var/lib/mysql-files/producer_produce_movie.csv'
into table producer_produce_movie
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;
set FOREIGN_KEY_CHECKS=1; 

set FOREIGN_KEY_CHECKS=0; 
load data infile '/var/lib/mysql-files/writer_write_movie.csv'
into table writer_write_movie
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;
set FOREIGN_KEY_CHECKS=1; 

set FOREIGN_KEY_CHECKS=0; 
load data infile '/var/lib/mysql-files/actor_act_movie.csv'
into table actor_act_movie
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;
set FOREIGN_KEY_CHECKS=1; 

set FOREIGN_KEY_CHECKS=0; 
load data infile '/var/lib/mysql-files/movie_has_language.csv'
into table movie_has_language
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;
set FOREIGN_KEY_CHECKS=1; 


set FOREIGN_KEY_CHECKS=0; 
load data infile '/var/lib/mysql-files/movie_has_format.csv'
into table movie_has_format
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;
set FOREIGN_KEY_CHECKS=1; 


set FOREIGN_KEY_CHECKS=0; 
load data infile '/var/lib/mysql-files/studio_sponsor_movie.csv'
into table studio_sponsor_movie
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;
set FOREIGN_KEY_CHECKS=1; 


set FOREIGN_KEY_CHECKS=0; 
load data infile '/var/lib/mysql-files/star_starring_movie.csv'
into table star_starring_movie
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;

load data infile '/var/lib/mysql-files/movie_has_genre.csv'
into table movie_has_genre
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;
set FOREIGN_KEY_CHECKS=1; 




