
create table if not exists main
(
  id integer
        primary key autoincrement,
  hello text,
  about text
);
insert into main
values ('Приветсвую всех на моем первом сайте!','Коротко обо мне:
Меня зовут Сусак Анна Ивановна.
Мне 11 лет.
Я перехожу в шестой класс.');
update main set hello = 'Ann';
create table if not exists blog
(
  id integer
        primary key autoincrement,
  head text,
  story text,
  image text
);
insert into blog
values ('','Языки программирования
Scratch
RobotC
Python
C#',
'Спорт
Я люблю заниматься спортом.Мне нравится:

настольный теннис
катание на:
роликах велосипеде лыжах',

'Языки
Русский(мой родной язык, изучаю с рождения)
Английский(первый иностранный, изучаю с 5 лет)
Немецкий(второй иностранный, изучаю с 11 лет)',
'Робототехника
Я работала с:
Роботами на базе Lego с языком Mindstorms
Роботами-C на базе Vex IQ с языком RobotC
Участвую в соревнованиях (участвовала в соревнованиях «Кегельринг» в прошлом году и в соревнованиях «Робофест» в этом году). Занимаюсь проектной деятельностью(получила диплом 3 степени за проект по робототехнике в конкурсе «Поиск-Нит»).',
'Путешествия
Мне нравится путешествовать потому, что путешествия дают новые впечатления и расширяют кругозор.

Я уже была в:

Испании

Италии

Греции

Хорватии

Болгария

ОАЭ

Египте

на Кипре');
create table if not exists contacts
(
    id integer
        primary key autoincrement,
    contakt text
);
insert into contacts
values ('Адрес: улица Какая-то, дом№Рандом
Телефон: 111-112-113-114
E-mail: zahodite.na.moy.cait.@it’s.cool.com');
select * from main;
select * from blog;
select * from contacts;
