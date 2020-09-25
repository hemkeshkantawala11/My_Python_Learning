import math
#import Tkinter
#top = Tkinter.Tk()
# Code to add widgets will go here...

def add(x, y):
    """This function adds two numbers"""
    return x + y


def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y


def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y


def divide(x, y):
    """This function divides two numbers"""
    return x / y


def square_root(x):
    """This Function Gives The Square Root Of The Number"""
    return math.sqrt(x)


def square_of_a_number(x):
    """This Function Gives The Square Of A number"""
    return x * x


def factorial(x):
    """This Function Gives The Factorial Of A Number"""
    return math.factorial(x)


def sum_of_the_numbers_before_the_number_you_entered(x):
    """This Function Gives The Sum Of All The Numbers Before The Number Which You Have Entered """
    return math.fsum(range(x))


def logarithm(x, y):
    """This Function Helps In Performing Logarithm"""
    return math.log(x, y)


def MOD(x):
    """This Function Gives The Nearest Number OR It Rounds The Entered Number """
    return math.modf(x)


def HCF(x, y):
    """This Function Gives The HCF Of The Entered Two Numbers """
    return math.gcd(x, y)

def COPYsign(x,y):
    """math.copysign(x, y) function return a float with the magnitude (absolute value) of x but the sign of y."""
    return math.copysign(x,y)

def SI_units(val,unit_in,unit_out):
    #This function is used in conversion, to reduce the number of if-elif-else statements.
    return val * SI[unit_in] / SI[unit_out]

