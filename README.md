# AI-UNIVR
Sviluppo e ciclo vitale di software di intelligenza artificiale UNIVR

**Descrizione del progetto:**

Il seguente codice è stato sviluppato per un progetto per il corso "Sviluppo e ciclo vitale di software di intelligenza artificiale" dell'Università di Verona.

L'obiettivo era creare un piccolo programma in Python che riesce a riconoscere immagini di lettere (dataset notMNIST).

**Contenuto:**

Codice Python per caricare il dataset
Un modello  di rete neurale
Un programma per addestrare il modello
Un test per controllare che il modello funzioni
Un file Docker per eseguire il progetto
Una pipeline automatica (CI/CD) che esegue i test ogni volta che faccio un push su GitHub

**Come eseguire il progetto:**

Installare le librerie:
pip install -r requirements.txt

Addestrare il modello:
python3 code/train.py

Lanciare i test:
pytest

Eseguire con Docker (se si vuole):
docker build -t ai-univr-project .
docker run ai-univr-project

**Cosa fa la CI/CD:**

Ogni volta che faccio un push su GitHub, parte in automatico un controllo che lancia i test.


Davide Buin
Università di Verona
Anno Accademico 2024/2025