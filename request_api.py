import requests

url = "http://localhost:5000/predict"


data = {"Age" : 42,
        "Account_Manager" : 1,
        "Years" : 6,
        "Num_Sites" : 18
        }


response = requests.post(url, data = data)

print(response.status_code)
print(response.json())


data = {"Age" : 22,
        "Account_Manager" : 1,
        "Years" : 1,
        "Num_Sites" : 1
        }


response = requests.post(url, data = data)

print(response.status_code)
print(response.json())