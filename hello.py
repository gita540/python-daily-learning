print("hello, world!")
a =6
print(a)
a='hi'
print(len(a))
print(a+str(len(a)))

def main():
    print(repeat('yay',False))


def repeat(s, exclaim):
    result =s+s+s
    if exclaim:
        result = result+'!!!'
        return result
        
main()       