# Python developer - študent  

Tento python script, berie data zo stranky:    
[https://www.hyperia.sk], konkretne zacina -> [https://www.hyperia.sk/kariera/]  

Najde linky na vsetky pracovne ponuky a nasledne load-uje linky po jednom, a ziskava
data:
```buildoutcfg
{
    “title”: “Python developer”,
    “place”: “Slovensko”,
    “salary”: “od 1000 €”,
    “contract_type”: “dohoda”,
    “contact_email”: “hr@hyperia.sk”
}
```  
Kazdy jeden takyto python dictionary je pracovna ponuka, ktora je verejna na stranke.  

Nasledne vsetky tieto dictionaries uklada do listu (self.data) a na zaver vytvori z toho listu nas output, 
ktory je v .json formate.




