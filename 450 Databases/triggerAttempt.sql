-- Theodore Church G01127117
--DROP TRIGGER newAverage;
CREATE TRIGGER newAverage
AFTER INSERT OR UPDATE ON Watch
Begin
    Update Movie
    Set Movie.avg_rating = (Select AVG(rating) from Watch where movie.movie_id = watch.movie_id);
END;
/

INSERT into Watch(Member_ID,Profile_Name,Movie_ID,Rating) values('mjohnson2','Mary','100004','5');
INSERT into watch(Member_ID,Profile_Name,Movie_ID,Rating) values('mjohnson','Mary','100004','5');
INSERT into watch(Member_ID,Profile_Name,Movie_ID,Rating) values('msimpson','Kids','100004','5');
INSERT into watch(Member_ID,Profile_Name,Movie_ID,Rating) values('bpitt','Brad','100004','5');
INSERT into watch(Member_ID,Profile_Name,Movie_ID,Rating) values('dsmith','David','100004','5');
INSERT into watch(Member_ID,Profile_Name,Movie_ID,Rating) values('dsmith','Kids','100004','5');
Select * from Movie;
Select * from Watch;


