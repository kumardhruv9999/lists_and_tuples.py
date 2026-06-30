#Lists 
marks = [22.2, 33.8, 53.7, 92.8]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))
names = ["dhruv", 82, 55.2, "delhi"]
print(names)
print(type(names))
print(type(names[3]))

#List Slicing
marks = [22.2, 55, 66.8]
print(marks[1 : 3])

#Negative Indexing
marks = [22.2, 5.5, 66.8, 44.6, 55.8]
print(marks[-5 : -1])

#Methods of list
list = [22.2, 5.5, 66.8, 44.6, 55.8]
list.append(8)
print(list.sort())
print(list)
print(list.sort(reverse = True))      #decending order in lists
print(list)

list = ['banana', 'apple', 'guava']
list.append('mango')
print(list.sort(reverse = True))
print(list)

list = [2,5,8]
list.insert(1, 7)
print(list)

#Tuples
tup = (1, 2, 3, 4)
print(tup[0])

#Tuples methods
tup = (1, 2, 3, 4)
print(tup.index(2))

#Questions 
movies = []
movie1 = input("enter movie : ")
movie2 = input("enter movie : ")
movie3 = input("enter movie : ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)