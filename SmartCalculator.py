responses=["HELLO!! WELCOME TO SMART CALCULATOR","MY NAME IS CALI","SORRY, THIS BEYOND MY ABILITY","THANK YOU FOR USING ME :)"]

def extract_no_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def max(a,b):
    return a if a>b else b

def min(a,b):
    return a if a<b else b

def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1

def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1

def end():
    print(responses[3])
    input("Plaese enter key to exit")
    exit()

def sorry():
    print(responses[2])

def myname():
    print(responses[1])
    
def help():
    print("List of valid commands")
    for k in operations:
        print(k)
    for k in commands:
        print(k)

operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"MINUS":subtract,"SUBTRACT":subtract,"DIFFERENCE":subtract,"PRODUCT":multiply,"MULTIPLY":multiply,"MULTIPLICATION":multiply,"DIVIDE":divide,"DIVISION":divide,"LCM":lcm,"HCF":hcf,"LOWEST COMMON FACTOR":lcm,"HIGHEST COMMON FACTOR":hcf,"BIG":max,"MAXIMUM":max,"GREATER":max,"MINIMUM":min,"SMALLEST":min,"SMALL":min}
commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end,"HELP":help}

def main():
    print(responses[0])
    print(responses[1])
    while True:
        print("-----------------******------------*******-----------------")
        text=input("Enter the text:    ")
        for word in text.split(' '):
            if word.upper() in operations.keys():
                try:
                    l=extract_no_from_text(text)
                    r=operations[word.upper()](l[0],l[1])
                    print(r)
                except:
                    print("Something went wrong")
                    print("Please try again!!")
                finally:
                    break
            elif word.upper() in commands.keys():
                commands[word.upper()]()
                break
        else:
            sorry()

if __name__=="__main__":
    main()
              
    






























    

        
