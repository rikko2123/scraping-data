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

---

## 📝 Esempio di output JSON

{
  "['Award', 'Winner']": ["('Golden Ball', 'Lionel Messi')"]
}
