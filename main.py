import math
import random
import functools
import operator

# Narazie jest tylko 6 zadan

print("Napisz jakie zadanie chcesz sprawdzic np: zadanie1 aktualnie jest 6 zadan ")
zadanie = input()
if(zadanie == "zadanie1"):
  i = 1
  while(i <= 10):
    print("Podaj liczbe a: ")
    a = int(input())
    print("Podaj liczbe b: ")
    b = int(input())
    if(a == 0 or b == 0):
      print("Podales zero program zakonczy sie.")
      break
    else:
      print("Iloczyn tych liczb to: ", a * b)
    continue
if(zadanie == "zadanie2"):
  haslo = "1234"
  imie = "Patryk"
  nazwisko = "Niełacny"
  print("Podaj haslo masz 3 proby: ")
  proba = 1;
  while(proba <= 3):
    podaj_haslo = input()
    if(podaj_haslo == haslo):
      print("Podales poprawne hasło oto co było za nim ukryte:")
      print("\n",imie, nazwisko)
      break
    else:
      print("Podales zle haslo.")
      proba += 1
  print("\nPodales trzy razy złe hasło program zakonczył sie")
if(zadanie == "zadanie3"):
  i = 0
  lista = []
  kopia = []
  for i in range (0,10):
    x = random.randint(1,20)
    lista.append(x)
  print(lista)
  print("\nParzyste elementy listy: ")
  for i in range (0,10):
    if(lista[i] % 2 == 0):
      kopia.append(lista[i])
  print(kopia)
  print("\nPosortowane elementy parzyste:")
  print(sorted(kopia))
  print("\nPosortowane elemnty listy: ")
  print(sorted(lista))
if(zadanie == "zadanie4"):
  haslo = {'haslo' : '1234', 'proby' : 1}
  slownik = {'imie' : 'Patryk', 'nazwisko' : 'Niełacny'}
  print("Podaj haslo masz 3 proby: ")
  while(haslo['proby'] <= 3):
    podaj_haslo = input()
    if(podaj_haslo == haslo['haslo']):
      print("Podales poprawne hasło oto co było za nim ukryte:")
      print("\n", slownik['imie'], slownik['nazwisko'])
      break
    else:
      print("Podales zle haslo.")
      haslo['proby'] += 1
  print("\nPodales trzy razy złe hasło program zakonczył sie")
if(zadanie == "zadanie5"):
  lista_parzyste = []
  lista_nieparzyste = []
  liczby = {'parzyste' : 1, 'nieparzyste' : 1}
  while(liczby['parzyste'] < 4 and liczby['nieparzyste'] < 4):
    print("Podaj liczbe x: ")
    x = int(input())
    if(x % 2 == 0):
      lista_parzyste.append(x)
      liczby['parzyste'] += 1
      continue
    else:
      lista_nieparzyste.append(x)
      liczby['nieparzyste'] += 1
      continue
  if(liczby['parzyste'] == 4):
    print("Mnozenie 3 liczb parzystych wynosi: ",lista_parzyste[0] * lista_parzyste[1] * lista_parzyste[2])
  if(liczby['nieparzyste'] == 4):
    print("Mnozenie 3 liczb nieparzystych wynosi: ",lista_nieparzyste[0] * lista_nieparzyste[1] * lista_nieparzyste[2])
if(zadanie == "zadanie6"):
  listWord = ['P','a','t','r','y','k']
  print(listWord)
  lambdaresult = lambda x: listWord[0] + listWord[1] + listWord[2] + listWord[3] + listWord[4] + listWord[5]
  print(lambdaresult(listWord))