CREATE DATABASE mydb; 
USE mydb; 



CREATE TABLE genres (genre_id BIGINT, name VARCHAR(255), PRIMARY KEY (genre_id));

INSERT INTO genres (genre_id, name) VALUES (1, "Sci-Fi");
INSERT INTO genres (genre_id, name) VALUES (2, "Drama");
INSERT INTO genres (genre_id, name) VALUES (3, "Action");
INSERT INTO genres (genre_id, name) VALUES (4, "Children");
INSERT INTO genres (genre_id, name) VALUES (5, "Musical");




CREATE TABLE movies (id BIGINT NOT NULL, title VARCHAR(1000) NOT NULL, year BIGINT, director VARCHAR(1000), revenue BIGINT, rating FLOAT, genre BIGINT, PRIMARY KEY (id));

INSERT INTO movies (id, title, year, director, revenue, rating, genre) VALUES (101, "Gone with the Wind", 1939, "Victor Fleming", 87432102, 4.1, 2);
INSERT INTO movies (id, title, year, director, revenue, rating, genre) VALUES (102, "Star Wars", 1977, "Robert Wise", 143192342, 3.9, 1);
INSERT INTO movies (id, title, year, director, revenue, rating, genre) VALUES (103, "ET", 1982, "Steven Spielberg", 456271290, 3.6, 1);
INSERT INTO movies (id, title, year, director, revenue, rating, genre) VALUES (104, "Titanic", 1997, "James Cameron", 349140923, 4.5, 3);
INSERT INTO movies (id, title, year, director, revenue, rating, genre) VALUES (105, "Avatar", 2009, "James Cameron", 2787965087, 4.2, 1);
INSERT INTO movies (id, title, year, director, revenue, rating, genre) VALUES (106, "Jurassic World", 2015, "Colin Trevorrow", 1670400367, 3.4, 1);
INSERT INTO movies (id, title, year, director, revenue, rating, genre) VALUES (107, "Furious 7", 2015, "James Wan", 1430400321, 3.5, 3);
INSERT INTO movies (id, title, year, director, revenue, rating, genre) VALUES (108, "Black Panther", 2018, "Ryan Coogler", 1320400945, 4.7, 3);
INSERT INTO movies (id, title, year, director, revenue, rating, genre) VALUES (109, "Frozen", 2013, "Jennifer Lee", 1243829093, 4.3, 4);
INSERT INTO movies (id, title, year, director, revenue, rating, genre) VALUES (110, "Raiders of the Lost Ark", 1981, "Steven Spielberg", 648324098, 3.6, 3);
INSERT INTO movies (id, title, year, director, revenue, rating, genre) VALUES (111, "The Sound of Music", 1965, "Robert Wise", 431480421, 3.8, 5);
INSERT INTO movies (id, title, year, director, revenue, rating, genre) VALUES (112, "Interstellar", 2014, "Christopher Nolan", 677383122, 4.4, 1);



CREATE TABLE users (id BIGINT AUTO_INCREMENT, username VARCHAR(255), password VARCHAR(255), email VARCHAR(255), PRIMARY KEY (id));



CREATE TABLE questions (id BIGINT AUTO_INCREMENT, question_text VARCHAR(255), difficulty VARCHAR(255), PRIMARY KEY (id));
INSERT INTO questions (question_text, difficulty) VALUES ("Which movie came out in 1997?", "Easy");
INSERT INTO questions (question_text, difficulty) VALUES ("Which movie earned the most revenue?", "Easy");
INSERT INTO questions (question_text, difficulty) VALUES ("How many movies were directed by James Cameron?", "Easy");
INSERT INTO questions (question_text, difficulty) VALUES ("What is the highest grossing movie that came out before 2000?", "Easy");
INSERT INTO questions (question_text, difficulty) VALUES ("Which genre has the most movies on this list?", "Medium");




CREATE TABLE answers (question_id BIGINT AUTO_INCREMENT, correct_query VARCHAR(255), PRIMARY KEY (question_id));
INSERT INTO answers (correct_query) VALUES ("SELECT title FROM movies WHERE year = 1997");
INSERT INTO answers (correct_query) VALUES ("SELECT title FROM movies ORDER BY revenue DESC LIMIT 1");
INSERT INTO answers (correct_query) VALUES ("SELECT COUNT(id) FROM movies WHERE director = 'James Cameron'");
INSERT INTO answers (correct_query) VALUES ("SELECT title FROM movies WHERE year < 2000 ORDER BY revenue DESC LIMIT 1");
INSERT INTO answers (correct_query) VALUES ("SELECT name FROM movies m JOIN genres g ON m.genre = g.genre_id GROUP BY genre ORDER BY COUNT(title) DESC LIMIT 1");




CREATE TABLE completed_questions (id BIGINT AUTO_INCREMENT, user_id BIGINT, question_id VARCHAR(255), completed_time DATETIME, PRIMARY KEY (id));



