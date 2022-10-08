"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm


# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"


@hops.component(
    "/binmult",
    inputs=[hs.HopsNumber("A"), hs.HopsNumber("B")],
    outputs=[hs.HopsNumber("Multiply")],
)
def BinaryMultiply(a: float, b: float):
    return a * b


@hops.component(
    "/add",
    name="Add",
    nickname="Add",
    description="Add numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Sum", "S", "A + B")]
)
def add(a: float, b: float):
    return a + b


@hops.component(
    "/pointat",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)


@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def ruled_surface(a: rhino3dm.Point3d,
                  b: rhino3dm.Point3d,
                  c: rhino3dm.Point3d,
                  d: rhino3dm.Point3d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)



"""
AUTOMATINC THE BRING STUFF WITH PYTHON
Moving and renaming thousands of files and sorting them into folders
Filling out online forms—no typing required
Downloading files or copying text from a website whenever it updates
Having your computer text you custom notifications
Updating or formatting Excel spreadsheets
Checking your email
and sending out prewritten responses

██╗███╗   ██╗████████╗██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██║████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║
██║██║ ╚████║   ██║   ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""

print('Hello, world!')
@hops.component(
    "/hello",
    name="Hello",
    nickname="Hello",
    description="Hello world",
    inputs=[hs.HopsString("Name", "N", "Name to say hello to"),],
    outputs=[hs.HopsString("Hello", "H", "Hello world")]
)
def hello(name: str):
    print (name)
    return f"Hello {name}"

"""
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                     
██████╗  █████╗ ███████╗██╗ ██████╗███████╗          
██╔══██╗██╔══██╗██╔════╝██║██╔════╝██╔════╝          
██████╔╝███████║███████╗██║██║     ███████╗          
██╔══██╗██╔══██║╚════██║██║██║     ╚════██║          
██████╔╝██║  ██║███████║██║╚██████╗███████║          
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝╚══════╝  
"""
# Python Basics
# interactive shell
#REPL (read-eval-print loop)
# run or execute a script
# variables
# data types
# strings, numbers, booleans, lists, dictionaries
@hops.component(
    "/integer",
    name="Integer",
    nickname="Integer",
    description="Integer",
    inputs=[hs.HopsInteger("Number", "N", "Number")],
    outputs=[hs.HopsInteger("Number", "N", "Number")]
)
def integer(number: int):
    return number

@hops.component(
    "/number",
    name="Number",
    nickname="Number",
    description="Number",
    inputs=[hs.HopsNumber("Number", "N", "Number")],
    outputs=[hs.HopsNumber("Number", "N", "Number")]
)
def number(number: float):
    return number

@hops.component(
    "/string",
    name="String",
    nickname="String",
    description="String",
    inputs=[hs.HopsString("String", "S", "String")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def string(string: str):
    return string

# string concatenation
@hops.component(
    "/concatenate",
    name="Concatenate",
    nickname="Concatenate",
    description="Concatenate",
    inputs=[
        hs.HopsString("String 1", "S1", "String 1"), 
        hs.HopsString("String 2", "S2", "String 2")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def concatenate(string1: str, string2: str):
    return string1 + string2

# casting (converting) between data types
@hops.component(
    "/cast",
    name="Cast",
    nickname="Cast",
    description="Cast",
    inputs=[hs.HopsString("String", "S", "String")],
    outputs=[hs.HopsInteger("Integer", "I", "Integer")]
)
def cast(string: str):
    return int(string)

# text and number equivalence
@hops.component(
    "/equivalence4",
    name="Equivalence",
    nickname="Equivalence",
    description="Equivalence",
    inputs=[
        hs.HopsString("String", "S", "String"), 
        hs.HopsInteger("Integer", "I", "Integer"),
        hs.HopsNumber("Number", "N", "Number")
        ],
    outputs=[hs.HopsBoolean("Boolean1", "B1", "Boolean"),
             hs.HopsBoolean("Boolean2", "B2", "Boolean"),]
)
def equivalence4(string: str, integer: int, number: float):
    return string == integer, integer == number

"""
███████╗██╗      ██████╗ ██╗    ██╗     ██████╗ ██████╗ ███╗   ██╗████████╗██████╗  ██████╗ ██╗     
██╔════╝██║     ██╔═══██╗██║    ██║    ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║     
█████╗  ██║     ██║   ██║██║ █╗ ██║    ██║     ██║   ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║     
██╔══╝  ██║     ██║   ██║██║███╗██║    ██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║     
██║     ███████╗╚██████╔╝╚███╔███╔╝    ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗
╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
"""

# flow control
# the difference between the == and = operators
# conditions
# if, elif, else
@hops.component(
    "/if",
    name="If",
    nickname="If",
    description="If",
    inputs=[hs.HopsBoolean("Boolean", "B", "Boolean")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def if_(boolean: bool):
    if boolean:
        return "True"
    else:
        return "False"

# elif
@hops.component(
    "/elif",
    name="Elif",
    nickname="Elif",
    description="Elif",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def elif_(integer: int):
    if integer == 1:
        return "One"
    elif integer == 2:
        return "Two"
    else:
        return "Other"

# else (optional)
@hops.component(
    "/else",
    name="Else",
    nickname="Else",
    description="Else",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def else_(integer: int):
    if integer == 1:
        return "One"
    elif integer == 2:
        return "Two"
    else:
        return "Other"

# fizz buzz
@hops.component(
    "/fizzbuzz",
    name="FizzBuzz",
    nickname="FizzBuzz",
    description="FizzBuzz",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

# while loop statement
@hops.component(
    "/while2",
    name="While",
    nickname="While",
    description="While",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def while_(n):
    i = 0
    _string = ""
    while i < n:
        _string += str(i)
        i += 1
    return _string

# break statement
@hops.component(
    "/break",
    name="Break",
    nickname="Break",
    description="Break",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def break_(n):
    i = 0
    _string = ""
    while i < n:
        _string += str(i)
        i += 1
        if i == 5:
            break
    return _string

# continue statement
@hops.component(
    "/continue",
    name="Continue",
    nickname="Continue",
    description="Continue",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def continue_(n):
    i = 0
    _string = ""
    while i < n:
        i += 1
        if i == 5:
            continue
        _string += str(i)
    return _string

# for loops and the range function
@hops.component(
    "/for",
    name="For",
    nickname="For",
    description="For",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def for_(n):
    _string = ""
    for i in range(n):
        _string += str(i)
    return _string

# for loops and the range function
@hops.component(
    "/range",
    name="Range",
    nickname="Range",
    description="Range",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def range_(n):
    _string = ""
    for i in range(0, n, 2):
        _string += str(i)
    return _string

# range start, stop, step
@hops.component(
    "/rangeInt",
    name="Range2",
    nickname="Range2",
    description="Range2",
    inputs=[
        hs.HopsInteger("Start", "S", "Start"),
        hs.HopsInteger("Stop", "P", "Stop"),
        hs.HopsInteger("Step", "T", "Step")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def rangeInt(start, stop, step):
    _string = ""
    for i in range(start, stop, step):
        _string += str(i)
    return _string

"""
██╗███╗   ███╗██████╗  ██████╗ ██████╗ ████████╗             
██║████╗ ████║██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝             
██║██╔████╔██║██████╔╝██║   ██║██████╔╝   ██║                
██║██║╚██╔╝██║██╔═══╝ ██║   ██║██╔══██╗   ██║                
██║██║ ╚═╝ ██║██║     ╚██████╔╝██║  ██║   ██║                
╚═╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝                
                                                             
