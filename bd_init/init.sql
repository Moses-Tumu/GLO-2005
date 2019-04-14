CREATE DATABASE universite;
use universite;

CREATE TABLE users(
  firstName VARCHAR(20),
  lastName VARCHAR(20)
);

INSERT INTO users (firstName, lastName)
VALUES
       ("Moses", "Tumuhambaze"),
       ("Laurence", "Campeau");