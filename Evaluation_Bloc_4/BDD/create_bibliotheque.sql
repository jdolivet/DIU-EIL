CREATE TABLE LECTEUR(
        id_lecteur Int NOT NULL ,
        nom        Varchar (50) NOT NULL ,
        adresse    Varchar (50) NOT NULL
	,CONSTRAINT LECTEUR_PK PRIMARY KEY (id_lecteur)
);

CREATE TABLE OUVRAGE(
        isbn             Int NOT NULL ,
        titre            Varchar (50) NOT NULL ,
        date_emprunt     Date ,
        id_lecteur       Int
	,CONSTRAINT OUVRAGE_PK PRIMARY KEY (isbn)

	,CONSTRAINT OUVRAGE_LECTEUR_FK FOREIGN KEY (id_lecteur) REFERENCES LECTEUR(id_lecteur)
);

CREATE TABLE RESERVATION(
        isbn                Int NOT NULL ,
        id_lecteur          Int NOT NULL ,
        instant_reservation Datetime default CURRENT_TIMESTAMP
	,CONSTRAINT RESERVATION_PK PRIMARY KEY (isbn,id_lecteur)

	,CONSTRAINT RESERVATION_OUVRAGE_FK FOREIGN KEY (isbn) REFERENCES OUVRAGE(isbn)
	,CONSTRAINT RESERVATION_LECTEUR0_FK FOREIGN KEY (id_lecteur) REFERENCES LECTEUR(id_lecteur)
);

