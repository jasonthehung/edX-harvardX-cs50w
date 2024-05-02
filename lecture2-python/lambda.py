people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]


# def f(person):
#     return person["name"]


# people.sort(key=f)

# lambda function is an anonymous function
people.sort(key=lambda person: person["name"])

print(people)