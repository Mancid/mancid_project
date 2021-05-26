--PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
	id INTEGER NOT NULL, 
	email VARCHAR(100), 
	password VARCHAR(100), 
	name VARCHAR(1000), 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
INSERT INTO users VALUES(1,'damien2809@hotmail.fr','sha256$1SXm4EFqp4pvbgdz$7753d2536ac6a4b5f9c19f095ffd3ba13cb7615cd221f9d7e34fbb6b96112991','damien');
INSERT INTO users VALUES(2,'psgman3@msn.com','sha256$FvN4CTANw2AZGKRQ$8878a465247c9eb3898d0213175f333c49ec634e25ecdedd198cbd2a059bafb1','Nico');
COMMIT;
