## task 3
- 3-1
```mysql
insert into member(name,username,password,follower_count) values('Amy','test','test',500);
insert into member(name,username,password,follower_count) values('Bob','member1','aaa123',200);
insert into member(name,username,password,follower_count) values('Cathy','member2','bbb123',700);
insert into member(name,username,password,follower_count) values('Debby','member3','ccc123',1200);
insert into member(name,username,password,follower_count) values('Eddie','member4','ddd123',500);
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/0c740819-5ea2-4904-aaa0-3be5ae059ff9" width="500" height="auto">

- 3-2
```mysql
select*from member;
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/e8c14f67-de6b-4ff8-9ec4-560b8ebcbbbd" width="500" height="auto">

- 3-3
```mysql
select*from member order by time asc;
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/d412dc12-33a7-40e8-8f90-56e058e732f8" width="500" height="auto">

- 3-4
```mysql
select*from member order by time asc limit 3 offset 1;
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/f2b79f9e-8ff6-4411-9854-ec0ad65f9302" width="500" height="auto">

- 3-5
```mysql
select*from member where username='test';
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/b5b40305-5083-4107-a1bf-0d76640fdc4a" width="500" height="auto">

- 3-6
```mysql
select*from member where username='test'and password='test';
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/fbe60989-7d9d-4adb-ba13-0997ffc005c4" width="500" height="auto">

- 3-7
```mysql
update member set name='test2' where username='test';
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/ead40e11-968b-4654-bf06-c75b689c8e32" width="500" height="auto">

## task 4
- 4-1
```mysql
select count(name) from member;
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/a197ed78-3627-448e-acc5-244eeea0beba" width="500" height="auto">

- 4-2
```mysql
select sum(follower_count) from member;
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/34558616-8ff1-4ec7-bff2-7cbc54f07f04" width="500" height="auto">

- 4-3
```mysql
select std(follower_count) from member;
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/90769443-fbdd-4138-b5e4-c7eebefe8643" width="500" height="auto">

## task 5
- 5-1
```mysql
select message.content,member.name from message inner join member on member.id = message.member_id;
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/cf02f907-2b38-4e58-822b-9906c10f8c1d" width="500" height="auto">

- 5-2
```mysql
select member.name,message.content from member inner join message
on member.id=message.member_id  where member.username='test';
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/35b93f00-5c3c-4129-a49a-0a2105262072" width="500" height="auto">

- 5-3
```mysql
select avg(like_count) from member inner join message on member.id=message.member_id  where member.username='test';
```
<img src="https://github.com/Leega1020/STEP/assets/134196665/f20e6c89-f0ef-4ba8-a4cf-c5ce66250fdd" width="500" height="auto">
