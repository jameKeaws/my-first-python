import pickle

def save_dict_via_pickle(dict_to_save, file_path):
    with open(file_path, 'wb') as dict_file:
        pickle.dump(dict_to_save, dict_file)
        
def load_dict_via_pickle(file_path):
    with open(file_path, 'rb') as dict_file:
        return pickle.load(dict_file)


my_dict = {"Daddy" : "Jayson",
           "Mommy" : "Jane",
           "Baby" : "Noah",
           "Pet" : "5K"}

my_file_path = "dict_file.txt"

save_dict_via_pickle(my_dict, my_file_path)

print(load_dict_via_pickle("dict_file.txt"))