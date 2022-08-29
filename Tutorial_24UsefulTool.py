import random

feet_in_mile = 5280
meters_in_kilometers = 1000
beatles = ["John Lemon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:] #from the . and further

def roll_dice(num):
    return random.randint(1, num)