language = {
    "name" : "Python",
    "version" : 3,
    "creator": "Guido van Rossum"
}

language["website"] = "python.org"
language["extension"] = ".py"

# print(language)

# file_extension = language.get("extension")
# print(f"file_extension using language.get('extension') : {file_extension}")
# print("\n")
# if "extension" in language:
#     print("extension key is in language dictionary")
#     print(language["extension"])
    
favorite_movie ={
    "title" : "Jurassic Park 3",
    "release year" : 2001,
    "director" : "Joe Johnston",
    "genre" : "Science Fiction, Action, Adventure",
    "lead actors" : ["Sam Neill", "Tea Leoni", "Michael Jeter"],
}

# Get the dictionary keys
the_dic_keys = favorite_movie.keys()
print("The dictionary keys are : ")
print(the_dic_keys)

# Get the dictionary values
the_dic_values = favorite_movie.values()
print("\n")
print("The dictionary values are : ")
print(the_dic_values)

the_dict_items = favorite_movie.items()
print("\n")
print("The dictionary items are : ")
print(the_dict_items)

print("\n")
for k in favorite_movie:
    print(k)
    print(favorite_movie[k])