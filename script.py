import requests
import pandas as pd
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()
token = os.getenv('GITHUB_TOKEN')

username = 'vuejs'
repo = 'core'

# URL de l'API GitHub pour obtenir les informations du dépôt
url = f'https://api.github.com/repos/{username}/{repo}'
headers = {
    'Authorization': f'token {token}'
}

print(f'Requête envoyée à {url}')
response = requests.get(url)
print(f'Statut de la réponse: {response.status_code}')

repo_data = response.json()
print('Données du dépôt récupérées')
contributors_url = repo_data.get('contributors_url')
forks_url = repo_data.get('forks_url')

# Récupérer les données des contributeurs
contributors_data = []
page = 1
while True and page <= 5:
    print(f'Requête envoyée à {contributors_url} pour la page {page}')
    contributors_response = requests.get(contributors_url, headers=headers, params={'page': page, 'per_page': 100})
    print(f'Statut de la réponse: {contributors_response.status_code}')
    if contributors_response.status_code == 200:
        data = contributors_response.json()
        if not data:
            break
        contributors_data.extend(data)
        page += 1
    else:
        print(f'Erreur {contributors_response.status_code}: Impossible de récupérer les données des contributeurs')
        break

print(f'Nombre de contributeurs récupérés: {len(contributors_data)}')
# Sauvegarder les données des contributeurs dans un fichier parquet
if contributors_data:
    contributors_df = pd.DataFrame(contributors_data)
    contributors_df.to_parquet('contributors_data.parquet')
    print('Données des contributeurs sauvegardées dans contributors_data.parquet')
else:
    print('Aucune donnée de contributeur récupérée')

# Récupérer les données des forks
forks_data = []
page = 1
while True and page <= 5:
    print(f'Requête envoyée à {forks_url} pour la page {page}')
    forks_response = requests.get(forks_url, headers=headers, params={'page': page, 'per_page': 100})
    print(f'Statut de la réponse: {forks_response.status_code}')
    if forks_response.status_code == 200:
        data = forks_response.json()
        if not data:
            break
        forks_data.extend(data)
        page += 1
    else:
        print(f'Erreur {forks_response.status_code}: Impossible de récupérer les données des forks')
        break

print(f'Nombre de forks récupérés: {len(forks_data)}')
# Sauvegarder les données des forks dans un fichier parquet
if forks_data:
    forks_df = pd.DataFrame(forks_data)
    forks_df.to_parquet('forks_data.parquet')
    print('Données des forks sauvegardées dans forks_data.parquet')
else:
    print('Aucune donnée de fork récupérée')