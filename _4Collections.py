#collections : list,dict,set,tuple,strings
#they are called collections because they are containers of other things
#strings: are collection of characters
#list: are collection of items which are mutable
#tuple: are collection of items which are immutable
#dict: are collection of items which are mutable
#set: are collection of items which are immutable

def stringCollection():
    A = "hello"
    B = "prasanth"
    wish = A + " " + B
    print("string concatenation:", wish) # Note the colon after "string concatenation"
    #output for this function:"hello prasanth"
    """
    This function concatenates two strings and prints the result.
    There are no parameters.
    There is no return value.
    """

def listCollection():
    A = [1,2,3]
    B = [1,2,3]
    wish = A + B
    print("list concatenation:", wish) # Note the colon after "list concatenation"
    #output for this function:[1, 2, 3, 1, 2, 3]
def tupleCollection():
    A = (1,2,3)
    B = (1,2,3)
    wish = A + B
    print("tuple concatenation:", wish) # Note the colon after "tuple concatenation"
    #output for this function:(1, 2, 3, 1, 2, 3)
def dictCollection():
    A = {"a":1,"b":2}
    B = {"a":1,"b":2}
    
    print(A,B) 
    #output for this function:{'a': 1, 'b': 2, 'a': 1, 'b': 2}
stringCollection()
listCollection()
tupleCollection()
dictCollection()