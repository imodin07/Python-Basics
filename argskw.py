# Arbitrary Argument

# Args and Kwargs Keyword in Python.

""" If we don not know how many arguments that will be passed into your function,
    add * before the parameter name in the function definition. """


# *args function

def firstargs(*args):  # function definition
    print(args[0])  # Position of item in list
    print(type(args))  # *args always belongs to tuple class.


number = ["one", "two", "three"]

firstargs(*number)


# Example number 02

def brand_name(name, *args):
    for item in args:
        print(item)
        print(name)


brandname = ("Bajaj", "KTM", "TVS", "Royal Enfield", "Yamaha", "Honda", "Hero")
name = "These are the motorcycle brands in India."

brand_name(name, brandname)

''' So basically args keyword is useful when you have a large dataset and 
you don't know how many arguments you have to pass. '''

# Arbitrary Keyword Arguments

# *kwargs function

''' If we don't know how many 'Keyword arguments' are passed in function then 
put ** before the parameter name in the function. '''


def brand_name(name, *argsbike, **kwargsspecs):
    print(name)

    for item in argsbike:
        print(item)

    for key, value in kwargsspecs.items():
        print(f"\n{key} produces {value}.")


brandname = ("Bajaj", "KTM", "TVS", "Royal Enfield", "Yamaha", "Honda", "Hero")
name = "These are the motorcycle brands in India."
specs = {"Bajaj": "Pulsar", "KTM": "Duke", "TVS": "Apache", "Royal Enfield": "GT", "Yamaha": "R15", "Honda": "CBR",
         "Hero": "Xpulse", "Harley Davidson": "Fatbob"}
brand_name(name, *brandname, **specs)

