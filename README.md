# Scraper Tabelle HTML in JSON da Wikipedia (FIFA World Cup Awards)

Script in Python che ho scritto per allenarmi con il web scraping usando BeautifulSoup. L’obiettivo è semplice: prendo tutte le tabelle presenti nella pagina Wikipedia dei premi della Coppa del Mondo FIFA, le analizzo e salvo ogni tabella in un file `.json` ben strutturato.

---

## Cosa fa questo script

- Fa una richiesta HTTP alla pagina specificata
- Estrae tutte le `<table>` dalla pagina (fino a 15)
- Per ogni tabella:
  - prende le intestazioni (`<th>`) e i dati (`<td>`)
  - li struttura in un dizionario
  - li salva in un file JSON, uno per ogni tabella
- Chiede all’utente in quale cartella salvare i file

Salva anche il codice sorgente HTML della pagina in un file `sourcePagCode.html`, utile se si vuole controllare com'è strutturato il documento.


##🧱 Stack Tecnologico
#👨‍💻 Linguaggio
Python 3.6+ – Linguaggio scelto per la sua semplicità nella gestione di stringhe, strutture dati e richieste web.

#🕸 Librerie principali
requests – Per effettuare richieste HTTP e ottenere il contenuto della pagina web in modo semplice e robusto.

beautifulsoup4 – Per analizzare e navigare l'HTML usando parsing strutturato (con parser html.parser).

#🗂 File system
os – Per navigare e modificare il percorso di salvataggio dei file JSON direttamente dal terminale.

#📄 Output
File .json – Struttura dati standard, leggibile e facilmente riutilizzabile in altri linguaggi o strumenti (es. JavaScript, pandas, ecc.).
