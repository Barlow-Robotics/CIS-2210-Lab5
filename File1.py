
#This function converts a number in degress C into
# degrees F
def convertCtoF(c):
    f = (c * (9 / 5)) + 32
    return f


#this function prompts the user for a temperature
#and prints out the converted result
def promptAndConvert():
    inputString = input("Enter a temperature in °C: ")
    inputFloat = float(inputString)
    f = convertCtoF(inputFloat)
    print(str(inputFloat) + " is equal to " + str(f) + "°F")

print("Welcome to the Temperature Converter program.")
promptAndConvert()