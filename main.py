# -*- coding: utf-8 -*-
import pymysql
import sys

def connectDatabase():
    global conn 
    conn = pymysql.connect('localhost', 'root' , 'reaktor', 'wydzial_architektury', use_unicode=1, charset="utf8")
    global c 
    c = conn.cursor()

def databaseError():
    print('\nbłąd połączenia z bazą danych')
    
def askForPassword():
    return input('Podaj hasło: ')

def checkPassword(x):
    try:
        c.execute('select password from password where login =\'' + x + '\'')
        return c.fetchone()[0]
    except:
        pass

def createListOfLogins():
    try:
        c.execute('select login from password')
        return [item[0] for item in c.fetchall()]
    except:
        databaseError()
        
def checkPermissions(x):    
    try:
        c.execute('select id_permissions from password where login =\'' + x + '\'')
        return (c.fetchone()[0])
    except:
        databaseError()
        
def exitProgram():
    sys.exit()
    
# klasy przedstawiające rodzaje użytkowników serwisu

class PublicUser:
        
    def dispLegendPublicUser(self):
        print('[q] Wyjdź z programu \n[1] Wyświetl wszystkie sprawy w trakcie \n[2] Wyświetl wszystkie sprawy zakończone\n[3] Sprawdź postępowania dla wskazanego adresu')
        
    def askForAction(self):
        return input('Podaj wybraną wartość z nawiasu: ') # dlaczego to mi zwraca dwie wartości zamiast jednej jest dodatkowo <main.PublicUser object at 0x021E6130>
        
    def dispAllProceduresFinished(self):
        try:
            c.execute('select * from allProceduresFinished')
            for row in c:
                print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|%3s|%3s|%3s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8], str(row[13]), row[14], row[15]))
        except:
            databaseError()
            
    def dispAllProceduresInProgress(self):
        try:
            c.execute('select * from allProceduresInProgress')
            for row in c:
                print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8]))
        except:
            databaseError()
    
    def dispProceduresForAdress(self):
        adres = str(input('podaj szukany adres: '))
        adres = str('\'' + adres + '\'')
        try:
            c.execute('select * from sprawy where sprawa_adres =' + adres) # rozbić ulicę i numer w bazie by ułatwić wyszukiwanie
            for row in c:
                print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|%3s|%3s|%3s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8], str(row[13]), row[14], row[15]))
        except:
            databaseError()

    def decisionTreePublicUser(y, x): # usunąć drugi argument gdy zrozumiem jak on się tu pojawił :(
        #print(x)
        #print(y)
        
        if x == 'q':
            exitProgram()
        elif x == '1':             
            PublicUser().dispAllProceduresInProgress()
        elif x == '2':
            PublicUser().dispAllProceduresFinished()
        elif x == '3':
            PublicUser().dispProceduresForAdress()
        else:
            print('\nPodano błędną wartość')

class Employee(PublicUser):
        
    def dispLegendEmployee(self):
        self.dispLegendPublicUser()
        print('[4] Wyświetl sprawy w trakcie dla pracownika\n[5] Wyświetl sprawy zakończone dla pracownika\n[6] Edytuj sprawę')
    
    def dispTargetEmployeeProceduresFinished(self):
        x = str(input('podaj nazwisko pracownika; '))
        try:
            c.execute('select * from allProceduresFinished where pracownik_nazwisko =\'' + x + '\'')
            for row in c:
                print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|%3s|%3s|%3s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8], str(row[13]), row[14], row[15]))
        except:
            databaseError()
            
    def dispTargetEmployeeProceduresInProgress(self):
        x = str(input('podaj nazwisko pracownika: '))
        try:
            c.execute('select * from allProceduresInProgress where pracownik_nazwisko =\'' + x + '\'')
            for row in c:
                print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8]))
        except:
            databaseError()
    
    # dodać funkcję editProcedure
    
    def decisionTreeEmployee(y, x): # usunąć drugi argument gdy zrozumiem jak on się tu pojawił :(
        #print(x)
        #print(y)
        
        if x == '4':
            Employee().dispTargetEmployeeProceduresInProgress()
        elif x == '5':             
            Employee().dispTargetEmployeeProceduresFinished()
        elif x == '6':
            print('funkcja edycji sprawy')
        else:
            Employee().decisionTreePublicUser(x)

class Manager(Employee):
        
    def dispLegendManager(self):
        self.dispLegendEmployee()
        print('[7] Obciążenie pracowników \n[d] Dodaj nową sprawę\n[p] Dodaj pracownika\n[u] Usuń pracownika\n[e] Edytuj pracownika')
    
    def dispOverload(self):
        try:
            c.execute('select * from employee_overload')
            for row in c:
                print("|%10s|%10s|%20s|%5s|%5s|" %(row[0],row[1],row[2],row[3],row[4]))
        except:
            databaseError()
    
    # dodać funkcję addNewProcedure
    
    # dodać funkcję addEmploy
    
    # dodać funkcję delEmployee
        
    # dodać funkcję editEmployee
    
    def decisionTreeManager(y, x): # usunąć drugi argument gdy zrozumiem jak on się tu pojawił :(
        #print(x)
        #print(y)
        
        if x == '7':
            print(Manager().dispOverload())
        elif x == 'd':             
            print('funkcja dodawania nowej sprawy')
        elif x == 'p':
            print('funkcja dodawania nowego pracownika')
        elif x == 'u':
            print('funkcja usuwania pracownika')
        elif x == 'e':
            print('funkcja edycji pracownika')            
        else:
            Manager().decisionTreeEmployee(x)

class Admin(Manager):
        
    def dispLegendAdmin(self):
        self.dispLegendManager()
        print('[z] Dodaj użytkownika do systemu\n[x] Edytuj LOGIN pracownika\n[c] Edytuj HASŁO pracownika\n')
    
    # dodać funkcję addUser
    
    # dodać funkcję editLogin
    
    # dodać funkcję editPassword
    
    # dodać funkcję editPermissions
    
    def decisionTreeAdmin(y, x): # usunąć drugi argument gdy zrozumiem jak on się tu pojawił :(
        #print(x)
        #print(y)
        
        if x == 'z':
            print('funkcja dodania użytkownika do systemu')
        elif x == 'x':             
            print('funkcja edycji LOGINu pracownika')
        elif x == 'c':
            print('funkcja edycji HASŁA pracownika')           
        else:
            Admin().decisionTreeManager(x)


