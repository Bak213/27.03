from asyncio import protocols
from symtable import Symbol
from urllib import response
import requests
#import swapi

    
from pprint import pprint

#name = input("podaj: nazwe ksiazki")

#format=input("podaj format: JSON lub wookiee")

while(1) : 
 print("1-lista planet 2-lista filmów 3-lista statków 4-break")
 wybierz = int(input()) 
 if wybierz == 1:
    
    print("1-szukaj po id 2-cala lista")
    wyb2 = int(input ())

    if wyb2 == 1:
        print("podaj id")
        id = int(input())
        url = "https://www.swapi.tech/api/planets/"
        response = requests.get(f"{url}{id}")  
        data = response.json()
        print(data)  
      
    else:
        url = "https://www.swapi.tech/api/planets/"
        response = requests.get(f"{url}") 
        data = response.json()
        print(data) 

 elif wybierz == 2:
     print("1-szukaj po tytule 2-cala lista")
     wyb3 = int(input ())
     if wyb3 == 1:

         print("podaj id")
         tytul = input()
         url = "https://www.swapi.tech/api/films/"
         response = requests.get(f"{url}{tytul}")  
         data = response.json()
         print(data) 
     else:
        url = "https://www.swapi.tech/api/films/"
        response = requests.get(f"{url}")  
        data = response.json()
        print(data) 

 elif wybierz == 3:
     print("1-szukaj po id 2-cala lista")
     wyb3 = int(input ())
     if wyb3 == 1:

         print("podaj id od 2")
         id = input()
         url = "https://www.swapi.tech/api/starships/"
         response = requests.get(f"{url}{id}")  
         data = response.json()
         print(data) 
     else:
        url = "https://www.swapi.tech/api/starships/"
        response = requests.get(f"{url}")  
        data = response.json()
        print(data) 




 elif wybierz == 4:
     break

    






