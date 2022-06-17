from pprint import pprint
import string





my_range = range(1, 21)
print([x*10 for x in my_range]) #List comprehension


print(list(map(str, my_range))) #map function


a = ["1", 1, "1", 2]
a = list(set(a)) #set function
print(a)


dic = {'a':1,'b':2, 'c':3}
print(sum(dic.values())) #sum function


d = dict((key, value) for key, value in dic.items() if value <= 1) #dict comprehension
print(d)


x = dict(a=list(range(1,11)),b=list(range(11,21)),c=list(range(21,31)))
pprint(x) # Importar modulo "from pprint import pprint"


d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
print(d['b'][2])

for i,z in d.items():
    print('{} has a value {}'.format(i,z))


for letter in string.ascii_lowercase: #Modulo importado string
    print(letter)

print(string.ascii_lowercase)
