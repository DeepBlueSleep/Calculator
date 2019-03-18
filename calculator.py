import re

#Just a little text guide showing all accepted commands for the user input (can be viewed again with the help command)
guide = "\n Guide\n ====================================================\n View guide: help \n Addition: sum(val1, val2, ...) \n \
Subtraction: sub(val1, val2) \n Division: div(val1, val2) \n Multiplication: mul(val1, val2, ...) \n"
print(guide)

class Calculator:

    #*args is a function that allows as many parameters to be taken as needed.
    # The important bit is the asterisk *, args is just a random variable name
    def Addition(self, *args):
        val = 0
        if (len(args) > 0):
            #For loop for each parameter entered (python for loops are weird, this one goes from 0 (default) to args length)
            for arg in args:

                #arg is a string btw so i gotta convert it to float
                val += float(arg)
                    
            return val

        else:
            return None

    #Because of how subtraction works, i can only allow 2 params (can be changed in the future)
    def Subtraction(self, a, b):
        if ((a is not None) and (b is not None)):
            val = float(a) - float(b)
            return val

        else:
            return None

    #Same deal with subtraction, only 2 params
    def Division(self, a, b):
        if ((a is not None) and (b is not None)):
            val = float(a)/float(b)
            return val

        else:
            return None

    #Same deal with addition, *args is key
    def Multiplication(self, *args):
        val = float(args[0])

        if (len(args) > 0):

            #Since in multiplication, anything * 0 = 0, val has to be set the the first arg entered,
            # and the subsequent ones multiplying with it in a for loop
            for arg in range(1, len(args)):
                val *= float(args[arg])
                    
            return val

        else:
            return None

#try and while True to constantly reset the inputs after each calculation is done
try:
    while True:
        #input() takes in user inputs, but the code runner must be set to run in terminal
        userInput = input(" Enter an command: ")

        #This is weird, so re.search is used to retrieve a substring between two characters '(' and ')',
        #which is what '\(([^)]+)' is for, it does this for every user input entered.
        result = re.search('\(([^)]+)', userInput)

        if (result is not None):

            #Separating the parameters from each other by ', ' (kinda specific)
            value = result.group(1).split(",")

            #since value is a list, values is also a list meant to store the parameters after filtering out non-numeric characters
            values = []

            #for loop to filter out each individual parameter of non-numeric characters and append it to the 'values' list
            # (if done outside of a for loop would just concatenate the parameters together)
            for v in value:
                values.append(re.sub(r'[^\d.]+', '', str(v)))
        else:
            pass

        #If the user asks for help the string at line 4 is printed again
        if(userInput.startswith("help")):
            print(guide)

        #Remaining statements enter the parameters into their respective methods based of a prefix command and prints the results
        elif(userInput.startswith("sum")):
            final = str(Calculator().Addition(*values))
            print('\n ' + final + '\n')

        elif(userInput.startswith("sub")):
            final = str(Calculator().Subtraction(values[0], values[1]))
            print('\n ' + final + '\n')

        elif(userInput.startswith("div")):
            final = str(Calculator().Division(values[0], values[1]))
            print('\n ' + final + '\n')

        elif(userInput.startswith("mul")):
            final = str(Calculator().Multiplication(*values))
            print('\n ' + final + '\n')

        else:
            print("\n Please enter a valid command\n")

#Keyboard interrupt to stop the program if CTRL-C is pressed
except KeyboardInterrupt:
    pass
