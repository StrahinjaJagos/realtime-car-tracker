# Praćenje Lokacije Automobila u Stvarnom Vremenu

## Instalacija

Prvo instalirajte sve pakete:
``
pip install -r requirements.txt
``

Pokrenite program za praćenje:
``
cd tracker
python tracker.py
``

## Pokretanje web servera

Za pokretanje web servera pokrenite:
``
python -m http.server
``

Za proslijeđivanje web aplikacije na javni URL pomoću ngrok-a pokrenite:
``
ngrok http 8000
``