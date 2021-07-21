select id,iname,cost from items where sid>(select sid from supplier where sname="Sandesh");
select sid,sname from supplier where sname in ("Sandesh","Sarvesh");
select * from supplier; 
select * from items where sid in(select sid from supplier where sname in ("Sandesh","Sarvesh"));
select * from items where sid>Any(select sid from supplier where sname in ("Sandesh","Sarvesh"));
select * from items where sid<Any(select sid from supplier where sname in ("Sandesh","Sarvesh"));
select * from items where sid>All(select sid from supplier where sname in ("Sandesh","Sarvesh"));
select * from items where sid <All(select sid from supplier where sname in ("Sandesh","Sanket0"));