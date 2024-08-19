# Create temporary password using Python
import string
import secrets

# TODO: Function to return a temporary password given a length
def generate_temp_pass(num_chars=8):
    potential_chars = string.ascii_letters + string.digits + "+=?/!@#$%*"
    result = "".join(secrets.choice(potential_chars) for chars in range(num_chars))
    return result


# TODO: Function to return a temporary password and enfore 1 number and 1 uppercase
def gen_better_temp_pass(num_chars=8):
    potential_chars = string.ascii_letters + string.digits + "+=?/!@#$%*"
    while True:
        result = "".join(secrets.choice(potential_chars) for chars in range(num_chars))
        print(f'result : {result}')
        # If anyone of the character is upper case AND anyone is a digit
        if ( any(anychar.isupper() for anychar in result) and any(anychar.isdigit() for anychar in result)):
            break
    return result

# TODO Create a temporary hard to guess URL
result_url = "https://my.example.com?reset="
result_url += secrets.token_urlsafe(15)
print(result_url)

# Create a temporary password
# print(generate_temp_pass(10))

# Create a better password
# print(gen_better_temp_pass(10))