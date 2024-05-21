import json
# import os
# os..listdir()
book = {}
book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 98989898
}

book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': 23424234
}

s = json.dumps(book)
print(s)

with open("/BasicPython\\test.txt", "w") as f:
    f.write(s)

print("File content :- ")
f = open("/BasicPython\\test.txt", 'r')
s = f.read()
print(s)