███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗███████╗
████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗  ███████╗
██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝  ╚════██║
██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗███████║
╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝
"""
# import random, sys, os, math, datetime, re
# from import statements
# ending a program early with sys.exit() function

@hops.component(
    "/sysExit",
    name="SysExit",
    nickname="SysExit",
    description="SysExit",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def sysExit(n):
    import sys
    if n == 0:
        sys.exit()
    return "Hello World"

# a short program to guess the number
@hops.component(
    "/guessNumber3",
    name="GuessNumber",
    nickname="GuessNumber",
    description="GuessNumber",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def guessNumber3(n):
    import random
    secretNumber = random.randint(1, 3)
    print("I am thinking of a number between 1 and 3.")
    # Ask the player to guess 6 times.
    for guessesTaken in range(1):
        print("Take a guess.")
        guess = int(n)
        if guess < secretNumber:
            print("Your guess is too low.")
        elif guess > secretNumber:
            print("Your guess is too high.")
        else:
            break
    if guess == secretNumber:
        return "Good job! You guessed my number in " + str(guessesTaken) + " guesses!"
    else:
        return "Nope. The number I was thinking of was " + str(secretNumber)

""" 
███████╗██╗   ██╗███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔════╝██║   ██║████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
█████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
"""
# return values and return statements
@hops.component(
    "/returnValues",
    name="ReturnValues",
    nickname="ReturnValues",
    description="ReturnValues",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def returnValues(n):
    if n == 1:
        return "It is certain"
    elif n == 2:
        return "It is decidedly so"
    elif n == 3:
        return "Yes"
    elif n == 4:
        return "Reply hazy try again"
    elif n == 5:
        return "Ask again later"
    elif n == 6:
        return "Concentrate and ask again"
    elif n == 7:
        return "My reply is no"
    elif n == 8:
        return "Outlook not so good"
    elif n == 9:
        return "Very doubtful"
    else:
        return "Error"

# the None value
@hops.component(
    "/noneValue",
    name="NoneValue",
    nickname="NoneValue",
    description="NoneValue",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def noneValue(n):
    if n == 1:
        return "Hello"
    elif n == 2:
        return "Howdy"
    elif n == 3:
        return "Hi"
    else:
        return None

# keyword arguments and print() function
@hops.component(
    "/keywordArguments",
    name="KeywordArguments",
    nickname="KeywordArguments",
    description="KeywordArguments",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def keywordArguments(n):
    print("Hello", end=" ")
    print("World")
    print("cats", "dogs", "mice")
    print("cats", "dogs", "mice", sep=",")
    return "Hello"

# the call stack
@hops.component(
    "/callStack",
    name="CallStack",
    nickname="CallStack",
    description="CallStack",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def callStack(n):
    def a():
        print("a() starts")
        b()
        d()
        print("a() returns")
    def b():
        print("b() starts")
        c()
        print("b() returns")
    def c():
        print("c() starts")
        print("c() returns")
    def d():
        print("d() starts")
        print("d() returns")
    a()
    return "Hello"

# local and global scope
@hops.component(
    "/localGlobalScope",
    name="LocalGlobalScope",
    nickname="LocalGlobalScope",
    description="LocalGlobalScope",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
# local variables cannot be used in the global scope
def localGlobalScope(n):
    def spam():
        global eggs
        eggs = "spam"
    eggs = "global"
    spam()
    print(eggs)
    return "Hello"

# local variables cannot be used in other scopes

# local variables can be read from a local scope
@hops.component(
    "/localVariables",
    name="LocalVariables",
    nickname="LocalVariables",
    description="LocalVariables",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def localVariables(n):
    def spam():
        eggs = "spam local"
        print(eggs)
    eggs = "global"
    spam()
    print(eggs)
    return "Hello"


# local and global variables with the same name
@hops.component(    
    "/localGlobalVariables",
    name="LocalGlobalVariables",
    nickname="LocalGlobalVariables",
    description="LocalGlobalVariables",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def localGlobalVariables(n):
    def spam():
        global eggs
        eggs = "spam"
    eggs = "global"
    spam()
    print(eggs)
    return "Hello"

# The global statement
@hops.component(
    "/globalStatement",
    name="GlobalStatement",
    nickname="GlobalStatement",
    description="GlobalStatement",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def globalStatement(n):
    def spam():
        global eggs
        eggs = "spam"
    def bacon():
        eggs = "bacon"
    def ham():
        print(eggs)
    eggs = 42
    spam()
    print(eggs)
    bacon()
    print(eggs)
    ham()
    return "Hello"

    # Note: if you ever want to modify the value of a global variable from within a function, use the global statement on that variable.
    @hops.component(
        "/globalStatement",
        name="GlobalStatement",
        nickname="GlobalStatement",
        description="GlobalStatement",
        inputs=[hs.HopsInteger("Integer", "I", "Integer")],
        outputs=[hs.HopsString("String", "S", "String")]
    )
    def globalStatement(n):
        def spam():
            global eggs
            eggs = "spam"
        def bacon():
            eggs = "bacon"
        def ham():
            print(eggs)
        eggs = 42
        spam()
        print(eggs)
        bacon()
        print(eggs)
        ham()
        return "Hello"

# exception handling
# try and except statements
@hops.component(
    "/tryExcept2",
    name="TryExcept",
    nickname="TryExcept",
    description="TryExcept",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def tryExcept2(n):
    def spam(divideBy):
        try:
            return 42 / divideBy
        except ZeroDivisionError:
            print("Error: Invalid argument.")
    print(spam(n))
    return "Hello"

# a short program: zigzag
@hops.component(
    "/zigzag",
    name="Zigzag",
    nickname="Zigzag",
    description="Zigzag",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def zigzag(n):
    import time, sys
    indent = 0
    indentIncreasing = True
    try:
        while True:
            print(" " * indent, end="")
            print("********")
            time.sleep(0.1)
            if indentIncreasing:
                indent = indent + 1
                if indent == 20:
                    indentIncreasing = False
            else:
                indent = indent - 1
                if indent == 0:
                    indentIncreasing = True
    except KeyboardInterrupt:
        sys.exit()
    return "Hello"

""" 
██╗     ██╗███████╗████████╗███████╗
██║     ██║██╔════╝╚══██╔══╝██╔════╝
██║     ██║███████╗   ██║   ███████╗
██║     ██║╚════██║   ██║   ╚════██║
███████╗██║███████║   ██║   ███████║
╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝
"""
# the list data type
@hops.component(
    "/list",
    name="List",
    nickname="List",
    description="List",
    inputs=[hs.HopsInteger("Integer", "I", "Integer")],
    outputs=[hs.HopsString("String", "S", "String")]
)
def list(n):
    spam = ["cat", "bat", "rat", "elephant"]
    return spam[n]

# negative indexes
@hops.component(
    "/negativeIndexes",
    name="NegativeIndexes",
    nickname="NegativeIndexes",
    description="NegativeIndexes",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def negativeIndexes(n):
    spam = ["cat", "bat", "rat", "elephant"]
    return spam[n]

# getting a list from another list with slices
@hops.component(
    "/slice",
    name="Slice",
    nickname="Slice",
    description="Slice",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)   
def slice(n):
    spam = ["cat", "bat", "rat", "elephant"]
    return spam[n:n+3]

# getting a list's length with the len() function
@hops.component(
    "/length3",
    name="Len",
    nickname="Len",
    description="Len",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def length3(n):
    spam = ["cat", "bat", "rat", "elephant"]
    return len(spam[n:n+3])

# changing values in a list with indexes
@hops.component(
    "/changeValue",
    name="ChangeValue",
    nickname="ChangeValue",
    description="ChangeValue",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def changeValue(n):
    spam = ["cat", "bat", "rat", "elephant"]
    spam[n] = "Hello"
    return spam

# list concatenation and list replication
@hops.component(
    "/concatenation",
    name="Concatenation",
    nickname="Concatenation",
    description="Concatenation",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def concatenation(n):
    spam = [1, 2, 3]
    spam = spam + ["A", "B", "C"]
    return spam

# removing values from lists with del statements
@hops.component(
    "/del",
    name="Del",
    nickname="Del",
    description="Del",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def del2(n):
    spam = ["cat", "bat", "rat", "elephant"]
    del spam[n]
    return spam

"""
██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗              
██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝              
██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗             
██║███╗██║██║   ██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║             
╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝             
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝              
                                                                      
