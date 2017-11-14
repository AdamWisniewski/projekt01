CREATE VIEW liczba_prowadzonych_spraw AS
    SELECT 
        pracownik_imie,
        pracownik_nazwisko,
        liczba_prowadzonych_spraw
    FROM
        pracownicy AS p
            LEFT JOIN
        (SELECT 
            pracownik_prowadzacy_ID,
                COUNT(pracownik_prowadzacy_ID) AS liczba_prowadzonych_spraw
        FROM
            sprawy
        WHERE
            decyzja_numer IS NULL
                OR sprawa_status = 5
        GROUP BY pracownik_prowadzacy_ID) AS t ON p.ID = t.pracownik_prowadzacy_ID;
    
# pomysł na trigger - jeżeli wpiszę numer decyzji to automatycznie status sprawy zmienia się na zakończona
