name = input("Enter your name: ")
age = int(input("Enter your age: "))

def checkAge(age):
    if(age <= 18):
        return "child"
    elif(age > 18 and age < 65):
        return "adult"
    else: 
        return "senior"

print(f"Hello {name} you are a {checkAge(age)}")