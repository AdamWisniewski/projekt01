Projekt pozwala na zarządzanie prowadzonymi sprawami w ramach dowolnego wydziału Architektury i Budownictwa w Polsce.

podstawowe funkcje systemu to:
- ewidencja prowadzonych w wydziale postępowań w sprawie wydania pozwolenia na budowę
- nazdór nad zachowaniem ustawowych terminów
- nadzór nad obciążeniem pracowników pracą
- dekretacja spraw
- ewidencja wydanych decyzji
- 4 poziomy uprawnień wraz z logowaniem do systemu za pomocą ustalonego hasła


plik main.py:
- zestawienie klas i funkcji
- każda klasa odpowiada poziomowi uprawnień użytkownika w systemie
- każda kolejna klasa dziedziczy funkcje po wyższej klasie
- rodzaje użytkowników:
	PublicUser: przeglądanie spraw prowadzonych i wydanych również pod wskazanym adresem
	Employee: edytowanie procedur, wprowadzanie wydanych decyzji
	Manager: kontrola nad obciążeniem pracą, wprowadzanie nowych postępowań do systemu, zarządzanie personelem
	Admin: zarządzanie uprawnieniami użytkowników w systemie

plik start.py
- kod programu