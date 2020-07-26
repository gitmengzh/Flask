import requests


headers = {
}
# r = requests.get('https://www.baidu.com')

r = requests.get('http://127.0.0.1:5000/login', auth=HTTPBasicAuth('xiaoming', '123456'))

print(r.text)
