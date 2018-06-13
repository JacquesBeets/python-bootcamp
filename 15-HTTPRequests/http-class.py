import requests

url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers={"Accept": "application/json"})

if response.ok:
  print("========================================================================================\n")
  print(f"Your response to {url} came back with status code {response.status_code}\n")
  print("========================================================================================\n")
else:
  print("===========================================================================================================\n")
  print(f"We encountered an error with the request to {url}. Status Code {response.status_code}\n")
  print("===========================================================================================================\n")
  
data = response.json()

print(data['joke'])