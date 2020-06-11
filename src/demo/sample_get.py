import requests

url_index = r'http://127.0.0.1:12356'
res_index = requests.get(url_index)
print('res message:{}'.format(res_index.text))