██╗    ██╗██╗████████╗██╗  ██╗    ██╗     ██╗███████╗████████╗███████╗
██║    ██║██║╚══██╔══╝██║  ██║    ██║     ██║██╔════╝╚══██╔══╝██╔════╝
██║ █╗ ██║██║   ██║   ███████║    ██║     ██║███████╗   ██║   ███████╗
██║███╗██║██║   ██║   ██╔══██║    ██║     ██║╚════██║   ██║   ╚════██║
╚███╔███╔╝██║   ██║   ██║  ██║    ███████╗██║███████║   ██║   ███████║
 ╚══╝╚══╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝ 
"""

# working with lists
@hops.component(
    "/append",
    name="Append",
    nickname="Append",
    description="Append",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def append(n):
    spam = ["cat", "bat", "rat", "elephant"]
    spam.append("Hello")
    return spam

# inserting values into lists with the insert() method
@hops.component(
    "/insert",
    name="Insert",
    nickname="Insert",
    description="Insert",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def insert(n):
    spam = ["cat", "bat", "rat", "elephant"]
    spam.insert(n, "Hello")
    return spam

# removing values from lists with the remove() method
@hops.component(
    "/remove",
    name="Remove",
    nickname="Remove",
    description="Remove",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)   
def remove(n):
    spam = ["cat", "bat", "rat", "elephant"]
    spam.remove(spam[n])
    return spam

# using loops with lists
@hops.component(
    "/loop",
    name="Loop",
    nickname="Loop",
    description="Loop",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def loop(n):
    spam = ["cat", "bat", "rat", "elephant"]
    for i in range(len(spam)):
        print("Index " + str(i) + " in spam is: " + spam[i])
    return spam

# the in and not in operators
@hops.component(
    "/in",
    name="In",
    nickname="In",
    description="In",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def _in(n):
    spam = ["cat", "bat", "rat", "elephant"]
    if "cat" in spam:
        answer = ("Yes")
    else:
        answer =("No")
    return answer

@hops.component(
    "/not_in",
    name="Not In",
    nickname="Not In",
    description="Not In",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def not_in(n):
    spam = ["cat", "bat", "rat", "elephant"]
    if "cat" not in spam:
        answer = ("Yes")
    else:
        answer =("No")
    return answer

# multiple assignment trick
@hops.component(
    "/multiple_assignment",
    name="Multiple Assignment",
    nickname="Multiple Assignment",
    description="Multiple Assignment",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def multiple_assignment(n):
    cat = ["fat", "black", "loud"]
    size, color, disposition = cat
    return size, color, disposition

# using the enumerate() function with lists
@hops.component(
    "/_enumerate",
    name="Enumerate",
    nickname="Enumerate",
    description="Enumerate",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def _enumerate(n):
    spam = ["cat", "bat", "rat", "elephant"]
    for i, v in enumerate(spam):
        print("Index " + str(i) + " in spam is: " + v)
    return spam

# using random.choice() to choose a value from a list
@hops.component(
    "/random_choice",
    name="Random Choice",
    nickname="Random Choice",
    description="Random Choice",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)  
def random_choice(n):
    import random
    spam = ["cat", "bat", "rat", "elephant"]
    randChoice = (random.choice(spam))
    return randChoice

# using random.shuffle() to shuffle the values in a list
#  having issues with strings and numbers

# sorting the values in a list with the sort() method
@hops.component(
    "/sorted3",
    name="Sort",
    nickname="Sort",
    description="Sort",
    inputs=[
        hs.HopsNumber("Number", "N", "Number")
    ],
    outputs=[hs.HopsNumber("sortedNumber", "SN", "Number")]
)
def sorted3(n):
    spam = [2, 5, 3.14, 1, -7]
    spam.sort()
    return spam

# reverse sorting the values in a list with the reverse() method
@hops.component(
    "/reverse",
    name="Reverse",
    nickname="Reverse",
    description="Reverse",
    inputs=[
        hs.HopsNumber("Number", "N", "Number")
    ],
    outputs=[hs.HopsNumber("sortedNumber", "SN", "Number")]
)
def reverse(n):
    spam = [2, 5, 3.14, 1, -7]
    spam.sort()
    spam.reverse()
    return spam

# magic 8 ball with lists
@hops.component(
    "/magic8ball",
    name="Magic 8 Ball",
    nickname="Magic 8 Ball",
    description="Magic 8 Ball", 
    inputs=[
        hs.HopsString("Question", "Q", "Question")
    ],
    outputs=[hs.HopsString("Answer", "A", "Answer")]
)
def magic8ball(q):
    import random
    answers = [
        "It is certain", 
        "It is decidedly so", 
        "Yes", "Reply hazy try again", 
        "Ask again later", 
        "Concentrate and ask again", 
        "My reply is no", 
        "Outlook not so good", 
        "Very doubtful"]
    randAnswer = (random.choice(answers))
    return randAnswer

# sequences data types
# tuples
@hops.component(
    "/tuples",
    name="Tuples",
    nickname="Tuples",
    description="Tuples",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def tuples(n):
    eggs = ("hello", 42, 0.5)
    return eggs[n]

# mutable and immutable data types
@hops.component(
    "/mutable",
    name="Mutable",
    nickname="Mutable",
    description="Mutable",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def mutable(n):
    spam = 42
    spam = spam + 1
    return spam

@hops.component(
    "/immutable",
    name="Immutable",
    nickname="Immutable",
    description="Immutable",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def immutable(n):
    spam = "Say Goodbye, then."
    spam[1] = "Hello"
    return spam

@hops.component(
    "/immutable3",
    name="Immutable2",
    nickname="Immutable2",
    description="Immutable2",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def immutable3(n):
    spam = "Say Goodbye, then."
    newspam = spam[0:4] + "Hello" + spam[11:]
    return newspam

# identity and the id() function
@hops.component(
    "/identity",
    name="Identity",
    nickname="Identity",
    description="Identity",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def identity(n):
    spam = 42
    eggs = spam
    print(id(spam))
    print(id(eggs))
    return spam

# passing references
@hops.component(
    "/passing_references",
    name="Passing References",
    nickname="Passing References",
    description="Passing References",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)   
def passing_references(n):
    def eggs(someParameter):
        someParameter.append("Hello")
    spam = [1, 2, 3]
    eggs(spam)
    return spam

# the copy module's copy() and deepcopy() functions
@hops.component(
    "/copy",
    name="Copy",
    nickname="Copy",
    description="Copy",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def copy(n):
    import copy
    spam = ["A", "B", "C", "D"]
    cheese = copy.copy(spam)
    cheese[1] = 42
    return cheese

@hops.component(
    "/deepcopy",
    name="Deep Copy",
    nickname="Deep Copy",
    description="Deep Copy",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def deepcopy(n):
    import copy
    spam = ["A", "B", "C", "D"]
    cheese = copy.deepcopy(spam)
    cheese[1] = 42
    return cheese



""" 
 ██████╗ ██████╗ ███╗   ██╗██╗    ██╗ █████╗ ██╗   ██╗███████╗                          
