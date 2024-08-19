def main():
    # x = 0
    # print(f'This is our x : {x}')
    
    # while x < 5:
    #     print(x)
    #     x = x + 1
        
    # For loop
    # for x in range(5,10):
    #     print(f'For loop value of x : {x}')
    
    days = ["Mon","Tues","Wed","Thu","Fri","Sat","Sun"]
    
    # for anyDay in days:
    #     print(anyDay)
        
    for x in range(5,10):
        # if x == 7:
        #     break
        print(x)
        if x % 2 == 0:
            # continue > Skip the rest of the code and go back into the top of the loop
            continue
        print(f'Print statement after continue. loop value of x : {x}')
    
    # enumerate > returns two values index & value
    for i, d in enumerate(days):
        print(i, d)
    
main()