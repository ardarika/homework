create table data (id serial, name varchar(20), pwd varchar(50), email varchar(50), gender varchar(1));

insert into data(name, pwd, email, gender)
values ('Vasya', '21341234qwfsdf', 'mmm@mmail.com', 'm'),
('Alex', '21341234', 'mmm@gmail.com', 'm'),
('Alexey', 'qq21341234Q', 'alexey@gmail.com', 'm'),
('Helen', 'MarryMeeee', 'hell@gmail.com', 'f'),
('Jenny', 'SmakeMyb', 'eachup@gmail.com', 'f'),
('Lora', 'burn23', 'tpicks@gmail.com', 'f');

select 'This is' ||' '|| name || ','|| case when gender='m' then ' he has email' else ' she has email' end ||' '|| email from data;

select 'We have' || ' ' || count(gender) || ' ' || case when gender='m' then 'boys'
else 'girls!' end as "Gender information"
from data group by gender;

select name, count(word.vocabulary_id) as "words" from word inner join vocabulary on (vocabulary.id = word.vocabulary_id) 
group by name, vocabulary_id 
order by name;

