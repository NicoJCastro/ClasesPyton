
#List de diccionarios
people = [
    {"name": "Nico", "age": 25},
    {"name": "Ani", "age": 30},
    {"name": "Rita", "age": 35},
    {"name": "Nina", "age": 40},
    {"name": "Perla", "age": 45}
]

#def f(person):
    #return person["name"] si cambiamos a age ordena por edad

people.sort(key=lambda person: person["name"]) 
print(people)