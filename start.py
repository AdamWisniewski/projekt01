# -*- coding: utf-8 -*-
import pymysql
from main import *

print('Witaj w systemie ewidencji spraw Wydziału Architektury i Budownictwa Powiatu X')

while True:
     userLogin = str(input('\n- Podaj login  \n- wciśnij enter i rozpocznij przeglądanie bez zalogowania \n- [q] zakończ program\n->'))
     
     if userLogin == 'q':
          exitProgram()
     elif userLogin != '':
          userPassword = askForPassword()
          connectDatabase()
          if userPassword == checkPassword(userLogin):
               print('poprawnie zalogowano')
          else:
               print('\npodano błędny login lub hasło')
               continue
     
     logins = createListOfLogins()
          
     while True:
          if userLogin == '':
               print('\nPrzeglądanie bez zalogowania')
               user = PublicUser()
               user.dispLegendPublicUser()
               userChoice = user.askForAction()
               user.decisionTreePublicUser(userChoice)             
          elif userLogin == 'naczelnik':
               print('\nZalogowano jako: Naczelnik')
               user = Manager()
               user.dispLegendManager()
               userChoice = user.askForAction()
               user.decisionTreeManager(userChoice)
          elif userLogin == 'admin':
               print('\nZalogowano jako: Administrator')
               user = Admin()
               user.dispLegendAdmin()
               userChoice = user.askForAction()
               user.decisionTreeAdmin(userChoice)
          elif userLogin in logins:
               print('\nZalogowano jako: ' + userLogin)
               user = Employee()
               user.dispLegendEmployee()
               userChoice = user.askForAction()
               user.decisionTreeEmployee(userChoice)                 

          logoutDecision = str(input('\n[enter] kontynuuj \n[l] panel logowania \n[q] zakończ program:'))
          if logoutDecision == 'l':
               break
          elif logoutDecision == 'q':
               exitProgram()
          else:
               continue

