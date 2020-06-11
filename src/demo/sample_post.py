import requests

url_login = r'http://127.0.0.1:12356/login'
username = 'criss'
password = 'criss'

payload = 'username=' + username + '&password=' + password

res_login = requests.post(url_login, params=payload)
print(res_login.text)