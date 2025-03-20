def myFunction(*keywords):
    print("The first keyword is " + keywords[2])
    
myFunction("Emil", "Tobias", "Linus")

def myFunction(**kid):
    for x in kid:
        print(x + " is " + kid[x])

myFunction(fname = "Emil", lname = "Refsnes")