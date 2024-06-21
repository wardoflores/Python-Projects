""" To get something, one must first have an empty bowl """


# TODO: Add @property decorators.


# TODO: make the classes interact with each other through class
# TODO:  methods called by the user.
# I think I utilized the class function definition wrong,
# the classes need to be coded closer to textbook definition.


# TODO: DEFINE A CLASS AND USE IT'S PARAmETERS AS DEFINITION
# TODO:  OF THE RESULTS OF THE INPUT RESULTS FUNCTION.
# mandatory for properly utilizing the defined classes.


# TODO: Utilize function parameter *args.
# TO do with relative issues.


# TODO: Apply Dunder method to the classes.
# Still reading up on it.


# TODO: Use string format() method for easier applicaton of concept.
# To choose between file modification.


# TODO: Ponder if using a for loop for appending on a new 'result'
# TODO:  list is better than other methods.
# Still reading up on it.


# TODO: Apply nonlocal modifier.
# Just a reminder, not mandatory.


# TODO: Use Getter and setter property method decorators, also just
# TODO:  property in general for the ClassObjects.
# To do with other relative issues.


# TODO: make the state of the variables/classes "water" and "bowl"
# TODO:  as str in order for them to be easily iterable.
# Waiting for the global variables to be defined more clearly.


# TODO: Use regex for defining the functions of adding or removing
# TODO:  water.
# To do with other relative issues.


# TODO: maybe tinker with the global variables inside of the functions
# TODO:  and set some into a local variable.
# Reminder, not mandatory.


# TODO: USE ASYNC FUNCTIONS!!! maybe if I could figure out how
# TODO:  to continuously run the script after the userinput.
# mandatory, for the water and bowl to maintain its state
# after userinput is given.


# TODO: Use a text file for The dialogue.
# Reminder, slightly mandatory if the alternative of using async
# functions doesn't work.


## TODO: Use list referencing.
# To do with other relative issues.


## TODO: Add boolean in or not in for list method of data handling.

# TODO: Contemplate whether to use an empty list as the result and
# TODO:  to modify the functions towards appending what string appears.
# TODO:  And maybe even a text file for dialogue.
# Third alternative method with similarity to the second,
# use the discord bot code for inspiration on manipulating text files.


# TODO: Compress code into shorthand.
# Do this for clean-up/practice when hopefully all of this works.

# Tinker with code occasionally with new knowledge to implement,
#  Don't think that this is a one-time project.


# Variables



# Classes

class Bowl:
    

    def __init__(self, ):
        pass

    def pour(self):

        pass

    def empty(self):
        pass


class BowlObject(Bowl):

    pass


class WaterObject(Bowl):

    pass


user_data = str(input('''\"Choose a Command, entering other data unlike the choices provided results in an error.\" \n
 [A] - pour water \n
 [B] - empty water \n
 [C] - display list of responses: '''))


def userinput(): # Use while loop and store all choices in a dict maybe?
    
    if user_data == 'A':
        pass
    elif user_data == 'B':
        pass
    elif user_data == 'C':
        pass
    elif user_data == 'D':
     exit()
    else:
     print("No such command")
'''
while True:

    try:
        conversation = userinput()
        print(conversation)

    except(KeyboardInterrupt, EOFError, SystemExit):
            break
'''

# end of code.
