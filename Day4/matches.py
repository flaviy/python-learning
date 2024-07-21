series = "N-02"

if series == "N-01":
    print("India vs England")
elif series == "N-02":
    print("India vs Australia")
elif series == "N-03":
    print("India vs South Africa")
else:
    print("No matches available")

# rewrite with match

match series:
    case "N-01":
        print("India vs England")
    case "N-02":
        print("India vs Australia")
    case "N-03":
        print("India vs South Africa")
    case _:
        print("No matches available")

client = {'name': 'John', 'age': 26, 'city': 'New York'}
movie = {'name': 'The Dark Knight', 'year': 2008, 'rating': 9.0,
         'credits': {'director': 'Christopher Nolan', 'writer': 'Christopher Nolan',
                     'cast': ['Christian Bale', 'Heath Ledger', 'Aaron Eckhart']}}
items = [client, movie, 'book']
for i in items:
    match i:
        case {'name': name, 'age': age, 'city': city}:
            print("It is a client")
            print(f"Client: {name} is {age} years old and lives in {city}")
        case {'name': name, 'year': year, 'rating': rating, 'credits': {'director': director, 'cast': cast}}:
            print("It is a movie")
            print(f"Movie: {name} was released in {year} with a rating of {rating}")
            print(f"Director: {director}")
            print(f"Cast: {cast}")
        case _:
            print("I don't know what it is")