#CREATE VIEW pracownicy_obciazenie AS
    SELECT 
        pracownik_imie,
        pracownik_nazwisko,
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
            decyzja_numer IS NULL AND sprawa_status != 5
        GROUP BY pracownik_prowadzacy_ID) AS t ON p.ID = t.pracownik_prowadzacy_ID
        ORDER BY liczba_prowadzonych_spraw DESC;
 
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
        
 select * from sprawa_status;
 
# pomysł na trigger - jeżeli wpiszę numer decyzji to automatycznie status sprawy zmienia się na zakończona
