/* Theodore Church G01127117 */
/*
1. Find the members who watched all of the movies that Hugh Jackman starred in. 
*/
Select M.member_ID 
from Members M
where not exists((Select A.actor_ID from Actor A Where A.first_name = 'Hugh' AND A.last_name = 'Jackman')
minus
(Select temp.actor_ID from (Select * from movie natural join watch natural join starred_by)temp where temp.member_ID = M.member_ID));
/*
2. For each member, print the member’s ID and the average rating he/she gave for 
movies, for members who rated at least 2 movies.
*/
Select M.Member_ID, AVG(S.rating)
from (Select W.member_ID from Watch W group by W.Member_ID having count(*)> 1)M, Watch S
where M.member_ID = S.member_ID
group by M.Member_ID;
/*
Select W.member_ID from Watch W group by W.Member_ID having count(*)> 1;
*/
/*
3. For each member, print the member’s ID and the number of the movies watched 
under the account. For example, suppose member David Smith has two profiles 
“David” and “Kids.” Also suppose that, under his account, 3 movies were 
watched using profile “David”, and 5 movies were watched using profile “Kids”, 
then you should print “dsmith   8”. If a member has not watched any movie, you 
should still print the member’s ID but with zero as the count. 
*/ 
Select S.member_ID, count(M.member_ID) 
from Members S left join Watch M on S.member_ID = M.member_ID 
group by S.member_ID;
/*
4. Find actors (actor_ID) who starred in the most movies.
*/
Select A.actor_ID
from (Select Count(S.Actor_ID)Acount, S.Actor_ID from Starred_by S group by S.Actor_ID)A
where A.Acount =
(Select Max(S.Acount) from (Select Count(S.Actor_ID)Acount, S.Actor_ID from Starred_by S group by S.Actor_ID)S);
/*
5. Find movies (movie_ID) that have the highest average rating. There might be 
more than one movie with such highest average rating.
*/
Select M.movie_ID
From (Select K.movie_ID, AVG(K.rating)Arating from Watch K group by K.movie_ID)M
where M.Arating = 
(Select MAX(Krating) from (Select K.movie_ID, AVG(K.rating)Krating from Watch K group by K.movie_ID));

