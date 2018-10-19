first_num=int(input("Please enter the first Number :"))
second_num=int(input("Please enter the second Number :"))
calc=input("Please enter any  listed details to do the calculation (+,-,*,/) :")

if calc=="+":
    print("Addition of both the Numbers are :", first_num + second_num)
else:
    if calc=="-":
        print("Substraction of boot Numbers are :", first_num - second_num)
    else:
        if calc=="*":
            print("Multiplication of both the numbers are :", first_num * second_num)
        else:
            if calc=="/":
                print("Division of two Numbers are :", first_num / second_num)
            else:
                print("please enter valid input Ex:(+,-,*,/)")
