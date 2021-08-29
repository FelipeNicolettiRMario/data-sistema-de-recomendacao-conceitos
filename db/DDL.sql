create database recomendation_system;

use recomendation_system;

create table recomendation_rules(

    id int not null auto_increment,

    primary key(id),

    product_name varchar(50) not null,

    recomendation_product varchar(50) not null,

    unique key uni_name_product(product_name)

);

insert into recomendation_rules(product_name,recomendation_product) values("Café","Leite");
insert into recomendation_rules(product_name,recomendation_product) values("Leite","Pão");
insert into recomendation_rules(product_name,recomendation_product) values("Pão","Manteiga");
insert into recomendation_rules(product_name,recomendation_product) values("Manteiga","Queijo");

