# Q&A
*Questions* is a Python program that asked for name and age from user input, helping to improve on coding knowledge and learn more about edge cases, classes, error checking conditions  
  
Implemented error checking conditions using Python’s built in functions such as isdigit or isalpha to check for edge cases to retrieve different attributes such as name and age from the class object  
  
![](character.gif)
# Usage
For your convenience, here is how you could do it in CMD environment.

1. First compile: gcc character.c
2. After compilation, to run the program, you would type the following command: a.exe

# Outputs
**Example console 1 (no error)**
```
Hi, what is your name?
> Adrian
How old are you Adrian?
> 12
Adrian, you are a child.

So your name is Adrian and you are 12 years old? (yes/no)
> no
Hi, what is your name?
> Tan
How old are you Tan?
> 19
Tan, you are an adult.

So your name is Tan and you are 19 years old? (yes/no)
```

**Example console 2 (with error)**
```
Hi, what is your name?
> 1
```
```
Invalid input

Hi, what is your name?
> Tan
How old are you Tan?
> tan
```
```
Invalid input

How old are you Tan?
> 19
Tan, you are an adult

So your name is Tan and you are 19 years old? (yes/no)
> s
```
```
Invalid input

So your name is Tan and you are 19 years old? (yes/no)
> yes
```

