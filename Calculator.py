print ("CALCULATOR\n" "\nMy marks:\n+ = plus \n- = minus \nx = times \n/ = divided \n* = power\n")
countinue = True
while True:
    number_1 = float(input("First number:"))
    mark = input ("Mark:")
    number_2 = float(input("Second number:"))


    if mark == "+":
        print (number_1 + number_2)
    elif mark == "-":
        print (number_1 - number_2)
    elif mark == "x":
        print (number_1 * number_2)
    elif mark == "/":
        print (number_1 / number_2)
    elif mark == "*":
        print (number_1 ** number_2)
    else:
        print("Erorr")
    nezadano = True
    while nezadano:
        odpoved = str(input("\nPřejete si zadat další příklad? yes / no: "))
        if (odpoved == "yes" or odpoved == "YES"):
           nezadano=False
        elif (odpoved == "no" or odpoved == "NO"):
            print ("Bye")
            break
        else:
          pass
    break


    
           


