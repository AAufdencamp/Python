# https://opentdb.com/

#review API endpoints, parameters and build Quizzler APP and use tkinter

#https://opentdb.com/api.php?amount=10&type=boolean
#everything before ? is the API Endpoint base. After ? are the parameters. More than one parameters are joined by &

#to work with APIs we must import the requests module
# import requests

#HTML entities replace characters that confuse HTML code. HTML entities escape those problem characters
# https://www.w3schools.com/html/html_entities.asp

# To unescape HTML entities to get back to human readable text
# import html
# html.unescape()


# https://www.freeformatter.com/html-escape.html

# In Python, data types are flexible. You can create a variable and change its data type later on. Dynamic Typing.

# To reduce error using data types.
# var: datatype declaration
# example
  # age: int
  # name: str
  # height: float
  # is_human: bool

#We can specify the data type inside a function.

def police_check(age:int):   #here we specify the data type for var age to be int.
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


def police_check(age:int) -> bool:  #we can also specify the data type of the output of a function using hyphen & arrow
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

print(police_check(19)) #we can use the output from this function to create a print statement

if police_check(19):
    print("You may pass")
else:
    print("Pay a fine.")


#Type Hints
# def greeting(name:str) -> str:
#    return 'Hello' + name

#Type Hints are helpful if you want your IDE like PyCharm to hep you spot potential bugs