██╔════╝██╔═══██╗████╗  ██║██║    ██║██╔══██╗╚██╗ ██╔╝██╔════╝                          
██║     ██║   ██║██╔██╗ ██║██║ █╗ ██║███████║ ╚████╔╝ ███████╗                          
██║     ██║   ██║██║╚██╗██║██║███╗██║██╔══██║  ╚██╔╝  ╚════██║                          
╚██████╗╚██████╔╝██║ ╚████║╚███╔███╔╝██║  ██║   ██║   ███████║                          
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝                          
                                                                                        
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ███████╗    ██╗     ██╗███████╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██╔════╝    ██║     ██║██╔════╝██╔════╝
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║█████╗      ██║     ██║█████╗  █████╗  
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║██╔══╝      ██║     ██║██╔══╝  ██╔══╝  
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝██║         ███████╗██║██║     ███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝ ╚═╝         ╚══════╝╚═╝╚═╝     ╚══════╝
"""

# conway's game of life
@hops.component(
    "/conway",
    name="Conway's Game of Life",
    nickname="Conway's Game of Life",
    description="Conway's Game of Life",
    inputs=[
        hs.HopsInteger("Integer", "I", "Integer")
    ],
    outputs=[hs.HopsString("String", "S", "String")]
)
def conway(n):
    import random, time, copy
    WIDTH = 60
    HEIGHT = 20

    # Create a list of list for the cells:
    nextCells = []
    for x in range(WIDTH):
        column = []
        for y in range(HEIGHT):
            if random.randint(0, 1) == 0:
                column.append("#")
            else:
                column.append(" ")
        nextCells.append(column)
    while True: # Main program loop
        print("\n\n\n\n\n") # Separate each step with newlines.
        currentCells = copy.deepcopy(nextCells)
        # Print the currentCells on the screen:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                print(currentCells[x][y], end="")
            print()
        # Calculate the next step's cells based on current step's cells:
        for x in range(WIDTH):
            for y in range(HEIGHT):
                # Get neighboring coordinates:
                # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
                leftCoord = (x - 1) % WIDTH
                rightCoord = (x + 1) % WIDTH
                aboveCoord = (y - 1) % HEIGHT
                belowCoord = (y + 1) % HEIGHT

                # Count number of living neighbors:
                numNeighbors = 0
                if currentCells[leftCoord][aboveCoord] == "#":
                    numNeighbors += 1

                if currentCells[x][aboveCoord] == "#":
                    numNeighbors += 1

                if currentCells[rightCoord][aboveCoord] == "#":
                    numNeighbors += 1

                if currentCells[leftCoord][y] == "#":
                    numNeighbors += 1

                if currentCells[rightCoord][y] == "#":
                    numNeighbors += 1

                if currentCells[leftCoord][belowCoord] == "#":
                    numNeighbors += 1

                if currentCells[x][belowCoord] == "#":          
                    numNeighbors += 1

                if currentCells[rightCoord][belowCoord] == "#":     
                    numNeighbors += 1

                # Set cell based on Conway's Game of Life rules:
                if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                    # Living cells with 2 or 3 neighbors stay alive:
                    nextCells[x][y] = "#"
                elif currentCells[x][y] == " " and numNeighbors == 3:
                    # Dead cells with 3 neighbors become alive:
                    nextCells[x][y] = "#"
                else:
                    # Everything else dies or stays dead:
                    nextCells[x][y] = " "
        time.sleep(1) # Add a 1-second pause to reduce flickering.

""" 
██████╗ ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗ █████╗ ██████╗ ██╗███████╗███████╗                                          
██╔══██╗██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔══██╗██╔══██╗██║██╔════╝██╔════╝                                          
██║  ██║██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████║██████╔╝██║█████╗  ███████╗                                          
██║  ██║██║██║        ██║   ██║██║   ██║██║╚██╗██║██╔══██║██╔══██╗██║██╔══╝  ╚════██║                                          
██████╔╝██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║██║  ██║██║  ██║██║███████╗███████║                                          
╚═════╝ ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝                                          
                                                                                                                               
 █████╗ ███╗   ██╗██████╗                                                                                                      
