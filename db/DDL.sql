create database recomendation_system;

use recomendation_system;

create table product(
    id int not null auto_increment,
    primary key(id),
    product_name varchar(50) not null,
    unique key uni_name_product(product_name)
);

create table rule(

    product_base int not null,
    product_recomendation int not null,
    foreign key(product_base) references product(id),
    foreign key(product_recomendation) references product(id)

);

create table compound_rule(

    product_a int not null,
    product_b int not null,
    product_recomendation int not null,

    foreign key(product_a) references product(id),
    foreign key(product_b) references product(id),
    foreign key(product_recomendation) references product(id)
);

create table transaction(
    Transaction int not null,
    Item varchar(30) not null,
    date_time datetime not null,
    period_day varchar(50) not null,
    weekday_weekend varchar(50) not null
);

insert into product(product_name) values("Café");
insert into product(product_name) values("Leite");
insert into product(product_name) values("Pão");
insert into product(product_name) values("Manteiga");


insert into rule(product_base,product_recomendation) values (1,2);
insert into rule(product_base,product_recomendation) values (3,4);

insert into compound_rule(product_a,product_b,product_recomendation) values (1,2,3);

insert into transaction(Transaction,Item,date_time,period_day,weekday_weekend) values(1,"Café","2021-05-05 10:30:45","morning","weekday");
insert into transaction(Transaction,Item,date_time,period_day,weekday_weekend) values(1,"Leite","2021-05-05 10:30:45","morning","weekday");
insert into transaction(Transaction,Item,date_time,period_day,weekday_weekend) values(2,"Café","2021-05-06 10:30:45","morning","weekday");
insert into transaction(Transaction,Item,date_time,period_day,weekday_weekend) values(2,"Leite","2021-05-06 10:30:45","morning","weekday");
insert into transaction(Transaction,Item,date_time,period_day,weekday_weekend) values(3,"Hamburguer","2021-07-06 16:45:45","afternoon","weekday");
insert into transaction(Transaction,Item,date_time,period_day,weekday_weekend) values(3,"Coca","2021-07-06 16:45:45","afternoon","weekday");
insert into transaction(Transaction,Item,date_time,period_day,weekday_weekend) values(4,"Hamburguer","2021-08-06 17:45:45","afternoon","weekday");
insert into transaction(Transaction,Item,date_time,period_day,weekday_weekend) values(4,"Coca","2021-08-06 17:45:45","afternoon","weekday");
insert into transaction(Transaction,Item,date_time,period_day,weekday_weekend) values(5,"Hot-Dog","2021-08-03 19:45:45","evening","weekday");

-- create table recomendation_rules(

--     id int not null auto_increment,

--     primary key(id),

--     product_name varchar(50) not null,

--     recomendation_product varchar(50) not null,

--     unique key uni_name_product(product_name)

-- );

-- insert into recomendation_rules(product_name,recomendation_product) values("Café","Leite");
-- insert into recomendation_rules(product_name,recomendation_product) values("Leite","Pão");
-- insert into recomendation_rules(product_name,recomendation_product) values("Pão","Manteiga");
-- insert into recomendation_rules(product_name,recomendation_product) values("Manteiga","Queijo");

