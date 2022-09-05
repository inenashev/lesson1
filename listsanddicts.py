l = [3, 5, 7, 9, 10.5]
print(l)
l.append('Python')
print(len(l))
print(l[0])
print(l[-1])
print(l[1:4])
l.remove("Python")


d =  {"city": "Москва", "temperature": "20"}
print(d['city'])

d['temperature'] = 5

print(d)
print(d.get("country"))
print(d.get("country","Россия"))
d['date']= "27.05.2019"
print(len(d))
