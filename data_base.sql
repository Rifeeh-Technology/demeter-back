CREATE TABLE property (id serial PRIMARY KEY NOT NULL,
name varchar(255) NOT NULL,
geom_localization polygon NOT NULL,
create_date date NOT NULL
);

CREATE TABLE users (id serial PRIMARY KEY NOT NULL,
name varchar(255) NOT NULL,
birth_date date NOT NULL,
address varchar(255) NOT NULL,
type_user varchar(25) NOT NULL
)