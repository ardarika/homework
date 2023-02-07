SELECT film_name, actor_lname from films INNER JOIN actors ON (actors.actor_id = films.actor_id);

SELECT film_name, actor_fname, actor_lname from films INNER JOIN actors ON (actors.actor_id = films.actor_id);

SELECT film_name, films.director_lname, films.director_fname FROM films INNER JOIN directors ON (directors.director_id = films.director_id);

SELECT film_name, films.director_lname, films.director_fname FROM films LEFT JOIN directors ON (directors.director_id = films.director_id);

SELECT * FROM films ORDER BY imdb DESC;

SELECT DISTINCT release_year, film_name FROM films ORDER BY release_year;

SELECT DISTINCT release_year FROM films ORDER BY release_year;

SELECT * FROM directors WHERE films_amount BETWEEN 5 AND 23;
