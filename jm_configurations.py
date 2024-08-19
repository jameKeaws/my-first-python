import configparser

# TODO Create the configuration parser
con_parser = configparser.ConfigParser()

# TODO Read the configuration file
con_parser.read("config.cfg")

# TODO Print the sections.  Just prints out the non default sections
# print(con_parser.sections())
# print(con_parser.has_section("Section 1"))

# TODO Access one of the default values
# using_time_travel = bool( con_parser['DEFAULT']['UseTimeTravel'] )
# print(using_time_travel)
# print(type(using_time_travel))
# ship_speed = con_parser['DEFAULT']['Ship Speed']
# print(ship_speed)

# TODO Demonstrate one of the getXXX convenience functions
# opd = con_parser['DEFAULT'].getboolean("ObeyPrimeDirective")
# print(f'opd: {opd}')
# print(f'type(opd): {type(opd)}')

# speed = con_parser['DEFAULT'].getfloat("Ship Speed")
# print(f'speed: {speed}')
# print(f'type(speed): {type(speed)}')


# TODO Access a non-existent value
try: 
    title = con_parser['SECTION 3']['title']
    print(title)
except KeyError as err:
    print(err)