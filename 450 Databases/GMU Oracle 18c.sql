-- Students: Hrushikesh Ayalasomayajula, Theodore Church
-- Homework #2
-- Instructor  – Dr. Jessica Lin 
-- Emails: hayalaso@gmu.edu, tchurch@gmu.edu

DROP TABLE Members CASCADE CONSTRAINTS;
DROP TABLE Profiles CASCADE CONSTRAINTS;
DROP TABLE Actors CASCADE CONSTRAINTS;
DROP TABLE Movies CASCADE CONSTRAINTS;
DROP TABLE Movie_Genre CASCADE CONSTRAINTS;
DROP TABLE Profile_Likes CASCADE CONSTRAINTS;
DROP TABLE Cast_List CASCADE CONSTRAINTS;
DROP TABLE Genre CASCADE CONSTRAINTS;
DROP TABLE Watch CASCADE CONSTRAINTS;

CREATE TABLE Members
(member_id CHAR(5),
first_name VARCHAR2(20),
last_name VARCHAR2(20),
start_date DATE,
PRIMARY KEY(member_id));

CREATE TABLE Actors
(actor_id CHAR(5),
first_name VARCHAR2(20),
last_name VARCHAR2(20),
PRIMARY KEY(actor_id));

CREATE TABLE Movies
(movie_id CHAR(5),
title VARCHAR2(50),
movie_year INTEGER,
producer VARCHAR2(50),
avg_rating REAL,
PRIMARY KEY(movie_id));

CREATE TABLE Genre
(movie_genre CHAR(20),
PRIMARY KEY(movie_genre));

CREATE TABLE Movie_Genre
(movie_id CHAR(5),
movie_genre CHAR(20),
PRIMARY KEY(movie_id, movie_genre),
FOREIGN KEY(movie_id) REFERENCES Movies(movie_id));

CREATE TABLE Profiles
(member_id CHAR(5),
profile_name VARCHAR2(10),
PRIMARY KEY (member_id, profile_name),
FOREIGN KEY (member_id) REFERENCES Members(member_id));


CREATE TABLE Profile_Likes
(member_id CHAR(5),
profile_name VARCHAR2(10),
movie_genre CHAR(20),
PRIMARY KEY(member_id, profile_name, movie_genre),
FOREIGN KEY (member_id, profile_name) REFERENCES Profiles ON DELETE CASCADE,
FOREIGN KEY (movie_genre) REFERENCES Genre(movie_genre));

CREATE TABLE Cast_List
(actor_id CHAR(5), 
movie_id CHAR(5),
PRIMARY KEY (actor_id, movie_id),
FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
FOREIGN KEY (actor_id) REFERENCES Actors(actor_id));

CREATE TABLE Watch
(member_id CHAR(5), 
profile_name VARCHAR2(10),
rating INTEGER, 
movie_id CHAR(5),
PRIMARY KEY (member_id, profile_name, movie_id),
FOREIGN KEY (member_id, profile_name) REFERENCES Profiles ON DELETE CASCADE,
FOREIGN KEY (movie_id) REFERENCES Movies(movie_id));

INSERT INTO Members(member_id, first_name, last_name, start_date) VALUES ('1337', 'Homer', 'Simpson', TO_DATE('01/01/2021', 'MM/DD/YYYY'));
INSERT INTO Members(member_id, first_name, last_name, start_date) VALUES ('1338', 'Bart', 'Simpson', TO_DATE('06/22/2019', 'MM/DD/YYYY'));

INSERT INTO Actors(actor_id, first_name, last_name) VALUES('12345','Shane','Carruth');
INSERT INTO Actors(actor_id, first_name, last_name) VALUES('54321','Matt','Damon');

INSERT INTO Movies(movie_id, title, movie_year, producer, avg_rating) VALUES ('00001','Primer', 2004, 'Shane Carruth', 5);
INSERT INTO Movies(movie_id, title, movie_year, producer, avg_rating) VALUES ('00002','Good Will Hunting', 1997, 'Lawrence Bender', 5);

INSERT INTO Genre(movie_genre) VALUES('Suspense');
INSERT INTO Genre(movie_genre) VALUES('Drama');

INSERT INTO Movie_Genre(movie_id, movie_genre) VALUES('00001','Suspense');
INSERT INTO Movie_Genre(movie_id, movie_genre) VALUES('00002','Drama');

INSERT INTO Profiles(member_id, profile_name) VALUES('1337','dadmode');
INSERT INTO Profiles(member_id, profile_name) VALUES('1338','bartmode');

INSERT INTO Profile_Likes(member_id, profile_name, movie_genre) VALUES ('1337', 'dadmode', 'Suspense');
INSERT INTO Profile_Likes(member_id, profile_name, movie_genre) VALUES ('1338', 'bartmode', 'Drama');

INSERT INTO Cast_list(actor_id, movie_id) VALUES('12345','00001');
INSERT INTO Cast_list(actor_id, movie_id) VALUES('54321','00002');

INSERT INTO Watch(member_id, profile_name, rating, movie_id) VALUES('1337','dadmode',5,'00001');
INSERT INTO Watch(member_id, profile_name, rating, movie_id) VALUES('1338','bartmode',5,'00002');

SELECT * FROM Members; 
SELECT * FROM Profiles;
SELECT * FROM Actors;
SELECT * FROM Movies;
SELECT * FROM Movie_Genre; 
SELECT * FROM Profile_Likes;
SELECT * FROM Cast_List;
SELECT * FROM Genre;
SELECT * FROM Watch;