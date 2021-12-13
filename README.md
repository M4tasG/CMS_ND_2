# CMS_ND_2
Simple blog created using Django backend

### Paleidimas
## Kadangi projektą įkėliau su duomenų baze, superuseris admin turėtų egzistuoti
## username: admin password: admin
Šis projektas reikalauja kad būtų instaliuota Python 3.9 programavimimo kalba
ir Django bibliotekos naujausia versija.
Suinstaliavus Python programavimo kalbą, įdiekite Django biblioteką atsidarius komandinį langą:
```
pip install django
```
Turėtų veikti ir pipenv failas suinstaliuojantis visus bibliotekų paketus tačiau dėl to neesu tikras. Suinstaliuojame pipenv ir tada įdiegiame aplinką:
```
pip install pipenv
cd [projekto-direktorija-kur-yra-Pipfile]
pipenv install
```
Atlikus šiuos  veiksmus, projektas yra paruoštas paleisti. Einame į manage.py 
direktorija ir atliekame veiksmus prieš paleidžiant projektą:
```
py manage.py makemigrations
py manage.py migrate
```
tada paleidžiame projektą:
```
py manage.py runserver
```
serveris yra paleidžiamas ant 8000 porto.
Atsidarome su naršykle http://localhost:8000/ ir galime naudotis puslapiu.
Norint prisijungti prie admin panelės, reikės administratoriaus paskyros.
```
py manage.py createsuperuser
```
atlikus veiksmus, bus galima prisijungti prie http://localhost:8000/admin/
