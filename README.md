# Backyard Recipes

## Overzicht

Backyard Recipes is een webapplicatie waarmee gebruikers recepten kunnen zoeken, bekijken en opslaan. De applicatie maakt gebruik van een Flask backend en een frontend geschreven in HTML en JavaScript. De applicatie is gehost op Azure.

## Backend

De backend is geschreven in [Flask](https://flask.palletsprojects.com/) en maakt gebruik van verschillende modules en functies om de functionaliteit van de webapplicatie te ondersteunen. Hieronder staan enkele belangrijke routes:

- `/registreren`: Endpoint voor het registreren van een nieuwe gebruiker.
- `/login`: Endpoint voor het inloggen van een gebruiker.
- `/checkemail`: Endpoint om te controleren of een e-mailadres al bestaat in de database.
- `/accountpagina/<username>`: Endpoint om de accountpagina van een gebruiker te renderen.
- `/receptdetails/<gid>`: Endpoint om receptdetails op te halen.
- `/receptaanmaken/<stap>` en `/receptaanmaken/<naam>`: Endpoints voor het toevoegen van stappen en namen aan recepten.

### Backend installatie en uitvoering

1. Installeer Flask en andere benodigde packages:

    ```
    pip install flask flask-cors
    ```

2. Start de backend server met het commando:

    ```
    flask run
    ```

## Frontend

De frontend van de applicatie is geschreven in HTML en JavaScript. De frontend maakt gebruik van Bootstrap voor de styling en heeft functionaliteiten zoals:

- Gebruikersgegevens bewerken
- Menu-items voor verschillende gebruikersacties
- Weergave van receptdetails

### Frontend installatie

Er is geen specifieke installatie vereist voor de frontend, omdat het een statische HTML-pagina is. 

## Configuratie

- De backend maakt gebruik van een `.env` bestand voor databaseconfiguratie en andere gevoelige informatie.
- De frontend maakt gebruik van localStorage om gebruikersgegevens op te slaan.

## Bijdragen

We waarderen bijdragen aan Backyard Recipes! Voel je vrij om een issue te openen of een pull-verzoek in te dienen.


