## Intro to Functions (and tests)

### Functions

Functions are used to group a collection of expressions.  For example, the code `name = 'bob'` assigns the string (or text) 'bob' to a variable called string.  That's an expression.  One procedure.  

Sometimes, we may want to group together multiple expressions, in a type of procedure.  For that we can use functions.

```python
name = 'bob'
print(name)

def sayHello():
  name = 'bob'.capitalize()
  greeting = 'Hello, my name is ' + name
  print(greeting)

print('hello')
```  

As you can see in the code above, we use the function `sayHello` to a few things with the text 'bob'.  As we add more and more code to a file, these small grouping will become important.

Let's first identify the parts of this function.  We initialize a function with the `def` keyword in python.  Followed by the name of the function.  Then the next lines are the `body` of the function - this is the procedure the function will perform.  Now, run this code.

I've written the code in the file `1-function-intro.py`, so we just need to run this file.  

> If the below steps are tricky, just copy and paste the above code into https://repl.it/languages/python3 .  And then press the play button.  

1. Open your console, or terminal and make sure you are in the directory that says 1-intro-to-functions.

2. Then run the file, by typing `python 1-function-intro.py`

3. See what prints out in your terminal.  

Or more importantly notice, what did not print out in the terminal.  First, the text 'bob' printed out, and then the text 'hello' printed out.  However, the text 'Hello my name is Bob' did not print out.  

This is because python programs will flow from top to bottom, but when defining a function, the code inside will not run.  It only runs when we explicitly ask it to.  For example type in the following, and run the code:

```python

sayHello()

```

Note that with functions, we define the code in one place, and run it in another.  We can run the code in whatever order we want.  This becomes pretty powerful.  Functions become tools that we build, and then can pull off the shelf when we see fit.

### Functional Arguments

In the code above, `sayHello` always does the same thing.  But functions, have mechanisms for us to slightly change the behavior.  In this case, we can change the person's name.

```python
# def sayHello():
#   name = 'bob'.capitalize()
#   greeting = 'Hello, my name is ' + name
#   print(greeting)

def sayHello(firstName):
    name = firstName.capitalize()
    greeting = 'Hello, my name is ' + name
    print(greeting)

sayHello('fred')
  # 'Hello, my name is Fred'

sayHello('Sally')
  # 'Hello, my name is Sally'
```

Take a look at how that worked.  The function definition and body stays the same, but when executing the function we pass through different data.


### Holding on to the result

Now that we can get these different results from functions, we may want to hold onto the value.  However, one thing to note about the functions is that everything defined inside the function is stuck there.

For example, try to reference the variables name or greeting outside of the function, and you cannot.

```python
def sayHello(firstName):
    name = firstName.capitalize()
    greeting = 'Hello, my name is ' + name
    print(greeting)

sayHello('bob')
greeting
  # NameError: name 'greeting' is not defined
```

The function acts a wall and the variables defined inside of the wall are trapped there.  The only way to throw something over the wall is with the return keyword.  Let's take a look:

```python
# without return keyword: Wrong.
def sayHello(firstName):
    name = firstName.capitalize()
    greeting = 'Hello, my name is ' + name
    print(greeting)

greeting = sayHello('bob')
# greeting has no value

def sayHello(firstName):
    name = firstName.capitalize()
    greeting = 'Hello, my name is ' + name
    return(greeting)

greeting = sayHello('bob')
greeting
  # 'Hello, my name is Bob'
```

So return values allow us to capture the output of a function.  Time for some practice with functions.