██╔══██╗████╗  ██║██╔══██╗                                                                                                     
███████║██╔██╗ ██║██║  ██║                                                                                                     
██╔══██║██║╚██╗██║██║  ██║                                                                                                     
██║  ██║██║ ╚████║██████╔╝                                                                                                     
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝                                                                                                      
                                                                                                                               
███████╗████████╗██████╗ ██╗   ██╗ ██████╗████████╗██╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ██████╗  █████╗ ████████╗ █████╗ 
██╔════╝╚══██╔══╝██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║████╗  ██║██╔════╝     ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
███████╗   ██║   ██████╔╝██║   ██║██║        ██║   ██║   ██║██████╔╝██║██╔██╗ ██║██║  ███╗    ██║  ██║███████║   ██║   ███████║
╚════██║   ██║   ██╔══██╗██║   ██║██║        ██║   ██║   ██║██╔══██╗██║██║╚██╗██║██║   ██║    ██║  ██║██╔══██║   ██║   ██╔══██║
███████║   ██║   ██║  ██║╚██████╔╝╚██████╗   ██║   ╚██████╔╝██║  ██║██║██║ ╚████║╚██████╔╝    ██████╔╝██║  ██║   ██║   ██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
"""

# the dictionary data type is a mutable data type
@hops.component(
    "/dictionary",
    name="Dictionary",
    description="A dictionary is a mutable data type that stores mappings of unique keys to values.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")   
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def dictionary(integer):
    # create a dictionary
    myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
    # get the value of a key
    return myCat['size']

# dictionaries vs. lists
# dictionaries are unordered
# dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys
# lists are ordered
# lists are indexed by their position in the list, starting at 0

# the keys() and values() and items() methods
# cannot modify the dictionary while iterating over it
# can be used in for loops
@hops.component(
    "/_values4",
    name="Values",
    description="The values() method returns a list of all the values in the dictionary.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _values4(integer):
    spam = {'color': 'red', 'age': 42}
    listOut = []
    for v in spam.values():
        listOut.append(v)
    return listOut

@hops.component(
    "/_keys4",
    name="Keys",
    description="The keys() method returns a list of all the keys in the dictionary.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _keys4(integer):
    spam = {'color': 'red', 'age': 42}
    listOut = []
    for k in spam.keys():
        listOut.append(k)
    return listOut

@hops.component(
    "/_items4",
    name="Items",
    description="The items() method returns a list of tuples of all the key-value pairs in the dictionary.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _items4(integer):
    spam = {'color': 'red', 'age': 42}
    listOut = []
    for i in spam.items():
        listOut.append(i)
    return listOut

# checking whether a key or value exists in a dictionary
@hops.component(
    "/_in",
    name="In",
    description="The in and not in operators can be used to check whether a value exists in a dictionary.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _in(integer):
    spam = {'name': 'Zophie', 'age': 7}
    return 'name' in spam.keys()

@hops.component(
    "/_not_in",
    name="Not In",
    description="The in and not in operators can be used to check whether a value exists in a dictionary.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _not_in(integer):
    spam = {'name': 'Zophie', 'age': 7}
    return 'color' not in spam.keys()

# the get() method
# if the key does not exist, get() returns None
# if a default value is passed as a second argument, it is returned instead of None
@hops.component(
    "/_get",
    name="Get",
    description="The get() method returns the value for a given key if it exists, otherwise it returns None (or the default value if a default value is passed as a second argument).",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _get(integer):
    spam = {'name': 'Zophie', 'age': 7}
    return spam.get('name', 0)
    
# the setdefault() method
# if the key does not exist, it is set to the default value 
@hops.component(
    "/_setdefault",
    name="Set Default",
    description="The setdefault() method is similar to get(), but will set the key to the default value if it does not exist.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _setdefault(integer):
    spam = {'name': 'Pooka', 'age': 5}
    spam.setdefault('color', 'black')
    return spam
    
# use setdault() to count the number of occurrences of each letter in a string
@hops.component(
    "/_setdefault2",
    name="Set Default 2",
    description="Use setdefault() to count the number of occurrences of each letter in a string.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _setdefault2(integer):
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    return count

# pretty printing
# pprint.pprint() will "pretty print" a dictionary's values
@hops.component(
    "/_pprint",
    name="Pretty Print",
    description="pprint.pprint() will \"pretty print\" a dictionary's values.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _pprint(integer):
    import pprint
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    return pprint.pformat(count)

# tic tac toe
# the board data structure
# the keys are the (x, y) tuples for each space on the board
# the values are one of two strings: 'X' or 'O'
# the keys are the (x, y) tuples for each space on the board
# the values are one of two strings: 'X' or 'O'
@hops.component(
    "/_board",
    name="Board",
    description="The board data structure.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _board(integer):
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    return theBoard

# printing the board    
@hops.component(
    "/_print_board",
    name="Print Board",
    description="Printing the board.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _print_board(integer):
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    return theBoard['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R']
    return '-+-+-'
    return theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R']
    return '-+-+-'
    return theBoard['low-L'] + '|' + theBoard['low-M'] + '|' + theBoard['low-R']

# Nested Dictionary and Lists
@hops.component(
    "/_nested",
    name="Nested",
    description="Nested Dictionary and Lists.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _nested(integer):
    import pprint
    allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                 'Bob': {'ham sandwiches': 3, 'apples': 2},
                 'Carol': {'cups': 3, 'apple pies': 1}}
    def totalBrought(guests, item):
        numBrought = 0
        for k, v in guests.items():
            numBrought = numBrought + v.get(item, 0)
        return numBrought
    print('Number of things being brought:')
    print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
    print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
    print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
    print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
    print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))
    return allGuests

# List to Dictionary Function for Fantasy Game Inventory
@hops.component(
    "/_list_to_dict",
    name="List to Dictionary",
    description="List to Dictionary Function for Fantasy Game Inventory.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _list_to_dict(integer):
    def displayInventory(inventory):
        print("Inventory:")
        item_total = 0
        for k, v in inventory.items():
            print(str(v) + ' ' + k)
            item_total = item_total + v
        print("Total number of items: " + str(item_total))
    def addToInventory(inventory, addedItems):
        for i in addedItems:
            inventory.setdefault(i, 0)
            inventory[i] = inventory[i] + 1
        return inventory
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)
    return inv

""" 
███╗   ███╗ █████╗ ███╗   ██╗██╗██████╗ ██╗   ██╗██╗      █████╗ ████████╗██╗███╗   ██╗ ██████╗ 
████╗ ████║██╔══██╗████╗  ██║██║██╔══██╗██║   ██║██║     ██╔══██╗╚══██╔══╝██║████╗  ██║██╔════╝ 
██╔████╔██║███████║██╔██╗ ██║██║██████╔╝██║   ██║██║     ███████║   ██║   ██║██╔██╗ ██║██║  ███╗
██║╚██╔╝██║██╔══██║██║╚██╗██║██║██╔═══╝ ██║   ██║██║     ██╔══██║   ██║   ██║██║╚██╗██║██║   ██║
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║██║     ╚██████╔╝███████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                
███████╗████████╗██████╗ ██╗███╗   ██╗ ██████╗ ███████╗                                         
██╔════╝╚══██╔══╝██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝                                         
███████╗   ██║   ██████╔╝██║██╔██╗ ██║██║  ███╗███████╗                                         
╚════██║   ██║   ██╔══██╗██║██║╚██╗██║██║   ██║╚════██║                                         
███████║   ██║   ██║  ██║██║██║ ╚████║╚██████╔╝███████║                                         
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ 
"""
# working with strings
# String Literals
# double quotes
# escape characters
@hops.component(
    "/_escape_characters",
    name="Escape Characters",
    description="Escape Characters.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
# \' single quote
# \" double quote
# \t tab
# \n newline
# \\ backslash
def _escape_characters(integer):
    print ('Hello there!\nHow are you?\nI\'m doing fine.')
    return 'Hello there!\nHow are you?\nI\'m doing fine.'

# raw strings
@hops.component(
    "/_raw_strings",
    name="Raw Strings",
    description="Raw Strings.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _raw_strings(integer):
    print (r'That is Carol\'s cat.')
    return r'That is Carol\'s cat.'

# Multiline Strings with Triple Quotes
# Multiline comments

# indexing and slicing strings
@hops.component(
    "/_index_slice",
    name="Indexing and Slicing Strings",
    description="Indexing and Slicing Strings.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string0", "S0", "String"),
        hs.HopsString("string1", "S1", "String"),
        hs.HopsString("string2", "S2", "String"),
        hs.HopsString("string3", "S3", "String"),
        hs.HopsString("string4", "S4", "String"),
        hs.HopsString("string5", "S5", "String"),
        hs.HopsString("string6", "S6", "String")
    ]
)   
def _index_slice(integer):
    spam = 'Hello world!'
    print(spam[0])
    print(spam[4])
    print(spam[-1])
    print(spam[0:5])
    print(spam[:5])
    print(spam[6:])
    return spam[0], spam[4], spam[-1], spam[0:5], spam[:5], spam[6:]

# the in and not in operators with strings
@hops.component(
    "/_in_not_in",
    name="The in and not in Operators with Strings",
    description="The in and not in Operators with Strings.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("stringIn", "SIn", "String"),
        hs.HopsString("stringNotIn", "SNotIn", "String")
    ]
)
def _in_not_in(integer):
    print('Howdy' in 'Howdy partner')
    print('Howdy' not in 'Howdy partner')
    return 'Howdy' in 'Howdy partner', 'Howdy' not in 'Howdy partner'

# putting strings inside other strings
@hops.component(
    "/_str_inside_str",
    name="Putting Strings Inside Other Strings",
    description="Putting Strings Inside Other Strings.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _str_inside_str(integer):
    name = 'Zophie'
    age = 7
    print('My name is %s. I am %s years old.' % (name, age))
    return 'My name is %s. I am %s years old.' % (name, age)

# f-strings
@hops.component(
    "/_f_strings",
    name="f-Strings",
    description="f-Strings.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _f_strings(integer):
    name = 'Zophie'
    age = 7
    print(f'My name is {name}. I am {age} years old.')
    return f'My name is {name}. I am {age} years old.'

# useful string methods
# upper(), lower(), isupper(), islower() methods
@hops.component(
    "/_useful_str_methods",
    name="Useful String Methods",
    description="Useful String Methods.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("upper", "U", "String"),
        hs.HopsString("lower", "L", "String"),
        hs.HopsString("isupper", "IU", "String"),
        hs.HopsString("islower", "IL", "String")

    ]
)
def _useful_str_methods(integer):
    spam = 'Hello world!'
    print(spam.upper())
    print(spam.lower())
    print(spam.isupper())
    print(spam.islower())
    return spam.upper(), spam.lower(), spam.isupper(), spam.islower()

# the isX string methods
@hops.component(
    "/_isx_methods",
    name="The isX String Methods",
    description="The isX String Methods.",
    inputs=[
        hs.HopsInteger("integer", "I", "Integer")
    ],
    outputs=[
        hs.HopsString("isalpha", "IA", "String"),
        hs.HopsString("isalnum", "IAL", "String"),
        hs.HopsString("isdecimal", "ID", "String"),
        hs.HopsString("isspace", "IS", "String"),
        hs.HopsString("istitle", "IT", "String"),
        hs.HopsString("startswith", "SW", "String"),
        hs.HopsString("endswith", "EW", "String")
    ]
)
def _isx_methods(integer):
    return 'hello'.isalpha(), 'hello123'.isalnum(), '123'.isdecimal(), ' '.isspace(), 'This Is Title Case'.istitle(), 'Hello world!'.startswith('Hello'), 'Hello world!'.endswith('world!')

# validate input data
@hops.component(
    "/_validate_input_data",
    name="Validate Input Data",
    description="Validate Input Data.",
    inputs=[
        hs.HopsString("string", "S", "String")
    ],
    outputs=[
        hs.HopsString("string", "S", "String")
    ]
)
def _validate_input_data(string):
    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    return string

# startswith() and endswith() methods
@hops.component(
    "/_startswith_endswith",
    name="startswith() and endswith() Methods",
    description="startswith() and endswith() Methods.",
    inputs=[
        hs.HopsString("string", "S", "String")
    ],
    outputs=[
        hs.HopsString("startswith", "SW", "String"),
        hs.HopsString("endswith", "EW", "String")
    ]
)
def _startswith_endswith(string):
    return string.startswith('Hello'), string.endswith('world!')


# join() and split() methods
@hops.component(
    "/_join_split",
    name="join() and split() Methods",
    description="join() and split() Methods.",
    inputs=[
        hs.HopsString("string", "S", "String")
    ],
    outputs=[
        hs.HopsString("join", "J", "String"),
        hs.HopsString("split", "SP", "String")
    ]
)
def _join_split(string):
    print(', '.join(['cats', 'rats', 'bats']))
    print(' '.join(['My', 'name', 'is', 'Simon']))
    print('My name is Simon'.split())
    print('MyABCnameABCisABCSimon'.split('ABC'))
    return ', '.join(['cats', 'rats', 'bats']), ' '.join(['My', 'name', 'is', 'Simon']), 'My name is Simon'.split(), 'MyABCnameABCisABCSimon'.split('ABC')

# splitting strings with the partition() and rpartition() methods
@hops.component(
    "/_partition_rpartition",
    name="splitting strings with the partition() and rpartition() Methods",
    description="splitting strings with the partition() and rpartition() Methods.",
    inputs=[
        hs.HopsString("string", "S", "String")
    ],
    outputs=[
        hs.HopsString("partition", "P", "String"),
        hs.HopsString("rpartition", "RP", "String")
    ]
)
def _partition_rpartition(string):
    print('Hello there!'.partition(' '))
    print('Hello there!'.rpartition(' '))
    return 'Hello there!'.partition(' '), 'Hello there!'.rpartition(' ')

# ljust(), rjust(), and center() string methods
@hops.component(
    "/_ljust_rjust",
    name="ljust(), rjust(), and center() String Methods",
    description="ljust(), rjust(), and center() String Methods.",
    inputs=[
        hs.HopsString("string", "S", "String")
    ],
    outputs=[
        hs.HopsString("ljust", "LJ", "String"),
        hs.HopsString("rjust", "RJ", "String"),
        hs.HopsString("center", "C", "String"),
        hs.HopsString("rjust2", "RJ2", "String"),
        hs.HopsString("center2", "C2", "String")
    ]
)
def _ljust_rjust(string):
    print('Hello'.ljust(10))
    print('Hello'.rjust(10))
    print('Hello'.center(10))
    print('Hello'.rjust(20, '='))
    print('Hello'.center(20, '*'))
    return 'Hello'.ljust(10), 'Hello'.rjust(10), 'Hello'.center(10), 'Hello'.rjust(20, '='), 'Hello'.center(20, '*')

# remove whitespace with strip(), rstrip(), and lstrip() methods
@hops.component(
    "/_strip_rstrip_lstrip",
    name="remove whitespace with strip(), rstrip(), and lstrip() Methods",
    description="remove whitespace with strip(), rstrip(), and lstrip() Methods.",
    inputs=[
        hs.HopsString("string", "S", "String")
    ],
    outputs=[
        hs.HopsString("_strip", "S", "String"),
        hs.HopsString("_rstrip", "SR", "String"),
        hs.HopsString("_lstrip", "SL", "String")
    ]
)
def _strip_rstrip_lstrip(string):
    spam = '    Hello World     '
    print(spam.strip()) 
    print(spam.rstrip())
    print(spam.lstrip())
    return spam.strip(), spam.rstrip(), spam.lstrip()




# Numeric values of characters with ord() and chr() functions
@hops.component(
    "/_ord_chr",
    name="Numeric values of characters with ord() and chr() Functions",
    description="Numeric values of characters with ord() and chr() Functions.",
    inputs=[
        hs.HopsString("string", "S", "String")
    ],
    outputs=[
        hs.HopsString("ord", "O", "String"),
        hs.HopsString("chr", "C", "String")
    ]
)
def _ord_chr(string):
    print(ord('H'))
    print(ord('e'))
    print(ord('l'))
    print(ord('l'))
    print(ord('o'))
    print(chr(72))
    print(chr(101))
    print(chr(108))
    print(chr(108))
    print(chr(111))
    return ord('H'), ord('e'), ord('l'), ord('l'), ord('o'), chr(72), chr(101), chr(108), chr(108), chr(111)


""" 
███████╗██╗  ██╗ ██████╗ ██████╗ ████████╗                           
██╔════╝██║  ██║██╔═══██╗██╔══██╗╚══██╔══╝                           
███████╗███████║██║   ██║██████╔╝   ██║                              
╚════██║██╔══██║██║   ██║██╔══██╗   ██║                              
███████║██║  ██║╚██████╔╝██║  ██║   ██║                              
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝                              
                                                                     
