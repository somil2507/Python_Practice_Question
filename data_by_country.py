people = [
    {"name": "Alice", "age": 30, "country": "USA"},
    {"name": "Bob", "age": 25, "country": "Canada"},
    {"name": "Charlie", "age": 35, "country": "USA"},
    {"name": "David", "age": 28, "country": "Canada"},
    {"name": "Eve", "age": 32, "country": "France"}
]

d = {}

for i in people:
    country = i["country"]
    if country not in people:
        d[country] = []
    d[country].append(i) 

print(d)

