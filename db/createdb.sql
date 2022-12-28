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

COMMIT TRANSACTION;