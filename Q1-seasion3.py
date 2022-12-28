def eq():
    print("""the Standear form of Quadratic Equation is :
           aX^2 + bX + c = O
           to solve the problem, insert the following numbers : """)
    a = int(input(" a : "))
    b = int(input(" b : "))
    c = int(input(" c : "))
    delta = b ** 2 - 4 * a * c
    if delta > 0 : 
        x1 = ((-1 * b - (b ** 2 - 4 * a * c)** 0.5) / 2 * a )
        x2 = ((-1 * b + (b ** 2 - 4 * a * c)** 0.5) / 2 * a )
    if delta == 0 :
        print (" the only answer is = " , x1 )
    if delta < 0 :
        print ("the equation has no answer." ) 
         
eq()
