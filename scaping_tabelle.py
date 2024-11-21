from bs4 import BeautifulSoup
import requests
import json
from json import JSONDecodeError
import os

#prendo codice sorgente pagina, che mi serve per capire come è stutturato il documento
def getSourceCode(soup):
    with open('sourcePagCode.html', 'w') as sourceHTML:
        sourceHTML.write(str(soup))

#cerco fra tutti i tag quelli che mi interessano
def searchTag(t, soup) -> int:
    count = 0
    for tag in soup.find_all():
        if hasattr(tag, 'name'):
            if tag.name == t:
             count += 1
    return count   

#prendo i dati che mi servono ciclo per ogni tablella. gli metto un max di iterazioni
#la tabella vedendo il codice sorgente è trutturata table -> tbody -> th e td
#quindi ad ogni tabella mi storo in due array  i dati che mi interessano 
# attraverso.append, che al suo interno avra un for che inserira tutti i th e td nei rispettivi array 
#le th sono da convertire in str mentre le liste di td che ho generato sono da conertite in tuple per fare in modo
#che sia hashabili, fatto questo apro il json, a storo i dati al suo interno
def getTableData(soup):
    #per ogni tabella che trovo apro un file json che rappresentera i suoi dati
    for table in soup.find_all('table')[:15]:
        #prima di inserire i dati in un json devo prima convertirli in un dizionario
        #cerco i table head e li uso come chiave
        ths = []
        #cerco i td(table data) e li uso come valore
        tds = []
        #cerco i th e aggiungo il loro contenuto con .text, se non c'è un th inserisco ''
        ths.append([th.text for th in table.find_all('th')])
        #aggiungo le sue corrispondenti righe
        tds.append([data.text if table.find('td') else '' for data in table.find_all('td')]) 
        #aggiungo i valori presi all'interno di dati e li converto in un dizionario
        # print(f'this is table head{tds}')
        # print('----------------------------------------------------------------------------------')

        #converto in str le t head
        ths = [str(th) for th in ths]
        #converto in tuple le liste all'interno di t data
        tds = [tuple(str(td)) for td in tds]
        #creo dizionario con accoppiamenti
        diz = dict(zip(ths, tds))
        #salvo i file nella dir specificata
        os.chdir('/home/rikko/Desktop/stuff-in-python/python_scaping/scraping_tabelle/data')
        try:
            #nomino il json come la tabella che ho preso
            nameTable = table.find('caption').text
        except AttributeError as e:
            print(f'error {e}')
        #creo json e scrivo sopra i dati
        with open (f'{nameTable}.json', 'w') as file:
            json.dump(diz, file, indent=4)

def main():
    #prendo pagita tramite una richesta get
    url = 'https://en.wikipedia.org/wiki/FIFA_World_Cup_awards'
    page = requests.get(url)
    #gestisce errori http 
    page.raise_for_status() 

    try:
        #istanzio soup
        soup = BeautifulSoup(page.content, 'html.parser')
        getSourceCode(soup)
        print(searchTag("table", soup))

        getTableData(soup)

    except requests.RequestException as e:
        print(f"C'è statpo un errore: {e}")

if __name__ == '__main__':
    main()
