# ***Tech201 Functions***
An introduction to Python Functions. 




- A **function** is a **block of code** which *only runs when it is called*.

- You can *pass data*, known as **parameters**, into a function.

- A function can *return data* as a result.

- In a nutshell, **functions** are *tools* that allow us to *embed certain pieces of code*, so we can use them later.

```bash
default code for a function
def function_name():
    print("This is how you make a function.")
 # running the code at this stage will not return anything, as we did not CALL the function.   
 
 #To CALL a function, simply use the function name:

function_name()
```

```bash
# Showcasing

def print_something():
     print("Something has been printed.")
# def = define; creating a function, followed by the name we give the function.
# print_something = name of function
# () after the function name = here we can introduce arguments for the function(how we want to use the function).
# print("something has been printed.") = what we are asking the function to do.
print_something() # will print "Something has been printed.".
```

- At this stage, this function is not efficient as it just prints something that can be written in a different and simpler way.

### Ways of adding complexity to a function:
1. Functions and arguments
```bash
#   SHOWCASE
def print_something(print_string):
    print(print_string)
print_something() # ERROR:
print_something("This is my variable.")
print_something("This is the second time I am calling this function.")
```
- Extra info:

In Java:
```bash
# public void print_string(string_text)
# we do not need to specify things like "public void" in Python, as it is a dynamicly typed language and it knows what it needs to call.
```

```bash
def greeting(name):
    print("Hello, my name is " + name)
greeting("Flo")
greeting("Paul")
greeting("George")
```

2. The Return statement
```bash
def addition(int1, int2):
    return int1 + int2 # adding return in front of the action of the function will tell the function to know what to do with the function`s result(like above with print)
#
print(addition(2, 2)) # prints None because we didn`t ask it to do anything with the number it gets from adding the 2 vallues
```

3. Default arguments
```bash
def addition(int1=2, int2=5):
    return int1 + int2
print(addition()) # no need to mention when calling the function, as we already gave the arguments a certain value.
print(addition(3,5)) # we don`t need to print the default values, as we can overwrite them, but only for that specific time.
print(addition()) # will print 7 again, as it calls the default set earlier again
```

4. Multiple arguments
```bash
def multi_args(*multiargs): # *(takes as many arguments as we want, so does not create a variable, but a tuple) multiargs is not an argument but a tuple
    print(type(multiargs))
#
    for arg in multiargs:
        print(arg)
#
multi_args(1, 2, 3, 4, 5, 6) # print the <class 'tuple'> and 1 2 3 4 5 6  # the arguments we pass are put into a tuple
```

5. Type Hints
```bash
def greeting(name: str):
    print("Hello, my name is " + name)
#
greeting(345264) #ERROR
# adding type hints - python tells us when we have a typing error
greeting("Flo") # will print Hello my name is Flo
```
```bash
def division(num1: int = 5, num2: int = 7) -> float: # -> and then the data type you expect to come out of the function #can do default types even if we use type hints
    return num1 / num2
#
print(type(division(4, 53))) # will print <class 'float'>
print(division()) # prints the result of 5/7 in float as we put default types
```




### Functions best practices:

- Name your functions CLEARLY using lower case and underscores!!!!!!!!
- All arguments should be CLEAR in their need and where possible include their expected type!!!!!!
- Remember the return statement or your functions are going to return none !!!!!
- Keep functions SMALL to preserve readability and simplicity!!!!!
- Use comments in your functions and methods to give instructions on how to use them!!!!!
- Consider using type hints to avid type errors when you run your code!!!!
- D R Y = Don`t Repeat Yourself !!!!!!

- Reasoning behind DRY = KEEP IT STUPID SIMPLE! - easy to manage code, easy to read code.