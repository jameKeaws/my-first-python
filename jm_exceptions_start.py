

# try:
#     x = 10 / 0
# except Exception as e:
#     print(type(e).__name__)
#     print(e)
# finally:
#     print('We executed the finally part')

try:
    answer = input("What should I divide 10 by?")
    num = int(answer)
    print(10/num)
except ValueError as ve:
    print(type(ve).__name__)
    print(ve)
except ZeroDivisionError as zde:
    print(type(zde).__name__)
    print(zde)
except Exception as e:
    print(type(e).__name__)
    print(e)
finally:
    print('We have reached the finally clause')