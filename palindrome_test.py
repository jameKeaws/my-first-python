def is_palindrome(teststr):
    # Your code goes here.
    
    temp_str = teststr.lower()
    print(temp_str)
    
    # Strip all punctuations and spaces from temp_str
    new_str = ''
    for any_char in temp_str:
        if any_char.isalnum():
            new_str += any_char
            print(f'new_str as it grows {new_str}')
            
    orig_list = list(new_str)
    print(orig_list)
    
    list_len = len(orig_list)
    print(list_len)
    
    reversed_list = orig_list[::-1]
    print(reversed_list)
    
    for ind,value in enumerate(orig_list):
        print(ind,value)
        
    x = 0
    is_palindrome = True
    while x < list_len:
        print('Start evaluating')
        if orig_list[x] == reversed_list[x]:
            print('Still equal')
        else:
            is_palindrome = False
            break
        x = x + 1
        print(f'We incremented x by 1.  Current value is {x}')
        
    print(f'new_str {new_str} is_palindrome value is {is_palindrome}') 

is_palindrome("maddam")