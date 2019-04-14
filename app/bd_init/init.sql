CREATE DATABASE universite;
use universite;

CREATE TABLE IF NOT EXISTS users(
  id INT NOT NULL AUTO_INCREMENT,
  firstName VARCHAR(20),
  lastName VARCHAR(20),
  PRIMARY KEY (id)
);

INSERT INTO users (firstName, lastName) VALUES ("Moses", "Tumuhambaze");