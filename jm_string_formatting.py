from string import Template
import datetime

# TODO Using template string
the_str = "The quick brown $animal $action over the lazy dog"
the_template = Template(the_str)
output_str = the_template.substitute(animal="fox", action="jumped")
print(output_str)
args = {
    "animal": "DRAGON",
    "action" : "FLEW"
}
output_str = the_template.substitute(args)
print(output_str)

# TODO Using str.format()
foo = "foo"
bar = 123
print("Output : {} {}".format(foo, bar))
print("Output : {1} {0}".format(foo, bar))
print("Output : {var1} {var2}".format(var1=foo, var2=bar))
# Formatting directive x is lowercase hexidecimal X is uppercase hexadecimal
print("Output : {var2:x} {var2:X} {var1}".format(var1=foo, var2=bar))

# TODO Using interpolation with f-strings in Python 3.6
product = "Widget"
price = 19.99
tax = 0.07
nyeve = datetime.datetime(2024,1,1)
print(f"{product} has a price of {price}, with tax {tax:.2%}.  The total is {round((price + price*tax),2)}")
print(f"But only on {nyeve:%B %d %Y}")