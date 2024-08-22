def calc_order_price(order_contents):
    # set the initial variables for the totals
    total_price = 0.0

    # Your code to calculate the total price goes here
    for order in order_contents:
        match order:
            case str(), str(), bool(), bool():
                print(f"Dry Cleaning")
                # dry_clean_price = 12.95
                starch_cost = 0.0
                same_day_cost = 0.0
                starched = order[2]
                same_day = order[3]
                if starched == True:
                    starch_cost = 2.0
                if same_day == True:
                    same_day_cost = 10.00
                dry_clean_price = 12.95 + starch_cost + same_day_cost
                total_price = total_price + dry_clean_price
            case str(), float():
                print(f"Wash and Fold")
                weight = order[1]
                wash_fold_price = 4.95
                if weight > 15.0:
                    wash_fold_price = (wash_fold_price * weight) - (wash_fold_price * weight * 0.1)
                else:
                    wash_fold_price = wash_fold_price * weight
                total_price = total_price + wash_fold_price
            case str(), bool(), str():
                print(f"Blankets")
                blankets_price = 25.00
                dry_clean = order[1]
                if dry_clean == True:
                    blankets_price = blankets_price + 5.0
                total_price = total_price + blankets_price      
            case _:
                print(f"Invalid item format")

    # then return the result rounded to 2 places
    return round(total_price,2)

test_order = [
    ["shirt", "L", True, False],
    ["pants", "M", False, True],
    ["dress", "M", False, True],
    ["cover", True, "L"],
    ["whites", 5.25],
    ["darks", 12.5],
    ["pants", "S", False, False],
    ["jacket", "L", False, True],
    ["shirts and jeans", 28.0],
    ["comforter", False, "L"],
    ["shirt", "L", True, True]
]

result = calc_order_price(test_order)
print(result)