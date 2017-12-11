# -*- coding: utf-8 -*-
import pymysql
from main import *

print('Witaj w systemie ewidencji spraw Wydziału Architektury i Budownictwa Powiatu X')

while True:
     userLogin = str(input('\nPodaj login lub wciśnij enter i rozpocznij przeglądanie bez zalogowania \n[q] zakończ program:'))
     connectDatabase()
     
     while True:
          if userLogin == 'q':
               exitProgram()
          elif userLogin == '':
               print('Przeglądanie bez zalogowania')
               user = PublicUser()
               user.dispLegendPublicUser()
               userChoice = user.askForAction()
               user.decisionTreePublicUser(userChoice)
          elif userLogin == 'pracownik': #in lista użytkowników
               print('Zalogowano jako: Pracownik')
               user = Employee()
               user.dispLegendEmployee()
               userChoice = user.askForAction()
               user.decisionTreeEmployee(userChoice)               
               
               
          #--------------zamknąć blok w odrębną funkcje i przerzucić do pliku main (jeszcze nie umiem tego zrobić)
          logoutDecision = str(input('\n[enter] kontynuuj \n[l] wyloguj \n[q] zakończ program:'))
          if logoutDecision == 'l':
               break
          elif logoutDecision == 'q':
               exitProgram()
          else:
               continue
          #--------------zamknąć blok w odrębną funkcje i przerzucić do pliku main (jeszcze nie umiem tego zrobić)
      
     
          #dodać metodę w pliku klasy gdzie będą ify w zależności od wprowadzonej w cyfry z legendy - i to
          #też będzie mogło się dziedziczyć po kolejnych klasach bez powielania kodu
          #po wyświetleni tabeli po wciśnięciu entera powrót na początek tej wewnętrznej pętli i ponowne 
          #może do dispLegendPublicUser() dodać drzewko ifów z wywoływaniem poleceń w zależności od podanej 
          #przez użytkownika cyfry? TAK! da radę! dziedziczenei pierwszego drzewka jako metodyPublicUser() w 
          #drugim jak z wyswietlaniem metod!! np:


