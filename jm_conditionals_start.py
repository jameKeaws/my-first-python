def main():
    x,y = 1, 1
    
    # result = "x is less than y" if x < y  else "x is greater than or equal to y"
    # print(result)
    
    # This is a lesson about conditionals
    # if x < y:
    #     result = "x is less than y"
    # elif x == y:
    #     result = "x is equal to y"
    # else:
    #     result = "y is less than x"
    # print(result)
    
    # match-case
    value = "three"
    
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3,4)
        case _:
            result = -1
    print(result)

main()