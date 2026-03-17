import math
def greet(name):
    message = "Hello, "+name
    return message
def add(a, b):
    return a +b
def is_even(n):
    return n %2 == 0

def double(a,b):
    result = add(a,b)
    return result *2   

def repeat(s,exclaim):
       result = s+s+s
       if exclaim:
          result = result +'!!!'

       return result   



def main():
    result = "Geetha"
    print(result)
    print(greet("geetha"))
    print(add(4,3))
    print(is_even(4))
    print(is_even(5))
    print(double(5,3))
    print(repeat("gita", True))
    print(repeat('Yay', False))

if __name__ == "__main__"  :
    main()

