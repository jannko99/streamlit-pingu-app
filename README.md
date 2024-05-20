## Erläuterung des Codes:

Bibliotheken importieren:
- Wir verwenden streamlit für die App, pandas zum Laden und Bearbeiten der Daten, sowie seaborn und matplotlib für die Visualisierung.
Daten laden: 
- Das Beispiel-Datenset (Pinguindaten) wird aus dem Internet geladen und gecached, um die Ladezeiten zu reduzieren.
Daten anzeigen:
- Eine Tabelle zeigt die ersten fünf Zeilen des Datensatzes an.
Visualisierungsmethoden: 
- Der Benutzer kann zwischen einer Tabelle, einem Scatterplot und einem Histogramm wählen. Je nach Auswahl werden entsprechende Eingabefelder zur Steuerung der Anzeige angezeigt.
Eingabefelder: 
- Je nach Visualisierungsmethode können die Achsen für den Scatterplot oder die Spalte und die Anzahl der Bins für das Histogramm ausgewählt werden.

## App Starten

Um die App auszuführen, speichere den Code in einer Datei (z.B. app.py) und führe den Befehl streamlit run app.py in der Kommandozeile aus. Die App wird dann in deinem Standardbrowser geöffnet.

## Deployment

### Streamlit 

https://share.streamlit.io/

### Azure

```
az webapp create --resource-group jk-streamlit --plan jk-appplan-streamlit --name jk-webapp-streamlit --deployment-container-image-name jannko99/streamlit-pingu-app
```