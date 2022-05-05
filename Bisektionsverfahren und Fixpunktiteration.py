# Bisektionsverfahren und Fixpunktiteration
# 05.05.2022

import math

print("Zum Lösen der Gleichung: y = math.log(2 + 4 * x**2, math.e) - x "
      "wird das Bisektionsverfahren oder die Fixpunktiteration angewedet.")
w = input("Bitte wählen Sie für das Bisektionsverfahren die 1 und für die Fixpunktiteration die 2.")
w = int(w)

if (w < 2):

    #  Bisektionsverfahren

    def funktion(x):
        y = math.log(2 + 4 * x**2, math.e) - x
        return y

    a = 5  # startwert 1
    b = 1  # startwert 2

    f_a = funktion(a)
    f_b = funktion(b)
    d = (a + b) / 2
    f_d = funktion(d)

    i = 0
    differenz = 1
    list = [0, 0]
    list_d = [1, 2]

    while (i < 100 ) and (differenz >= 0.001):

        list_d[0] = d

        def funktion(x):
            y = math.log(2 + 4 * x**2, math.e) - x
            return y


        if (f_a <= f_b):
            if (f_d >= 0):
                list[0] = a
                list[1] = d
            else:
                list[0] = d
                list[1] = b
        else:
            if (f_d >= 0):
                list[0] = d
                list[1] = b
            else:
                list[0] = a
                list[1] = d

        f_a = funktion(list[0])
        f_b = funktion(list[1])
        d = (list[0] + list[1]) / 2
        f_d = funktion(d)

        a = list[0]
        b = list[1]

        list_d[1] = d

        differenz = abs(list_d[0] - list_d[1])

        i += 1

    print("Das Bisektionsverfahren erreicht x =", d, "nach", i, "Iterationen.")



## Fixpunktiteration

else:

    def funktion_eql_zero(x):
        y = math.log(4*x**2+2, math.e)
        return y


    i = 0
    x_n = 1  # Startwert
    list_fix = [1, 2]
    differenz_fix = abs(list_fix[0] - list_fix[1])



    while (i < 100) and (differenz_fix >= 0.001):
        list_fix[0] = x_n
        x_n = funktion_eql_zero(x_n)
        list_fix.append(x_n)
        list_fix[1] = x_n
        differenz_fix = abs(list_fix[0] - list_fix[1])
        i += 1

    print("Die Fixpunktiteration erreicht x =", list_fix[1], "nach", i, "Iterationen.")



