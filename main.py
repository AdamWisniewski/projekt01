# -*- coding: utf-8 -*-
import pymysql

def connectDatabase():
    global conn 
    conn = pymysql.connect('localhost', 'root' , 'reaktor', 'wydzial_architektury', use_unicode=1, charset="utf8")
    global c 
    c = conn.cursor()    
 
    
# klasy przedstawiające rodzaje użytkowników serwisu

class PublicUser:
    def __init__(self):
        print('Przeglądasz bez zalogowania')
        
    def dispLegendPublicUser(self):
        print('Wyświetl wszystkie sprawy w trakcie [1]\nWyświetl wszystkie sprawy zakończone[2]\nSprawdź postępowania dla wskazanego adresu[3]\n')
        
    def dispAllProceduresFinished(self):
        c.execute('select * from pracownicy')
        for row in c:
            print (row)        
        
connectDatabase()
a = PublicUser()
a.dispAllProceduresFinished()