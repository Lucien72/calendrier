import requests

# URL de l'API
api_url = 'http://127.0.0.1:5000/calendrier'
stop = True

while(stop != "yes"):
    # Paramètres pour le mois et l'année
    month = input("Enter the month : ")
    year = input("Enter the year : ")

    # Faire une requête à l'API pour générer le calendrier
    response = requests.get(api_url, params={'month': month, 'year': year})

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Récupérer le calendrier généré depuis la réponse JSON
        calendrier_data = response.json()
        calendrier = calendrier_data.get('calendar')

        # Afficher le calendrier dans la console
        print(calendrier)
    else:
        print("PB pour récupérer le calendrier:", response.text)
    
    stop = input("Stop : ")
