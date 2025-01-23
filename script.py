import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('GITHUB_TOKEN')

username = 'vuejs'
repo = 'core'

url = f'https://api.github.com/repos/{username}/{repo}'
headers = {'Authorization': f'token {token}'}

response = requests.get(url, headers=headers)

repo_data = response.json()
contributors_url = repo_data.get('contributors_url')
forks_url = repo_data.get('forks_url')
issues_url = repo_data.get('issues_url').replace("{/number}", "")
subscribers_url = repo_data.get('subscribers_url')
stargazers_url = repo_data.get('stargazers_url')

os.makedirs('data', exist_ok=True)

def retrieve_data(url, headers, data_type):
    data = []
    page = 1
    while page <= 5:
        params = {'page': page, 'per_page': 100}
        if data_type == "issues":
            params["state"] = "all"
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            page_data = response.json()
            if not page_data:
                break
            data.extend(page_data)
            page += 1
        else:
            print(f'Error {response.status_code}: Unable to retrieve {data_type} data')
            break
    print(f'Number of {data_type} retrieved: {len(data)}')
    if data:
        pd.DataFrame(data).to_parquet(f'data/{data_type}_data.parquet')
        print(f'{data_type.capitalize()} data saved to {data_type}_data.parquet')
    else:
        print(f'No {data_type} data retrieved')
    return data


contributors_data = retrieve_data(contributors_url, headers, 'contributors')
forks_data = retrieve_data(forks_url, headers, 'forks')
issues_data = retrieve_data(issues_url, headers, 'issues')
suscribers_data = retrieve_data(subscribers_url, headers, 'suscribers')
stargazers_data = retrieve_data(stargazers_url, headers, 'stargazers')