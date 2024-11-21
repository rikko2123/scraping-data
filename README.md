Scraper di Tabelle da Wikipedia
Questo progetto è uno scraper Python che estrae e salva i dati tabulari da pagine web, in particolare da una pagina di Wikipedia. Utilizza BeautifulSoup e requests per fare il parsing del contenuto HTML e raccogliere le tabelle, quindi memorizza i dati in file JSON per un uso successivo. È particolarmente utile per l'analisi automatizzata di dati strutturati da pagine web.

Funzionalità
Estrazione tabelle: Estrae tutte le tabelle dalla pagina Wikipedia specificata.
Salvataggio in JSON: I dati vengono salvati in file JSON, con le intestazioni delle tabelle come chiavi e i valori associati come tuple.
Codice sorgente salvato: Salva il codice HTML della pagina per facilitare l’analisi e il debug.
Conteggio dei tag: Conta i tag di tipo <table> presenti nella pagina, per fornire informazioni utili sulla struttura del documento.
Tecnologie utilizzate
Python: Linguaggio di programmazione utilizzato per lo sviluppo.
BeautifulSoup: Libreria per il parsing HTML e l'estrazione dei dati.
Requests: Libreria per fare richieste HTTP e recuperare il contenuto delle pagine.
JSON: Formato di archiviazione dei dati in modo strutturato e leggibile.
OS: Utilizzato per la gestione dei file e delle directory.

Come usarlo:
  Clona il repository:
  git clone https://github.com/tuo-utente/nome-del-progetto.git

  Installa le dipendenze:
  pip install beautifulsoup4 requests
  
  Esegui lo script:
  python scraper.py
