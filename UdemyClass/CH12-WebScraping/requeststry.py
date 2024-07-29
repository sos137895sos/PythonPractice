import requests

result = requests.get("http://www.example.com")
print(result.headers)
print(result.encoding)
print(result.cookies)
print(result.status_code)
print(type(result.text))
print("----------"*3)
print(result.text)
