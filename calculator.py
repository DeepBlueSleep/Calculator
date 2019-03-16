import re

guide = "\n Guide\n ====================================================\n View guide: help \n Addition: sum(val1, val2, ...) \n \
Subtraction: sub(val1, val2) \n Division: div(val1, val2) \n Multiplication: mul(val1, val2, ...) \n"
print(guide)

try:
    while True:
        class Calculator:

            def Addition(self, *args):
                val = 0
                if (len(args) > 0):
                    for arg in args:
                        val += float(arg)
                    
                    return val

                else:
                    return None

            def Subtraction(self, a, b):
                if ((a is not None) and (b is not None)):
                    val = float(a) - float(b)
                    return val

                else:
                    return None

            def Division(self, a, b):
                if ((a is not None) and (b is not None)):
                    val = float(a)/float(b)
                    return val

                else:
                    return None

            def Multiplication(self, *args):
                val = float(args[0])

                if (len(args) > 0):
                    for arg in range(1, len(args)):
                        val *= float(args[arg])
                    
                    return val

                else:
                    return None

        userInput = input(" Enter an command: ")
        result = re.search('\(([^)]+)', userInput)
        if (result is not None):
            values = result.group(1).split(", ")
        else:
            pass

        if(userInput.startswith("help")):
            print(guide)

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

except KeyboardInterrupt:
    pass