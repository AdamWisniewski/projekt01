# -*- coding: utf-8 -*-
import pymysql
from main import *

print('Witaj w systemie ewidencji spraw Wydziału Architektury i Budownictwa Powiatu X')

while True:
     userLogin = str(input('Podaj login lub wciśnij enter i rozpocznij przeglądanie bez zalogowania :'))
     connectDatabase()
     
     if userLogin == '':
          user = PublicUser()
          user.dispLegendPublicUser()
          userChoice = user.askForAction()
          user.decisionTreePublicUser(userChoice)
          
            
          
          #user.decisionTreePublicUser(userChoice)
          #user.decisionTreePublicUserWrongInput(userChoice)
          #dodać metodę w pliku klasy gdzie będą ify w zależności od wprowadzonej w cyfry z legendy - i to
          #też będzie mogło się dziedziczyć po kolejnych klasach bez powielania kodu
          #po wyświetleni tabeli po wciśnięciu entera powrót na początek tej wewnętrznej pętli i ponowne 
          #wyświetlenie legendy
          #może do dispLegendPublicUser() dodać drzewko ifów z wywoływaniem poleceń w zależności od podanej 
          #przez użytkownika cyfry? TAK! da radę! dziedziczenei pierwszego drzewka jako metodyPublicUser() w 
          #drugim jak z wyswietlaniem metod!! np:


