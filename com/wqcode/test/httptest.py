import requests
import urllib3


a = 1
b = 2
c = a + b
print(c)

http = urllib3.PoolManager()

r = http.request('GET', 'http://www.baidu.com')
print(r.status)
# print(r.data)

