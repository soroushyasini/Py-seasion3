def eq():
    print("""the Standear form of Quadratic Equation is :
           aX^2 + bX + c = O
           to solve the problem, insert the following numbers : """)
    a = int(input(" a : "))
    b = int(input(" b : "))
    c = int(input(" c : "))

    x1 = ((-1 * b - (b ** 2 - 4 * a * c)** 0.5) / 2 * a )
    x2 = ((-1 * b + (b ** 2 - 4 * a * c)** 0.5) / 2 * a )
    if x2 != x1 :
        print (" the first answer is = " , x1 )
        print (" the second answer is = " , x2 )
    else :
         print (" the only answer is = " , x1 )
eq()
