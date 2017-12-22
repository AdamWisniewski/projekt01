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
        return input('Podaj wybraną wartość z nawiasu: ')
        
    def dispAllProceduresFinished(self):
        try:
            c.execute('select * from allProceduresFinished')
            for row in c:
                print("|%3i|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|%3s|%3s|%3s|" %(row[0], row[1], row[2], str(row[3]), row[4], row[5], row[6], row[7], row[8], row[13], str(row[14]), row[15], row[16]))
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
        ulica = str(input('podaj nazwę ulic (bez skrótu ul. pl. al. itp.): '))
        numer = str(input('podaj szukany numer lub wciśnij [enter]: '))
        if numer == '':
            adres = str('\'' + ulica + '\'')
        else:
            adres = str('\'' + ulica + '' + numer +'\'')
        try:
            c.execute('select * from sprawy where sprawa_adres =' + adres)
            for row in c:
                print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|%3s|%3s|%3s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8], str(row[13]), row[14], row[15]))
        except:
            databaseError()

    def decisionTreePublicUser(self, x): # zawsze gdy wywołujemy funkcję która jest wewnątrz klasy pierwszym argumentem jest self
        
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
        
    def dispEmployeeList(self):
        try:
            c.execute('select * from allEmployee')
            print("|%3s|%10s|%10s|%20s|" %('ID', 'imię', 'nazwisko', 'stanowisko'))
            print('-'*48)
            for row in c:
                print("|%3s|%10s|%10s|%20s|" %(row[0],row[1],row[2],row[3]))
        except:
            databaseError()         
    
    def dispTargetEmployeeProceduresFinished(self):
        self.dispEmployeeList()
        x = str(input('podaj nazwisko pracownika; '))
        try:
            c.execute('select * from allProceduresFinished where pracownik_nazwisko =\'' + x + '\'')
            for row in c:
                print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|%3s|%3s|%3s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8], str(row[13]), row[14], row[15]))
        except:
            databaseError()
            
    def dispTargetEmployeeProceduresInProgress(self):
        self.dispEmployeeList()
        x = str(input('podaj nazwisko pracownika: '))
        try:
            c.execute('select * from allProceduresInProgress where pracownik_nazwisko =\'' + x + '\'')
            for row in c:
                print("|%3i|%3i|%10s|%12s|%15s|%12.12s|%20.20s|%3i|%-35s|" %(row[0], row[1], str(row[2]), row[3], row[4], row[5], row[6], row[7], row[8]))
        except:
            databaseError()
    
    # dodać funkcję editProcedure
    
    # dodać funkcję addDecision
    
    def decisionTreeEmployee(y, x):  # zawsze gdy wywołujemy funkcję która jest wewnątrz klasy pierwszym argumentem jest self
        
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
    
    def addNewProcedure(self): # funkcja nie działa
        #ID_sprawa - autoinkrementacja
        sprawa_numer = str(input('numer sprawy: '))
        data_wniosku = str(input('data wniosku w formacie XX-XX-XX'))
        inwestor_imie = str(input('imię inwestora :'))
        inwestor_nazwisko = str(input('nazwisko inwestora :'))
        inwestor_nazwa = str(input('nazwa inwestora :'))
        sprawa_adres = str(input('adres inwestycji :'))
        ID_sprawa_kategoria = str(input('kategoria sprawy od 1 do 30 :'))
        sprawa_opis = str(input('opis sprawy (max 150 znaków) :'))
        sprawa_waga = str(input('waga sprawy od 1 do 5 :'))
        ID_sprawa_status = str(input('status sprawy :'))
        #sprawa_deadline  = data_wniosku + 65 dni - wygenerować w SQL
        ID_pracownik = str(input('pracownik prowadzący od 1 do 5 :'))
        #decyzja_numer
        #decyzja_rok
        #decyzja_data_wydania
        #ID_decyzja_rodzaj
        #ID_decyzja_status
        komentarz = str(input('komentarz (max 200 znaków)'))
        
        try:
            c.execute("insert into sprawy values(null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, null, %s, null, null, null, null, null, %s)",
                      (sprawa_numer, data_wniosku, inwestor_imie, inwestor_nazwisko, inwestor_nazwa, sprawa_adres, ID_sprawa_kategoria, 
                       sprawa_opis, sprawa_waga, ID_sprawa_status, ID_pracownik, komentarz))
            conn.commit()
        except:
            databaseError()
    
    def addEmployee(self):
        self.dispEmployeeList()
        #ID_pracownik - autoinkrementacja
        pracownik_imie = str(input('imię pracownika :'))
        pracownik_nazwisko = str(input('nazwisko pracownika :'))
        ID_stanowisko = str(input('stanowisko prawownika = 1-6 :'))   
        
        try:
            c.execute("insert into pracownicy values(null, %s, %s, %s)",(pracownik_imie, pracownik_nazwisko, ID_stanowisko))
            conn.commit()
            print('Pracownik: ' + pracownik_imie + ' ' + pracownik_nazwisko + 'pomyślnie wprowadzony do systemu')
        except:
            databaseError()     
    
    def delEmployee(self):
        self.dispEmployeeList()
        ID_pracownik = str(input('\n podaj ID pracownika do usunięcia z systemu:'))    
        
        try:
            c.execute('delete from pracownicy where ID_pracownik =' + ID_pracownik)
            conn.commit()
            print('Pracownik został usunięty z systemu')
        except:
            databaseError()
        
    def editEmployee(self):
        self.dispEmployeeList()
        ID_pracownik = str(input('podaj ID pracownika do edycji : '))
        pracownik_imie = str(input('podaj nowe imię pracownika lub wciśnij [enter] : '))
        pracownik_nazwisko = str(input('podaj nowe nazwisko dla pracownika lub wciśnij [enter] : '))
        ID_stanowisko = str(input('podaj nowe stanowisko dla pracownika lub wciśnij [enter] : '))
        
        if pracownik_imie !='':
            try:
                c.execute('update pracownicy set pracownik_imie = \'' + pracownik_imie + '\' where ID_pracownik = ' + ID_pracownik)
                conn.commit()
                print('Dane pracownika pomyślnie edytowano')
            except:
                databaseError()
        
        if pracownik_nazwisko !='':
            try:
                c.execute('update pracownicy set pracownik_nazwisko = \'' + pracownik_nazwisko + '\' where ID_pracownik = ' + ID_pracownik)
                conn.commit()
                print('Dane pracownika pomyślnie edytowano')
            except:
                databaseError()
                
        if ID_stanowisko !='':
            try:
                c.execute('update pracownicy set ID_stanowisko = \'' + ID_stanowisko + '\' where ID_pracownik = ' + ID_pracownik)
                conn.commit()
                print('Dane pracownika pomyślnie edytowano')
            except:
                databaseError()
        else:
            print('dane pracownika nie zostały zmienone')
    
    def decisionTreeManager(y, x):  # zawsze gdy wywołujemy funkcję która jest wewnątrz klasy pierwszym argumentem jest self
        
        if x == '7':
            Manager().dispOverload()
        elif x == 'd':             
            Manager().addNewProcedure()
        elif x == 'p':
            Manager().addEmployee()
        elif x == 'u':
            Manager().delEmployee()
        elif x == 'e':
            Manager().editEmployee()            
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
    
    def decisionTreeAdmin(y, x):  # zawsze gdy wywołujemy funkcję która jest wewnątrz klasy pierwszym argumentem jest self
        
        if x == 'z':
            print('funkcja dodania użytkownika do systemu')
        elif x == 'x':             
            print('funkcja edycji LOGINu pracownika')
        elif x == 'c':
            print('funkcja edycji HASŁA pracownika')           
        else:
            Admin().decisionTreeManager(x)


