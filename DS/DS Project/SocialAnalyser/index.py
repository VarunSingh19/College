import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
url = "https://www.statista.com/statistics/272014/global-social-networks-ranked-by-number-of-users/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
user_counts = []
social_networks = []
table = soup.find('table')
rows = table.find_all('tr')[1:]  

for row in rows:
    columns = row.find_all('td')
    social_network = columns[0].text.strip()
    users = int(columns[1].text.replace(',', '').strip())  
    social_networks.append(social_network)
    user_counts.append(users)

plt.figure(figsize=(12, 8))
plt.barh(social_networks, user_counts, color='skyblue', edgecolor='black')
plt.xlabel('Number of Users (in millions)', fontsize=14)
plt.ylabel('Social Network', fontsize=14)
plt.title('Social Networks Users Reach Analysis', fontsize=18, fontweight='bold')
for index, value in enumerate(user_counts):
    plt.text(value, index, f'{value:,}'+" millions", va='center', fontsize=12)

plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()

