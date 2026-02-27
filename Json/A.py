import json
x = '{ "name":"Ernur", "age":18, "city":"Almaty"}'
y = json.loads(x)
print(y["age"])