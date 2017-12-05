# -*- coding: utf-8 -*-
import pymysql

def connectDatabase():
    global conn 
    conn = pymysql.connect('localhost', 'root' , 'reaktor', 'wydzial_architektury', use_unicode=1, charset="utf8")
    global c 
    c = conn.cursor()    
 
    
# klasy przedstawiające rodzaje użytkowników serwisu
# pomyśleć jak skrócić wiersz definiujący wiświetlanie tabeli

class PublicUser:
    def __init__(self):
        print('Przeglądasz bez zalogowania')
        
    def dispLegendPublicUser(self):
        print('Wyświetl wszystkie sprawy w trakcie [1]\nWyświetl wszystkie sprawy zakończone[2]\nSprawdź postępowania dla wskazanego adresu[3]\n')
        
    def dispAllProceduresFinished(self):
        c.execute('select * from sprawy where decyzja_numer is not null')
        for row in c:
            print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|%3s|%3s|%3s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8], str(row[13]), row[14], row[15]))
            
    def dispAllProceduresInProgress(self):
        c.execute('select * from sprawy where decyzja_numer is null')
        for row in c:
            print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8]))    
    
    def dispAllProcedures(self):
        c.execute('select * from sprawy')
        for row in c:
            print(wzorzec(self))   
        
    def dispProceduresForAdress(self):
        adres = str(input('podaj szukany adres: '))
        adres = str('\'' + adres + '\'')
        c.execute('select * from sprawy where sprawa_adres =' + adres) # rozbić ulicę i numerw bazie by ułatwić wyszukiwanie
        for row in c:
            print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|%3s|%3s|%3s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8], str(row[13]), row[14], row[15]))


connectDatabase()
a = PublicUser()
a.dispProceduresForAdress()5