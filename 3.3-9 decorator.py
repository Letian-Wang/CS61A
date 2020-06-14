'''----------------------------------- Basic understanding --------------------------'''
# decorate a function with another function， add more functionality, then return the function with same name
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")

# is equivalent to

def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)        



'''------------------------------- General definition of decorator --------------------------'''
def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner


'''--------------------------------------- chain decorator -----------------------------------'''
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("Hello")
# is equivalent to
def printer(msg):
    print(msg)
printer = star(percent(printer))


''' --------------------------------------- @Property ------------------------------------------'''
# 1. Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature
    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

# create an object
human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
coldest_thing = Celsius(-300)

# 2. using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)


human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
human.temperature = -300