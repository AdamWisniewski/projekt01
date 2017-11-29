#CREATE VIEW pracownicy_obciazenie AS
    SELECT 
        pracownik_imie,
        pracownik_nazwisko,
        stanowisko_pracownik,
        liczba_prowadzonych_spraw,
        waga_prowadzonych_spraw
    FROM
        pracownicy AS p
            LEFT JOIN
        (SELECT 
            pracownik_prowadzacy_ID,
			COUNT(pracownik_prowadzacy_ID) AS liczba_prowadzonych_spraw,
            SUM(sprawa_waga) AS waga_prowadzonych_spraw
        FROM
            sprawy
        WHERE
            decyzja_numer IS NULL AND sprawa_status != 5  #nie zliczamy spraw zakończonych(wydana decyzja) oraz spraw zawieszonych
        GROUP BY pracownik_prowadzacy_ID) AS t ON p.ID = t.pracownik_prowadzacy_ID
			NATURAL LEFT JOIN
		stanowisko AS s 
        ORDER BY stanowisko_pracownik, pracownik_nazwisko;
 
 #CREATE VIEW sprawy_w_toku AS
    SELECT 
		sprawa_numer, 
        data_wniosku, 
        inwestor_imie, 
        inwestor_nazwisko, 
        inwestor_nazwa,
        sprawa_adres,
        sprawa_kategoria,
        sprawa_opis,
        sprawa_status,
        status_sprawy
	FROM
		sprawy,
        sprawa_status
	order by data_wniosku;
 
 
 select * from sprawy;
 
 
 load data local infile 'C:/Users/Kasia/Desktop/sprawy.txt' into table sprawy;
 
 Select p.*, s.* from pracownicy p natural left join stanowisko s;
 
 
# pomysł na trigger - jeżeli wpiszę numer decyzji to automatycznie status sprawy zmienia się na zakończona
