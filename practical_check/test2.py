import requests

url = "https://raw.githubusercontent.com/hemanshidolar166-alt/Python-Pro-M.sc-IT-/main/Rank.py"

response = requests.get(url)

if response.status_code == 200:
    code = response.text
    print(code)
else:
    print("Failed to fetch file")