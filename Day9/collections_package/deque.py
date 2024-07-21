from collections import deque

deque_list = deque(["London", "Berlin", "Paris", "Madrid", "Rome", "Moscow"])


#The list must have the ability to incorporate elements from the left, and be named cities_list.

cities_list = deque(["London", "Berlin", "Paris", "Madrid", "Rome", "Moscow"])
print(cities_list)
cities_list.appendleft("Athens")
print(cities_list)
cities_list.append("Istanbul")
print(cities_list)
cities_list.popleft()
print(cities_list)
cities_list.pop()
print(cities_list)
cities_list.insert(2, "Lisbon")
print(cities_list) #deque(['London', 'Berlin', 'Lisbon', 'Paris', 'Madrid', 'Rome', 'Moscow'])