CREATE TABLE Lecteur(
        id_lecteur Int NOT NULL ,
        nom        Varchar (50) NOT NULL ,
        adresse    Varchar (50) NOT NULL ,
	 CONSTRAINT Lecteur_PK PRIMARY KEY (id_lecteur)
);

CREATE TABLE Ouvrage(
        isbn             Int NOT NULL ,
        titre            Varchar (50) NOT NULL ,
        date_emprunt     Date ,
        id_lecteur       Int ,
	 CONSTRAINT Ouvrage_PK PRIMARY KEY (isbn) ,
	 CONSTRAINT Ouvrage_Lecteur_FK FOREIGN KEY (id_lecteur) REFERENCES Lecteur(id_lecteur)
);

CREATE TABLE Reservation(
        isbn                Int NOT NULL ,
        id_lecteur          Int NOT NULL ,
        instant_reservation Datetime default CURRENT_TIMESTAMP ,
	 CONSTRAINT Reservation_PK PRIMARY KEY (isbn,id_lecteur) ,
	 CONSTRAINT Reservation_Ouvrage_FK FOREIGN KEY (isbn) REFERENCES Ouvrage(isbn) ,
	 CONSTRAINT Reservation_Lecteur0_FK FOREIGN KEY (id_lecteur) REFERENCES Lecteur(id_lecteur)
);
