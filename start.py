# -*- coding: utf-8 -*-
import pymysql
from main import *

print('Witaj w systemie ewidencji spraw Wydziału Architektury i Budownictwa Powiatu X')

while True:
     userLogin = str(input('\nPodaj login lub wciśnij enter i rozpocznij przeglądanie bez zalogowania \n[q] zakończ program:'))
     
     if userLogin == 'q':
          exitProgram()
     elif userLogin != '':
          userPassword = askForPassword()
     
     connectDatabase()
     
     # dodać funkcję sprawdzania czy dla podanego loginu jest hasło, jeżeli tak to continue, jeżeli nie to break?
     
     while True:
          if userLogin == '':
               print('\nPrzeglądanie bez zalogowania')
               user = PublicUser()
               user.dispLegendPublicUser()
               userChoice = user.askForAction()
               user.decisionTreePublicUser(userChoice)
          elif userLogin == 'pracownik': #in lista użytkowników
               print('\nZalogowano jako: Pracownik')
               user = Employee()
               user.dispLegendEmployee()
               userChoice = user.askForAction()
               user.decisionTreeEmployee(userChoice)               
          elif userLogin == 'naczelnik': # wprowadzić SQL
               print('\nZalogowano jako: Naczelnik')
               user = Manager()
               user.dispLegendManager()
               userChoice = user.askForAction()
               user.decisionTreeManager(userChoice)
          elif userLogin == 'admin': # wprowadzić SQL
               print('\nZalogowano jako: Administrator')
               user = Admin()
               user.dispLegendAdmin()
               userChoice = user.askForAction()
               user.decisionTreeAdmin(userChoice)       

          logoutDecision = str(input('\n[enter] kontynuuj \n[l] wyloguj \n[q] zakończ program:'))
          if logoutDecision == 'l':
               break
          elif logoutDecision == 'q':
               exitProgram()
          else:
               continue

