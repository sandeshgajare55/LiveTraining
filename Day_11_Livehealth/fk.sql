SELECT * FROM livehealth.items;
insert into items values(105,"Color",20,Null),(106,"Pass",10,903),(107,"Cardsheet",15,904),(108,"Notes",25,905);
SELECT * FROM livehealth.supplier;
insert into supplier values(903,"Sandy",86),(904,"Servo",94),(905,"Sanky",95);
desc items; 
select count(*) as 'Total No',sid from items where sid=(select sid from supplier where sname like "Sandesh")