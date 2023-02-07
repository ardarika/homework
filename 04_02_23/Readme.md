films=# select * from directors;
 director_id | director_lname | director_fname | birh_year | films_amount | film_id | actor_id
-------------+----------------+----------------+-----------+--------------+---------+----------
           1 | Wachowsky      | Lana           |      1965 |           21 |       2 |        1
           2 | Fincher        | David          |      1962 |           19 |       3 |        4
           3 | Sommers        | Stephen        |      1962 |           15 |       4 |        3
           4 | Baird          | Jon            |      1972 |           11 |       1 |        2
(4 рядки)


films=# select * from films;
 film_id | film_name  | director_lname | director_fname | release_year | imdb | actor_id | director_id
---------+------------+----------------+----------------+--------------+------+----------+-------------
       1 | Filth      | Baird          | Jon            |         2013 |  7.0 |        2 |           4
       2 | The Matrix | Wachowsky      | Lana           |         1999 |  8.7 |        1 |           1
       3 | Se7en      | Fincher        | David          |         1995 |  8.6 |        4 |           2
       4 | The Mummy  | Sommers        | Stephen        |         1999 |  7.1 |        3 |           3
(4 рядки)


films=# select * from actors;
 actor_id | actor_lname | actor_fname | birh_year | film_id | director_id
----------+-------------+-------------+-----------+---------+-------------
        1 | Reeves      | Keanu       |      1964 |       2 |           1
        2 | McAvoy      | James       |      1979 |       1 |           4
        3 | Fraser      | Brendan     |      1968 |       4 |           3
        4 | Freeman     | Morgan      |      1937 |       3 |           2
(4 рядки)


films=# SELECT film_name, actor_lname from films INNER JOIN actors ON (actors.actor_id = films.actor_id);
 film_name  | actor_lname
------------+-------------
 The Matrix | Reeves
 Filth      | McAvoy
 The Mummy  | Fraser
 Se7en      | Freeman
(4 рядки)


films=# SELECT film_name, actor_fname, actor_lname from films INNER JOIN actors ON (actors.actor_id = films.actor_id);
 film_name  | actor_fname | actor_lname
------------+-------------+-------------
 The Matrix | Keanu       | Reeves
 Filth      | James       | McAvoy
 The Mummy  | Brendan     | Fraser
 Se7en      | Morgan      | Freeman
(4 рядки)


films=# SELECT film_name, films.director_lname, films.director_fname FROM films INNER JOIN directors ON (directors.director_id = films.director_id);
 film_name  | director_lname | director_fname
------------+----------------+----------------
 The Matrix | Wachowsky      | Lana
 Se7en      | Fincher        | David
 The Mummy  | Sommers        | Stephen
 Filth      | Baird          | Jon
(4 рядки)


films=# SELECT film_name, films.director_lname, films.director_fname FROM films LEFT JOIN directors ON (directors.director_id = films.director_id);
 film_name  | director_lname | director_fname
------------+----------------+----------------
 The Matrix | Wachowsky      | Lana
 Se7en      | Fincher        | David
 The Mummy  | Sommers        | Stephen
 Filth      | Baird          | Jon
(4 рядки)


films=# SELECT * FROM films ORDER BY imdb DESC;
 film_id | film_name  | director_lname | director_fname | release_year | imdb | actor_id | director_id
---------+------------+----------------+----------------+--------------+------+----------+-------------
       2 | The Matrix | Wachowsky      | Lana           |         1999 |  8.7 |        1 |           1
       3 | Se7en      | Fincher        | David          |         1995 |  8.6 |        4 |           2
       4 | The Mummy  | Sommers        | Stephen        |         1999 |  7.1 |        3 |           3
       1 | Filth      | Baird          | Jon            |         2013 |  7.0 |        2 |           4
(4 рядки)


films=# SELECT DISTINCT release_year, film_name FROM films ORDER BY release_year;
 release_year | film_name
--------------+------------
         1995 | Se7en
         1999 | The Matrix
         1999 | The Mummy
         2013 | Filth
(4 рядки)


films=# SELECT DISTINCT release_year FROM films ORDER BY release_year;
 release_year
--------------
         1995
         1999
         2013
(3 рядки)


films=# SELECT * FROM directors WHERE films_amount BETWEEN 5 AND 23;
 director_id | director_lname | director_fname | birh_year | films_amount | film_id | actor_id
-------------+----------------+----------------+-----------+--------------+---------+----------
           1 | Wachowsky      | Lana           |      1965 |           21 |       2 |        1
           2 | Fincher        | David          |      1962 |           19 |       3 |        4
           3 | Sommers        | Stephen        |      1962 |           15 |       4 |        3
           4 | Baird          | Jon            |      1972 |           11 |       1 |        2
(4 рядки)