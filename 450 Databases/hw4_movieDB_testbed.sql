-- Drop any existing tables.

drop table Members cascade constraints;
drop table Profiles cascade constraints;
drop table Genre cascade constraints;
drop table Movie cascade constraints;
drop table Actor cascade constraints;
drop table Watch cascade constraints;
drop table Starred_By cascade constraints;
drop table Like_Genre cascade constraints;
drop table Movie_Genre cascade constraints;


/* 

Member (member_ID: string, first_name: string, last_name: string, start_date: date)
Primary Key: member_ID
*/

create table Members(
    member_ID     varchar2(10),
    first_name    varchar2(20),
    last_name     varchar2(20),
    start_date    date,
    primary key(member_ID)
    );

insert into Members values('dsmith', 'David', 'Smith', '1-Aug-2019');
insert into Members values('bpitt', 'Brad', 'Pitt', '1-Dec-2019');
insert into Members values('msimpson', 'Marge', 'Simpson', '1-June-2020');
insert into Members values('jwilliams', 'John', 'Williams', '1-Dec-2020');
insert into Members values('mjohnson', 'Mary', 'Johnson', '1-Jan-2020');
insert into Members values('mjohnson2', 'Mary', 'Johnson', '1-Jan-2020');


/*
Profiles(member_ID: string, profile_name: string)
Primary Key: member_ID, profile_name
Foreign Key: member_ID references Members(member_ID) 
*/

create table Profiles(
    member_ID       varchar2(10),
    profile_name    varchar2(10),
    primary key(member_ID, profile_name),
    foreign key(member_ID) references Members(member_ID)
        on delete cascade
    );

insert into Profiles values('dsmith', 'David');
insert into Profiles values('dsmith', 'Kids');
insert into Profiles values('bpitt', 'Brad');
insert into Profiles values('msimpson', 'Homer');
insert into Profiles values('msimpson', 'Kids');
insert into Profiles values('jwilliams', 'John');
insert into Profiles values('mjohnson', 'Mary');
insert into Profiles values('mjohnson2', 'Mary');

/*
Genre(m_genre: string)
Primary Key: m_genre
*/

create table Genre(
    m_genre         varchar2(20),
    primary key(m_genre)
    );

insert into Genre values('Drama');
insert into Genre values('Comedy');
insert into Genre values('Documentary');
insert into Genre values('SciFi');
insert into Genre values('Romance');
insert into Genre values('Musical');
insert into Genre values('Action');
insert into Genre values('Fantasy');
insert into Genre values('Animation');

/*
Movie(movie_ID: string, title: string, movie_year: integer, producer: string, avg_rating: real)
Primary Key: movie_ID
*/

create table Movie(
    movie_ID        char(6),
    title           varchar2(50),
    movie_year      integer,
    producer        varchar2(40),
    avg_rating      real,
    primary key(movie_ID)
    );
    
insert into Movie values('100001', 'The Rise of Skywalker', 2019, 'J. J. Abrams‎', 3.0);
insert into Movie values('100002', 'The Last Jedi', 2017, 'J. J. Abrams‎', 3.2);
insert into Movie values('100003', 'Harry Potter and the Sorcerer''s Stone', 2001, 'David Heyman‎', 4.0);
insert into Movie values('100004', 'The Greatest Showman', 2017, 'Laurence Mark‎', 4.0);
insert into Movie values('100005', 'Beauty and the Beast', 2017, 'David Hoberman', 3.5);
insert into Movie values('100006', 'First Knight', 1995, 'Hunt Lowry', 3.0);

/*
Actor(actor_ID: string, first_name: string, last_name: string)
Primary Key: actor_ID
*/

create table Actor(
    actor_ID        varchar2(10),
    first_name      varchar2(20),
    last_name       varchar2(20),
    primary key(actor_ID)
    );
    
insert into Actor values('hjackman', 'Hugh', 'Jackman');
insert into Actor values('dradcliffe', 'Daniel', 'Radcliffe');
insert into Actor values('ewatson', 'Emma', 'Watson');
insert into Actor values('dridley', 'Daisy', 'Ridley');
insert into Actor values('cfisher', 'Carrie', 'Fisher');
insert into Actor values('mhamill', 'Mark', 'Hamill');
insert into Actor values('adriver', 'Adam', 'Driver');
insert into Actor values('dstevens', 'Daniel', 'Stevens');
insert into Actor values('rgrint', 'Rupert', 'Grint');
insert into Actor values('sconnery', 'Sean', 'Connery');
insert into Actor values('rgere', 'Richard', 'Gere');

/*
Starred_By(movie_ID: string, actor_ID: string)
Primary Key: (movie_ID, actor_ID)
Foreign Key: movie_ID references Movie(movie_ID)
Foreign Key: actor_ID references Actor(actor_ID)
*/

create table Starred_By(
    movie_ID        char(6),
    actor_ID        varchar2(10),
    primary key(movie_ID, actor_ID),
    foreign key(movie_ID) references Movie(movie_ID),
    foreign key(actor_ID) references Actor(actor_ID)
    );

-- The Rise of Skywalker
insert into Starred_By values('100001', 'mhamill');
insert into Starred_By values('100001', 'cfisher');
insert into Starred_By values('100001', 'dridley');
insert into Starred_By values('100001', 'adriver');

