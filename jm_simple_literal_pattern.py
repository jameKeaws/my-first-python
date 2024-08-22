# Example file for Advanced Python: Language Features by Joe Marini
# Simple pattern matching using literal values

x = None

# TODO: Literal patterns are explicit values: integers, strings, Booleans, etc
match x:
    case 0:
        print('Zer0')
    case "Zero":
        print("x is a Zero string")
    case None:
        print("Nothing")
    case 1:
        print('One')
    case _:
        print("No match or anything goes here")

        