██████╗ ██████╗  ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║██╔════╝
██████╔╝██████╔╝██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║███████╗
██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║╚════██║
██║     ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
"""

# a short program: Pig Latin
# English to Pig Latin
@hops.component(
    "/_pig_latin2",
    name="a short program: Pig Latin",
    description="a short program: Pig Latin.",
    inputs=[
        hs.HopsString("string", "S", "String")
    ],
    outputs=[
        hs.HopsString("pig_latin", "PL", "String")
    ]
)
def _pig_latin2(string):
    print('Enter the English message to translate into Pig Latin:')
    message = string
    VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
    pigLatin = []    # A list of the words in Pig Latin.
    for word in message.split():
        # Separate the non-letters at the start of this word:
        prefixNonLetters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetters += word[0]
            word = word[1:]
        if len(word) == 0:
            pigLatin.append(prefixNonLetters)
            continue
        # Separate the non-letters at the end of this word:
        suffixNonLetters = ''
        while not word[-1].isalpha():
            suffixNonLetters += word[-1]
            word = word[:-1]
        # Remember if the word was in uppercase or title case.
        wasUpper = word.isupper()
        wasTitle = word.istitle()
        word = word.lower()    # Make the word lowercase for translation.
        # Separate the consonants at the start of this word:
        prefixConsonants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefixConsonants += word[0]
            word = word[1:]
        # Add the Pig Latin ending to the word:
        if prefixConsonants != '':
            word += prefixConsonants + 'ay'
        else:
            word += 'yay'
        # Set the word back to uppercase or title case:
        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()
        # Add the non-letters back to the start or end of the word.
        pigLatin.append(prefixNonLetters + word + suffixNonLetters)
    # Join all the words back together into a single string:
    print(' '.join(pigLatin))
    return ' '.join(pigLatin)

# a short program: a simple Caesar cipher
@hops.component(
    "/_caesar_cipher",
    name="a short program: a simple Caesar cipher",
    description="a short program: a simple Caesar cipher.",
    inputs=[
        hs.HopsString("string", "S", "String")
    ],
    outputs=[
        hs.HopsString("caesar_cipher", "CC", "String")
    ]
)
def _caesar_cipher(string):
    print('Enter the message to encrypt or decrypt:')
    message = string
    print('Enter the encryption/decryption key:')
    key = 13
    mode = 'encrypt'    # Set to either 'encrypt' or 'decrypt'.
    # Every possible symbol that can be encrypted:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    # Store the encrypted/decrypted form of the message:
    translated = ''
    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key
            # Handle wraparound, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex -= len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex += len(SYMBOLS)
            translated += SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated += symbol
    # Output the translated string:
    return translated

#a short program: guessing game
@hops.component(
    "/_guessing_game",
    name="a short program: guessing game",
    description="a short program: guessing game.",
    inputs=[
        hs.HopsString("string", "S", "String")
    ],
    outputs=[
        hs.HopsString("guessing_game", "GG", "String")
    ]
)
def _guessing_game(string):
    import random
    print('I am thinking of a number between 1 and 20.')
    secretNumber = random.randint(1, 20)
    # Ask the player to guess 6 times.
    for guessesTaken in range(1, 7):
        print('Take a guess.')
        guess = int(string)
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break    # This condition is the correct guess!
    if guess == secretNumber:
        print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
        return 'Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!'
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))
        return 'Nope. The number I was thinking of was ' + str(secretNumber)

""" 
██████╗  █████╗ ████████╗████████╗███████╗██████╗ ███╗   ██╗                                    
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║                                    
██████╔╝███████║   ██║      ██║   █████╗  ██████╔╝██╔██╗ ██║                                    
██╔═══╝ ██╔══██║   ██║      ██║   ██╔══╝  ██╔══██╗██║╚██╗██║                                    
██║     ██║  ██║   ██║      ██║   ███████╗██║  ██║██║ ╚████║                                    
╚═╝     ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝                                    
                                                                                                