-- The Last Jedi
insert into Starred_By values('100002', 'mhamill');
insert into Starred_By values('100002', 'cfisher');
insert into Starred_By values('100002', 'dridley');
insert into Starred_By values('100002', 'adriver');

-- Harry Potter and the Sorcerer's Stone
insert into Starred_By values('100003', 'ewatson');
insert into Starred_By values('100003', 'dradcliffe');
insert into Starred_By values('100003', 'rgrint');

-- The Greatest Showman
insert into Starred_By values('100004', 'hjackman');

-- Beauty and the Beast
insert into Starred_By values('100005', 'ewatson');
insert into Starred_By values('100005', 'dstevens');

-- First Knight
insert into Starred_By values('100006', 'sconnery');
insert into Starred_By values('100006', 'rgere');

/*
Watch(member_ID: string, profile_name: string, movie_ID: string, rating: integer)
Primary Key: (member_ID, profile_name, movie_ID)
Foreign Key: (member_ID, profile_name) references Profiles(member_ID, profile_name)
Foreign Key: movie_ID references Movie(movie_ID)
*/

create table Watch(
    member_ID       varchar2(10),
    profile_name    varchar2(10),
    movie_ID        char(6),
    rating          integer,
    primary key(member_ID, profile_name, movie_ID),
    foreign key(member_ID, profile_name) references Profiles(member_ID, profile_name),
    foreign key(movie_ID) references Movie(movie_ID)
    );
    
insert into Watch values('dsmith', 'Kids', '100005', 4);
insert into Watch values('dsmith', 'Kids', '100001', 3);
insert into Watch values('dsmith', 'Kids', '100003', 4);
insert into Watch values('dsmith', 'Kids', '100002', 3);
insert into Watch values('dsmith', 'David', '100002', 4);
insert into Watch values('bpitt', 'Brad', '100002', 3);
insert into Watch values('bpitt', 'Brad', '100001', 4);
insert into Watch values('msimpson', 'Kids', '100005', 3);
insert into Watch values('msimpson', 'Homer', '100002', 3);
insert into Watch values('msimpson', 'Homer', '100004', 4);
insert into Watch values('msimpson', 'Kids', '100001', 2);
insert into Watch values('mjohnson', 'Mary', '100001', 3);
insert into Watch values('mjohnson2', 'Mary', '100002', 3);
insert into Watch values('mjohnson2', 'Mary', '100006', 3);

/*
Movie_Genre(movie_ID: string, m_genre: string)
Primary Key: (movie_ID, m_genre)
Foreign Key: movie_ID references Movie(movie_ID)
Foreign Key: m_genre references Genre(m_genre)
*/

create table Movie_Genre(
    movie_ID        char(6),
    m_genre         varchar2(20),
    primary key(movie_ID, m_genre),
    foreign key(movie_ID) references Movie(movie_ID),
    foreign key(m_genre) references Genre(m_genre)
    );

insert into Movie_Genre values('100001', 'SciFi');
insert into Movie_Genre values('100001', 'Action');
insert into Movie_Genre values('100001', 'Fantasy');
insert into Movie_Genre values('100002', 'SciFi');
insert into Movie_Genre values('100002', 'Action');
insert into Movie_Genre values('100002', 'Fantasy');
insert into Movie_Genre values('100003', 'Fantasy');
insert into Movie_Genre values('100004', 'Drama');
insert into Movie_Genre values('100004', 'Musical');
insert into Movie_Genre values('100005', 'Fantasy');
insert into Movie_Genre values('100005', 'Musical');
insert into Movie_Genre values('100005', 'Animation');
insert into Movie_Genre values('100006', 'Drama');
insert into Movie_Genre values('100006', 'Action');

/*
Likes_Genre(member_ID: profile_name: string, m_genre: string)
Primary Key: (member_ID, profile_name, m_genre)
Foreign Key: (member_ID, profile_name) references Profiles(member_ID, profile_name)
Foreign Key: m_genre references Genre(m_genre)

*/

create table Like_Genre(
    member_ID       varchar2(10),
    profile_name    varchar2(10),
    m_genre         varchar2(20),
    primary key(member_ID, profile_name, m_genre),
    foreign key(member_ID, profile_name) references Profiles(member_ID, profile_name),
    foreign key(m_genre) references Genre(m_genre)
    );

insert into Like_Genre values('dsmith', 'Kids', 'Fantasy');
insert into Like_Genre values('dsmith', 'Kids', 'Animation');
insert into Like_Genre values('dsmith', 'David', 'Action');
insert into Like_Genre values('dsmith', 'David', 'SciFi');
insert into Like_Genre values('bpitt', 'Brad', 'SciFi');
insert into Like_Genre values('bpitt', 'Brad', 'Action');
insert into Like_Genre values('msimpson', 'Homer', 'SciFi');
insert into Like_Genre values('msimpson', 'Homer', 'Drama');
insert into Like_Genre values('msimpson', 'Kids', 'Animation');
insert into Like_Genre values('msimpson', 'Kids', 'Fantasy');

select * from Members;
select * from Profiles;
select * from Genre;
select * from Movie;
select * from Actor;
select * from Movie_Genre;
select * from Starred_By;
select * from Watch;
select * from Like_Genre;






