# -*- coding: utf-8 -*-
import pymysql

def connectDatabase():
    global conn 
    conn = pymysql.connect('localhost', 'root' , 'reaktor', 'wydzial_architektury', use_unicode=1, charset="utf8")
    global c 
    c = conn.cursor()    
 
    
# klasy przedstawiające rodzaje użytkowników serwisu
# ----pomyśleć jak skrócić wiersz definiujący wiświetlanie tabeli

class PublicUser:
    def __init__(self):
        print('Przeglądasz bez zalogowania')
        
    def dispLegendPublicUser(self):
        print('[1] Wyświetl wszystkie sprawy w trakcie \n[2] Wyświetl wszystkie sprawy zakończone\n[3] Sprawdź postępowania dla wskazanego adresu')
        
    def dispAllProcedures(self):
        c.execute('select * from sprawy')
        for row in c:
            print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|%3s|%3s|%3s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8], str(row[13]), row[14], row[15])) 
        
    def dispAllProceduresFinished(self):
        c.execute('select * from sprawy where decyzja_numer is not null')
        for row in c:
            print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|%3s|%3s|%3s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8], str(row[13]), row[14], row[15]))
            
    def dispAllProceduresInProgress(self):
        c.execute('select * from sprawy where decyzja_numer is null')
        for row in c:
            print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8]))    
    
    def dispProceduresForAdress(self):
        adres = str(input('podaj szukany adres: '))
        adres = str('\'' + adres + '\'')
        c.execute('select * from sprawy where sprawa_adres =' + adres) # rozbić ulicę i numer w bazie by ułatwić wyszukiwanie
        for row in c:
            print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|%3s|%3s|%3s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8], str(row[13]), row[14], row[15]))


class Employee(PublicUser):
    def __init__(self):
        print('Zalogowany jako' + 'dodac login')
        
    def dispLegendEmployee(self):
        a.dispLegendPublicUser(self)
        print('[4] Wyświetl moje sprawy w trakcie\n[5] Wyświetl moje sprawy zakończone\n[6] Edytuj sprawę')
    
    # dodać funkcję dispMyProceduresInProgress
    
    # dodać funkcję dispMyProceduresFinished
    
    # dodać funkcję editProcedure

class Manager(Employee):
    def __init__(self):
        print('Zalogowany jako Naczelnik')
        
    def dispLegendManager(self):
        a.dispLegendEmployee(self)
        print('[7] Obciążenie pracowników \n[d] Dodaj nową sprawę\n[p] Dodaj pracownika\n[u] Usuń pracownika\n[e] Edytuj pracownika')
    
    # dodać funkcję dispOverload
    
    # dodać funkcję addNewProcedure
    
    # dodać funkcję addEmployee
    
    # dodać funkcję delEmployee
        
    # dodać funkcję editEmployee

class Admin(Manager):
    def __init__(self):
        print('Zalogowany jako Administrator')
        
    def dispLegendAdmin(self):
        a.dispLegendManager(self)
        print('[z] Dodaj użytkownika do systemu\n[x] Edytuj LOGIN\n[c] Edytuj HASŁO\n')
    
    # dodać funkcję addPermissions
    
    # dodać funkcję editLogin
    
    # dodać funkcję editPassword




# polecenia testujące
connectDatabase()
a = Admin
a.dispLegendAdmin(Admin)