███╗   ███╗ █████╗ ████████╗ ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗                               
████╗ ████║██╔══██╗╚══██╔══╝██╔════╝██║  ██║██║████╗  ██║██╔════╝                               
██╔████╔██║███████║   ██║   ██║     ███████║██║██╔██╗ ██║██║  ███╗                              
██║╚██╔╝██║██╔══██║   ██║   ██║     ██╔══██║██║██║╚██╗██║██║   ██║                              
██║ ╚═╝ ██║██║  ██║   ██║   ╚██████╗██║  ██║██║██║ ╚████║╚██████╔╝                              
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝                               
                                                                                                
██╗    ██╗██╗████████╗██╗  ██╗    ██████╗ ███████╗ ██████╗ ██╗   ██╗██╗      █████╗ ██████╗     
██║    ██║██║╚══██╔══╝██║  ██║    ██╔══██╗██╔════╝██╔════╝ ██║   ██║██║     ██╔══██╗██╔══██╗    
██║ █╗ ██║██║   ██║   ███████║    ██████╔╝█████╗  ██║  ███╗██║   ██║██║     ███████║██████╔╝    
██║███╗██║██║   ██║   ██╔══██║    ██╔══██╗██╔══╝  ██║   ██║██║   ██║██║     ██╔══██║██╔══██╗    
╚███╔███╔╝██║   ██║   ██║  ██║    ██║  ██║███████╗╚██████╔╝╚██████╔╝███████╗██║  ██║██║  ██║    
 ╚══╝╚══╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    
                                                                                                
