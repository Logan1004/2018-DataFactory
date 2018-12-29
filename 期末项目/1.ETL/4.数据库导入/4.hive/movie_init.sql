-- we don't know how to generate schema movie (class Schema) :(
create table actor
(
  id int ,
  name string
) row format delimited fields terminated by ','
;

create table format
(
  id int,
  type string
) row format delimited fields terminated by ','
;

create table language
(
  id int ,
  type string
) row format delimited fields terminated by ','
;


create table actor_act_movie
(
  actor_id int,
  movie_id string
) row format delimited fields terminated by ','
;
create table comment
(
  id int,
  summary string,
  movie_id string,
  score decimal,
  time bigint,
  helpfulness string
) row format delimited fields terminated by ','
;

create table movie_has_format
(
  format_id int,
  movie_id string
) row format delimited fields terminated by ','
;

create table movie_has_language
(
  language_id int,
  movie_id string
) row format delimited fields terminated by ','
;

create table producer
(
  id int,
  name string
) row format delimited fields terminated by ','
;

create table producer_produce_movie
(
  producer_id int,
  movie_id string
)
;
create table studio
(
  id int,
  name string
) row format delimited fields terminated by ','
;

create table studio_sponsor_movie
(
  studio_id int,
  movie_id string
) row format delimited fields terminated by ','
;

create table subtitle
(
  id int,
  language string
) row format delimited fields terminated by ','
;

create table movie_has_subtitle
(
  subtitle_id int,
  movie_id string
)
;

create table writer
(
  id int,
  name string
) row format delimited fields terminated by ','
;

create table writer_write_movies
(
  writer_id int,
  movie_id string
) row format delimited fields terminated by ','
;
create table genre (id int, type string) row format  delimited fields terminated by ',';
create table star_starring_movie (actor_id int, movie_id string) row format  delimited fields terminated by ',';
create table movie_has_genre (genre_id int, movie_id string) row format  delimited fields terminated by ',';