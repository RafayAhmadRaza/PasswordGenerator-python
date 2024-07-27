import random
import pyperclip
Letters = 'abcdefghijklmnopqrstuvwxyz'

specialCharacters = '!@#$%^&*()[]{},.<>/?;:\'\"'
numbers = '0123456789'

smallChList = list(Letters)
upperChList = list(Letters.upper())

specialChList = list(specialCharacters)
numberList = list(numbers)


def passwordCreator(N:int) -> str:
    password = []
    for i in range(N):
        selector = random.randint(0,3)

        if selector == 0:
            password.append(smallChList[random.randint(0,(len(smallChList)-1))])

        elif selector == 1:
            password.append(upperChList[random.randint(0,(len(upperChList)-1))])

        elif selector == 2:
            password.append(numberList[random.randint(0,(len(numberList)-1))])

        elif selector ==3:
            password.append(specialCharacters[random.randint(0,(len(specialCharacters)-1))])

    copiedPassword = "".join(password)

    return copiedPassword



if __name__ == "__main__":
    print("\n\tPassword Creator\n\tBy Rafay Ahmad Raza")

    length = input("Enter the length of password ")

    while not length.isdecimal():
        length = input("> ")
    
    password = passwordCreator(int(length))
    pyperclip.copy(password)
    print(f"The password {password} has been copied to your clipboard")