███████╗██╗  ██╗██████╗ ██████╗ ███████╗███████╗███████╗██╗ ██████╗ ███╗   ██╗███████╗          
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██║██╔═══██╗████╗  ██║██╔════╝          
█████╗   ╚███╔╝ ██████╔╝██████╔╝█████╗  ███████╗███████╗██║██║   ██║██╔██╗ ██║███████╗          
██╔══╝   ██╔██╗ ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║██║██║   ██║██║╚██╗██║╚════██║          
███████╗██╔╝ ██╗██║     ██║  ██║███████╗███████║███████║██║╚██████╔╝██║ ╚████║███████║          
╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝  
"""

# finding patterns of text without regular expressions
# is phone number in text?
@hops.component(
    "/is_phone_number",
    name="Is Phone Number",
    description="Check if a text contains a phone number",
    icon="phone",
    inputs=[
        hs.HopsString("text", "Text", "Text to check")
],
    outputs=[
        hs.HopsString("phone_number", "Phone Number", "Phone number found in text")
    ]

)
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# Finding Patterns of Text with Regular Expressions
# grouping with parentheses
# group() method
@hops.component(
    "/grouping",
    name="Grouping with Parentheses",
    description="Grouping with Parentheses",
    icon="phone",
    inputs=[
        hs.HopsString("text", "Text", "Text to check")
    ],
    outputs=[
        hs.HopsString("phone_number", "Phone Number", "Phone number found in text"),
        hs.HopsString("area_code", "Area Code", "Area code found in text"),
        hs.HopsString("all_group", "All Group", "All group found in text"),
        hs.HopsString("all_groups", "All Groups", "All groups found in text")
    ]
)
def grouping_w(text):
    import re
    phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
    mo = phone_num_regex.search(text)
    return mo.group(2), mo.group(1), mo.group(0), mo.group()
    
# . ^ $ * + ? { } [ ] \ | ( )
# \. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)
# Matching Multiple Groups with the Pipe
@hops.component(
    "/pipe7",
    name="Matching Multiple Groups with the Pipe",
    description="Matching Multiple Groups with the Pipe",
    icon="phone",
    inputs=[
        hs.HopsString("text", "Text", "Text to check")
    ],
    outputs=[
        hs.HopsString("textOut", "Text1", "Text found in text")
    ]
)
def pipe7(text):
    import re
    hero_regex = re.compile(r"Batman|Tina Fey")
    mo1 = hero_regex.search(text)
    return mo1.group()
    
# findall() method
@hops.component(
    "/findall",
    name="findall() method",
    description="findall() method",
    icon="phone",
    inputs=[
        hs.HopsString("text", "Text", "Text to check")
    ],
    outputs=[
        hs.HopsString("textOut", "Text1", "Text found in text")
    ]
)
def findall(text):
    import re
    phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    mo = phone_num_regex.findall(text)
    return mo

# Batmobile lost a wheel
@hops.component(
    "/batmobile",
    name="Batmobile lost a wheel",
    description="Batmobile lost a wheel",
    icon="phone",
    inputs=[
        hs.HopsString("text", "Text", "Text to check")
    ],
    outputs=[
        hs.HopsString("textOut", "Text1", "Text found in text")
    ]
)
def batmobile(text):
    import re
    bat_regex = re.compile(r"Bat(man|mobile|copter|bat)")
    mo = bat_regex.search(text)
    return mo.group()

# optional matching with the question mark






if __name__ == "__main__":
    app.run(debug=True)