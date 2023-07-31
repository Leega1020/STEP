## task 3
- 1
```mysql
insert into member(name,username,password,follower_count) values('Amy','test','test',500);
insert into member(name,username,password,follower_count) values('Bob','member1','aaa123',200);
insert into member(name,username,password,follower_count) values('Cathy','member2','bbb123',700);
insert into member(name,username,password,follower_count) values('Debby','member3','ccc123',1200);
insert into member(name,username,password,follower_count) values('Eddie','member4','ddd123',500);
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/0c740819-5ea2-4904-aaa0-3be5ae059ff9" width="500" height="auto">

- 2
```mysql
select*from member;
```

- 3
```mysql
select*from member order by time asc;```

mysql> select*from member order by time asc limit 3 offset 1;

mysql> select*from member where username='test';

select*from member where username='test'and password='test';

mysql> update member set name='test2' where username='test';


select count(name) from member;

mysql> select sum(follower_count) from member;

select std(follower_count) from member;


mysql> select message.content,member.name from message inner join member on member.id = message.member_id;

mysql> select member.name,message.content from member inner join message
on member.id=message.member_id  where member.username='test';

mysql> select avg(like_count) from member inner join message on member.id=message.member_id  where member.username='test';
