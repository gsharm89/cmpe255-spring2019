from operator import itemgetter

users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    index=0;
    for item in friendship:
        if user in item: index+=1;
    return index
    pass

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    #sorted list with user and their number of friends
    name_with_friends=[(user["name"], num_friends(user["id"])) for user in users]
    name_with_friends.sort(key=itemgetter(1), reverse=True)
    
    #Output the sorted list
    for x in range(0,10):
        print(name_with_friends[x][0], "has", name_with_friends[x][1], "friends."),
    pass

#Output list of names and their number of friends.
for x in range(0,10):
    print(users[x]["name"], "has", num_friends(x), "friends."),
    
print("\nThis is the output after the sort function.\n");

#Sort function and display the sorted list
sort_by_num_friends();

