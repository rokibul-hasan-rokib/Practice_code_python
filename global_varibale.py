fruit = "apple"

def myfunc():
    global fruit
    fruit = "banana"
    print(fruit)
    
myfunc()

print(fruit)

