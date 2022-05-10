# Gradientenabstiegverfahren in Python
# Numerische Methoden Praktikum Aufgabe 2
# Milan Wenske 07.05.2022


list_x = [- 1, 0, 1.5, 3, 3.5, 4, 4.5, 6, 7.3]
list_y = [-0.5, 0.5, 1.8, 2, 4, 4.3, 5, 6.8, 7]
i = 0
a1 = 0  # Startwert
a2 = 0  # Startwert
learning_rate = 0.01


def lossFunktion (a1 ,a2, list_x, list_y):
    i = 0
    L = 0

    while i <= 8:
        L_temp = (list_y[i] - (a1 * list_x[i] + a2))**2
        L = L + L_temp
        i += 1
    L = L / i
    return L

L = lossFunktion (a1 ,a2, list_x, list_y)

def grad_a1(a1, a2, list_x, list_y):
    i = 0
    L = 0
    while i <= 8:
        L_temp = list_y[i] - (a1 * list_x[i] + a2)
        L = L + L_temp
        i += 1
    L = -2 * L / i
    return L


def grad_a2(a1, a2, list_x, list_y):
    i = 0
    L = 0
    while i <= 8:
        L_temp = list_y[i] - (a1 * list_x[i] + a2)   # wahrscheinlich falsch
        L = L + L_temp
        i += 1
    L = -3 * L / i   # wahrscheinlich falsch
    return L



while i <= 100:
    list_grad_a1 = [1, 2]
    list_grad_a2 = [1, 2]
    differenz_a1 = 1
    differenz_a2 = 1

    if differenz_a1 >= 0.001:
        list_grad_a1[0] = a1

        grad_a1 = grad_a1(a1, a2, list_x, list_y)
        a1 = a1 - (grad_a1 * learning_rate)

        list_grad_a1[1] = a1
        differenz_a1 = abs(list_grad_a1[0] - list_grad_a1[1])

    if differenz_a2 >= 0.001:
        list_grad_a2[0] = a2

        grad_a2 = grad_a2(a1, a2, list_x, list_y)
        a2 = a2 - (grad_a2 * learning_rate)

        list_grad_a2[1] = a2
        differenz_a2 = abs(list_grad_a2[0] - list_grad_a2[1])

    i += 1

    print("a1", a1)
    print("a2", a2)



