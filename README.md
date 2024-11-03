Projekt-Setup-Anleitung für Python 3.12.7
Diese Anleitung beschreibt die Schritte zur Installation und Konfiguration des Projekts mit Python 3.12.7.

Installation und Einrichtung

- Python-Version überprüfen
  Stelle sicher, dass Python 3.12.7 installiert ist:
  Befehl: python --version

- Virtuelle Umgebung erstellen
  Erstelle eine virtuelle Umgebung im Projektverzeichnis:
  Befehl: python -m venv env

- Virtuelle Umgebung aktivieren
  Aktiviere die virtuelle Umgebung:
  Befehl: .\env\Scripts\activate  # Für Windows PowerShell
  Befehl: env\Scripts\activate.bat  # Für Windows CMD
  Befehl: source env/bin/activate  # Für Unix/Linux

- Hinweis: Wenn ein Fehler bezüglich der Ausführungsrichtlinien auftritt, führe folgenden Befehl in PowerShell als Administrator aus:
  Befehl: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

- Abhängigkeiten installieren
  Installiere alle benötigten Pakete aus der requirements.txt:
  Befehl: pip install -r requirements.txt

- Wenn du die Pakete manuell installieren möchtest, nutze folgende Befehle:
  Befehl: python -m pip install Django  # Installiert Django
  Befehl: pip install djangorestframework  # Installiert Django REST Framework
  Befehl: python -m pip install django-cors-headers  # Installiert django-cors-headers für externen Zugriff

- Datenbankmigrationen durchführen
  Erstelle Migrationsdateien basierend auf den Modellen in models.py:
  Befehl: python manage.py makemigrations

  
- Führe die Migrationen aus, um die Tabellen in der Datenbank zu erstellen:
  Befehl: python manage.py migrate

  
- Server starten
  Navigiere in das Projektverzeichnis und starte den Server:
  Befehl: python manage.py runserver
  Der Server wird standardmäßig unter http://127.0.0.1:8000 laufen.
