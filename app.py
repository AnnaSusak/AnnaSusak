from flask import Flask
from flask import render_template

app = Flask(__name__)
import sqlite3


@app.route('/')
def index():
    conn = sqlite3.connect('bd.sqlite')
    cur = conn.cursor()
    create
    table
    stories
    (
        id      integer
    primary key autoincrement,
    main_page text,
    kontaks  text,
    blog  text,
    visible blob default TRUE
    );
    stories = []
    for main_page, kontaks, blog in cur.fetchall():
        stories.append({'main_page': values ('Приветсвую всех на моем первом сайте!','Коротко обо мне:
Меня зовут Сусак Анна Ивановна.
Мне 11 лет.
Я перехожу в шестой класс.');
update main set hello = 'Ann'; ('',, 'blog': 'Языки программирования
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

на Кипре');, 'kontaks': values ('Адрес: улица Какая-то, дом № Рандом
Телефон: 111-112-113-114
E-mail: zahodite.na.moy.cait.@it’s.cool.com');})

 select main_page, about, blog from stories where visible == TRUE;

cur.execute("""main_page, blog,about from stories where visible == ?;""", (True,))


    context = {'stories': stories}
    return render_template('index.html', **context)

    # основную логику функции прописываем после получения курсора,
    # но до закрытия соединения с БД

    conn.close()

    app.run()