# take input from the user
while True:
    enter_the_function = input("enter the function which you want to perform (CONVERTER:C AND OPERATIONS:O) and enter 'quit' to exit :- ")
    if enter_the_function=="O":
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Performing Logarithm")
        print("6.HCF")
        print("7.square root")
        print("8.square of a number")
        print("9.factorial")
        print("10.sum of the numbers before the number you entered")
        print("11.MOD")
        print("12.Copysign")

        choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12) or press q to quit:")

        if choice == "q":
            break
        global num1, num2
        if choice <= '6' and choice != '5' and choice != '11' and choice != "12":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        elif choice == '5':
            num1 = int(input("Enter the numeric number: "))
            num2 = int(input("Enter the base: "))
        elif choice == '11'  :
            num1 = float(input("Enter the numeric number: "))
        elif choice =="12":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
       
        elif choice < '11' or choice > '6' or choice =='8':
            num1 = int(input("Enter first number: "))
        elif choice > "12":
            print("Invalid input!!!! \n PLEASE ENTER THE CORRECT NUMBER OF THE CHOICE GIVEN.!!! \n PLEASE TRY AGAIN!!! \n THANKYOU....")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == "5":
            print("The Answer Is:- ", logarithm(num1, num2))

        elif choice == "6":
            print("The HCF Of ", num1,"and", num2, "is :- ", HCF(num1, num2))

        elif choice == "7":
            print("The Square Root Of", num1, "Is:- ", square_root(num1))

        elif choice == "8":
            print("The Square Of", num1, "Is :- ", square_of_a_number(num1))

        elif choice == "9":
            print("The Factorial Of", num1, "Is:- ", factorial(num1))

        elif choice == "10":
            print("The Sum Of The Numbers Before", num1, "is:- ", sum_of_the_numbers_before_the_number_you_entered(num1))

        elif choice == "11":
            print("The Answer Is:- ", MOD(num1))

        elif choice == "12":
            print("The Copysign of",num1,"and",num2,"is :- ", COPYsign(num1,num2))
    if enter_the_function=="quit":
        break

    if enter_the_function=="C":
        type_of_conversion=input("Enter The Type Of Conversion(L: LENGTH, V:VOLUME, WM: WEIGHT AND MASS, A: AREA, T:TEMPERATURE, E: ENERGY) :- ")
        if type_of_conversion=="V":
            print("mililiter= ml")
            print("gallons= G")
            print("liters= l")
            SI = {'ml': 0.001, 'l': 1, 'G':4.5}
            b = input("Enter The unit From Which You Want To Convert:- ")
            c = input("Enter The unit To Which You Want To Convert The Number To :- ")
            a = int(input("Enter The Number Which You Want To Convert:- "))
            a = SI_units(a, b, c)
            print(b,"in", c,  "is", a)



        elif type_of_conversion=="L":
            print("millimeters:mm \n centimeters:cm \n meters:m \n kilometers:km \n nanometers:nm \n feet:f \n yards:y \n Miles:mi \n inches:i")

            SI = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000.0, 'nm':0.000000001,'f':0.3048, 'y':0.9144, 'mi':1609.34, 'i':0.0254}

            b = int(input("Enter The Number Which You Want To Convert:- "))
            c = input("Unit from:- ")
            d = input('Unit to:- ')
            a = SI_units(float(b), c, d)
            print(b,c,"in",d,"is",a)

        elif type_of_conversion=="WM":
            print("carats:C \n milligrams:mg \n centigrams:cg \n decigrams:dg \n grams:G \n decagrams:Dg \n hectograms:Hg \n killograms:Kg \n tonnes:T \n pounds:P")
            SI = {'C': 0.2, 'mg': 0.001, 'cg': 0.01, 'dg': 0.1, 'G': 1.0, 'Dg': 10.0, 'Hg': 100, 'Kg': 1000, 'T': 1000000, 'P':453.592}
            b = int(input("Enter The Number Which You Want To Convert:- "))
            c = input("Unit from:- ")
            d = input('Unit to:- ')
            a = SI_units(float(b), c, d)
            print(b,c,"in",d,"is",a)

        elif type_of_conversion=="A":
            print("square milimeters: sqmm \n square centimeters:sqcm \n square meters: sqm \n hectares: H \n square kilometers: sqkm \n square inches: sqi \n square feet: sqf \n square yards: sqy \n acres:A")
            SI = {'sqmm': 0.000001, 'sqcm': 0.0001, 'sqm': 1, 'H': 10000.00, 'sqkm': 1000000.00, 'sqi': 0.000645, 'sqf': 0.092903, 'sqy': 0.836127,'A': 4046.856}
            b = int(input("Enter The Number Which You Want To Convert:- "))
            c = input("Unit from:- ")
            d = input('Unit to:- ')
            a = SI_units(float(b), c, d)
            print(b,c,"in",d,"is",a)

        elif type_of_conversion == "T":
            print("celsius:C \n farenhite:F \n kelvin:K")
            c = input("Unit from (Only WRITE in capital letters and only the units given ABOVE) :-")
            d = input('Unit to (Only WRITE in capital letters and only the units given ABOVE):- ')
            if c=="C" and d=="F":
                celsius = float(input("Enter temperature in celsius: "))
                fahrenheit = (celsius * 9 / 5) + 32
                print('%.2f Celsius is: %0.2f Fahrenheit' % (celsius, fahrenheit))

            elif c=="F" and d=="C":
                fahrenheit = float(input("Enter temperature in fahrenheit: "))
                celsius = (fahrenheit - 32) * 5 / 9
                print('%.2f Fahrenheit is: %0.2f Celsius' % (fahrenheit, celsius))

            elif c=="C" and d=="K":
                celsius=float(input("Enter Temperature in celsius:- "))
                print(celsius+273.15,"k")

            elif c=="K" and d=="C":
                kelvin=int(input("Enter The Temperature in Kelvin:- "))
                print(kelvin-273.15,"C")

            elif c=="F" and d=="K":
                fahrenheit=float(input("Enter The Temperature In Farenhite:- "))
                Kelvin = (fahrenheit-32) * 5 / 9 + 273.15
                print(Kelvin)

            elif c=="K" and d=="F":
                Kelvin=float(input("Enter The Temperature In Kelvin:- "))
                farenhite= (Kelvin - 273.15) * 9 / 5 + 32
                print(farenhite)
            else:
                print("Enter The Correct unit\nOR\nUNDER DEVELOPMENT")

        elif type_of_conversion == "E":
            print("joules:J\nkilojoules:KJ\nthermal_calories:TC\nfood_calories:FC ")
            SI = {'J': 1, 'KJ': 1000, 'TC': 4.184, 'FC': 4184}
            c = input("Unit from:- (Only WRITE in capital letters and only the units given ABOVE)")
            d = input('Unit to:- (Only WRITE in capital letters and only the units given ABOVE)')
            b = int(input("Enter The Number Which You Want To Convert:- "))
            a = SI_units(float(b), c, d)
            print(b,c,"in",d,"is",a)


#top.mainloop()
