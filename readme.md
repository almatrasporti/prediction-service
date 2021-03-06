# Servizio di predizione consumi

Il modello di rete neurale addestrato con i dati batch viene utilizzato per le previsioni dei consumi in tempo reale.

A questo scopo viene utilizzato un semplice web-service REST scritto in Python utilizzando il framework _Flask_.

## Endpoint predizione consumi

Il servizio rende disponibile il seguente endpoint REST:

`POST /`: 

- Input: un documento json nella seguente forma:
```json
{
  "values": [
    100, 200, 300, ...
  ]
}
```
dove `values` è un array di valori numerici usati per effettuare la predizione, di dimensione pari alla finestra 
temporale usata in fase di addestramento del modello.

- Output: un document json nella seguente forma:
```json
{
  "prediction": 123.45,
  "values": [
    100, 200, 300, ...
  ]
}
```
dove `prediction` è il valore predetto dal modello e `values` è la replica dei valori utilizzati per effettuare la 
predizione.

## Implementazione

L'endpoint effettua tre operazioni principali:

- **Lettura della serie storica di input**: lettura dei dati contenuti nel documento json di input;
- **Caricamento strutture dati**: caricamento delle seguenti strutture da file system:
  - _Modello di rete neurale_: precedentemente addestrato nel fase di creazione modello;
  - _Scaler dei dati_: trasformazione per la normalizzazione dati, tarata sui dati usati per l'addestramento;
- **Predizione del dato successivo**: il modello viene valutato per ottenere il dato di predizione;
- **Creazione del docuemnto di output**: il dato predetto viene impacchettato nel documento per la risposta.