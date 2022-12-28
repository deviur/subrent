BEGIN TRANSACTION;

create table category(
    id integer primary key,
    name varchar(255),
    type integer,           /* type: -1 - Расходы, 0 - Залог, +1 - Доход (выручка) */
    tag_id varchar(255)
);

create table transactions(
    created integer,
    date varchar(255),
    category_id integer,
    income real,
    outcome real,
    foreign key (category_id) references category(id)
);

insert into category (id, name)
values
    (0, "Без категории");

insert into category (name, type, tag_id)
values
    ("Субаренда", 1, "b1940ce9-773c-462b-879e-aa3495f925dc"),
    ("Борисово", 1, "aa0fc6b7-4468-4435-b010-d2d7f0133de9"),
    ("Задонский", 1, "6259f28a-4151-4bdb-a492-2c5fa8551074"),
    ("Каширка", 1, "c07b5caa-9ca0-479e-9ae5-de84ca5a9be9"),
    ("Шипиловская", 1, "9b2bdf19-4178-421e-98bc-2f23409c143b");

COMMIT TRANSACTION;