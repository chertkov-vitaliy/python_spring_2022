#https://docs.python.org/3/library/http.client.html#examples
# Источник: https://pythonim.ru/moduli/http-python

import http.client
import pprint

# import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
# Получить ответ сервера
response = conn.getresponse()
# Получить заголовки сервера
headers = response.getheaders()

print(response.status, response.reason)

data1 = response.read()  # This will return entire content.
# The following example demonstrates reading data in chunks.
conn.request("GET", "/")
response = conn.getresponse()
while chunk := response.read(200):
    print(repr(chunk))

conn = http.client.HTTPSConnection("docs.python.org")
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()
print(r2.status, r2.reason)

data2 = r2.read()
conn.close()