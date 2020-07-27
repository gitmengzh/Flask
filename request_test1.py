import requests


headers = {
}
# r = requests.get('https://www.baidu.com')

# r = requests.get('http://127.0.0.1:5000/login', auth=('xiaoming', '123456'))

#print(r.text)

token1 = 'eGlhb21pbmc6MC45OTExOTIzNzIxMzM3ODAxOjE1OTU3ODY3NDMuMjc1NjQ2'
r1 = requests.get('http://127.0.0.1:5000/test1', params={'token' : token1})
print(r1.text)

