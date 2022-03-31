-- Drop any existing tables.

drop table reserves cascade constraints;
drop table sailors cascade constraints;
drop table boats cascade constraints;

-- Add the three tables.

create table sailors(
        sid integer,
        sname varchar(30),
        rating integer,
        age real,
        primary key(sid)
        );

create table boats(
        bid integer,
        bname varchar(30),
        color varchar(10),
        primary key(bid)
        );

create table reserves(
        sid integer,
        bid integer,
        day date,
        primary key(sid,bid,day),
        foreign key(sid) references sailors,
        foreign key(bid) references boats
        );


-- Insert sample data

insert into sailors (sid, sname, rating, age)
        values (22, 'Dustin', 7, 45.0);
insert into sailors (sid, sname, rating, age)
        values (29, 'Brutus', 1, 33.0);
insert into sailors (sid, sname, rating, age)
        values (31, 'Lubber', 8, 55.5);
insert into sailors (sid, sname, rating, age)
        values (32, 'Andy', 8, 25.5);
insert into sailors (sid, sname, rating, age)
        values (58, 'Rusty', 10, 35.0);
insert into sailors (sid, sname, rating, age)
        values (64, 'Horatio', 7, 35.0);
insert into sailors (sid, sname, rating, age)
        values (71, 'Zorba', 10, 16.0);
insert into sailors (sid, sname, rating, age)
        values (74, 'Horatio', 9, 35.0);
insert into sailors (sid, sname, rating, age)
        values (85, 'Art', 3, 25.5);
insert into sailors (sid, sname, rating, age)
        values (95, 'Bob', 3, 63.5);

insert into boats (bid, bname, color)
        values (101, 'Interlake', 'blue');
insert into boats (bid, bname, color)
        values (102, 'Interlake', 'red');
insert into boats (bid, bname, color)
        values (103, 'Clipper', 'green');
insert into boats (bid, bname, color)
        values (104, 'Marine', 'red');

insert into reserves (sid, bid, day)
        values (22, 101, to_date('10/10/2004','mm/dd/yyyy'));
insert into reserves (sid, bid, day)
        values (22, 102, to_date('10/10/2004','mm/dd/yyyy'));
insert into reserves (sid, bid, day)
        values (22, 103, to_date('10/08/2004','mm/dd/yyyy'));
insert into reserves (sid, bid, day)
        values (22, 104, to_date('10/07/2004','mm/dd/yyyy'));
insert into reserves (sid, bid, day)
        values (31, 102, to_date('11/10/2004','mm/dd/yyyy'));
insert into reserves (sid, bid, day)
        values (31, 103, to_date('11/06/2004','mm/dd/yyyy'));
insert into reserves (sid, bid, day)
        values (31, 104, to_date('11/12/2004','mm/dd/yyyy'));
insert into reserves (sid, bid, day)
        values (64, 101, to_date('09/05/2004','mm/dd/yyyy'));
insert into reserves (sid, bid, day)
        values (64, 102, to_date('09/08/2004','mm/dd/yyyy'));
insert into reserves (sid, bid, day)
        values (74, 103, to_date('09/08/2004','mm/dd/yyyy'));

select * from sailors;
select * from boats;
select * from reserves;

/*
CREATE OR REPLACE TRIGGER notTooManyReservations
    BEFORE INSERT ON Reserves	                                       
    FOR EACH ROW
    DECLARE 
           res_count       INTEGER;                         
           Too_many        Exception;
    BEGIN                                                                                          
           SELECT COUNT(*) INTO res_count                                 
           FROM Reserves                         
           WHERE sid = :NEW.sid;              
           IF res_count > 3 THEN	           	
	         RAISE Too_many;
           END IF;
     EXCEPTION
          WHEN Too_many THEN
                 Raise_application_error(-20001, 'Too many reservations!');
	  END;	
/

select * from reserves;

insert into reserves (sid, bid, day)
        values (31, 104, to_date('12/12/2004','mm/dd/yyyy'));

*/       