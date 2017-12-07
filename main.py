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
        print('Przeglądanie bez zalogowania')
        
    def dispLegendPublicUser(self):
        print('[1] Wyświetl wszystkie sprawy w trakcie \n[2] Wyświetl wszystkie sprawy zakończone\n[3] Sprawdź postępowania dla wskazanego adresu')
        
    def askForAction(self):
        return input('Podaj wybraną wartość z nawiasu: ') # dlaczego to mi zwraca dwie wartości zamiast jednej jest dodatkowo <main.PublicUser object at 0x021E6130>
        
    #def dispAllProcedures(self):
        #c.execute('select * from sprawy')
        #for row in c:
            #print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|%3s|%3s|%3s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8], str(row[13]), row[14], row[15])) 
        
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

    def decisionTreePublicUser(y, x): # wywalić stąd drugi argument jak zrozumiem jak on się tu pojawił :(
        #print(x)
        #print(y)
        
        if x == '1':             
            PublicUser().dispAllProceduresInProgress()
        elif x == '2':
            PublicUser().dispAllProceduresFinished()
        elif x == '3':
            PublicUser().dispProceduresForAdress()        
               
    #def decisionTreePublicUserWrongInput(x):
        #dopisać wszystkie inne opcje że źle
        

class Employee(PublicUser):
    def __init__(self):
        print('Zalogowano jako' + 'dodac login')
        
    def dispLegendEmployee(self):
        self.dispLegendPublicUser()
        print('[4] Wyświetl moje sprawy w trakcie\n[5] Wyświetl moje sprawy zakończone\n[6] Edytuj sprawę')
    
    # dodać funkcję dispMyProceduresInProgress
    
    # dodać funkcję dispMyProceduresFinished
    
    # dodać funkcję editProcedure

class Manager(Employee):
    def __init__(self):
        print('Zalogowano jako Naczelnik')
        
    def dispLegendManager(self):
        self.dispLegendEmployee()
        print('[7] Obciążenie pracowników \n[d] Dodaj nową sprawę\n[p] Dodaj pracownika\n[u] Usuń pracownika\n[e] Edytuj pracownika')
    
    # dodać funkcję dispOverload
    
    # dodać funkcję addNewProcedure
    
    # dodać funkcję addEmployee
    
    # dodać funkcję delEmployee
        
    # dodać funkcję editEmployee

class Admin(Manager):
    def __init__(self):
        print('Zalogowano jako Administrator')
        
    def dispLegendAdmin(self):
        self.dispLegendManager()
        print('[z] Dodaj użytkownika do systemu\n[x] Edytuj LOGIN pracownika\n[c] Edytuj HASŁO pracownika\n')
    
    # dodać funkcję addPermissions
    
    # dodać funkcję editLogin
    
    # dodać funkcję editPassword


