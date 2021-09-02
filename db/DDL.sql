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

insert into product(product_name) values("Café");
insert into product(product_name) values("Leite");
insert into product(product_name) values("Pão");
insert into product(product_name) values("Manteiga");


insert into rule(product_base,product_recomendation) values (1,2);
insert into rule(product_base,product_recomendation) values (3,4);

insert into compound_rule(product_a,product_b,product_recomendation) values (1,2,3);

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

