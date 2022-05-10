# Gradientenabstiegverfahren
# Numerische Methoden Praktikum Aufgabe 2
# Milan Wenske 10.05.2022

from matplotlib import pyplot as plt

list_x = [- 1, 0, 1.5, 3, 3.5, 4, 4.5, 6, 7.3]
list_y = [-0.5, 0.5, 1.8, 2, 4, 4.3, 5, 6.8, 7]
a1 = 0  # Startwert
a2 = 0  # Startwert
learning_rate = 0.01


def grad_a1_def(a1, a2, list_x, list_y):
    i = 0
    L = 0
    while i < 9:
        L_temp = -2 * list_x[i] * (list_y[i] - (a1 * list_x[i] + a2))
        L = L + L_temp
        i += 1
    L = L / i
    return L


def grad_a2_def(a1, a2, list_x, list_y):
    i = 0
    L = 0
    while i < 9:
        L_temp = -2 * (list_y[i] - (a1 * list_x[i] + a2))
        L = L + L_temp
        i += 1
    L = L / i
    return L


list_grad_a1 = [1, 2]
list_grad_a2 = [1, 2]
differenz_a1 = 1
differenz_a2 = 2
i = 0

while i < 100 and (differenz_a1 >= 0.001 or differenz_a2 >= 0.001):

    if differenz_a1 >= 0.001:
        list_grad_a1[0] = a1

        grad_a1 = grad_a1_def(a1, a2, list_x, list_y)
        a1 = a1 - (grad_a1 * learning_rate)

        list_grad_a1[1] = a1
        differenz_a1 = abs(list_grad_a1[0] - list_grad_a1[1])

    if differenz_a2 >= 0.001:
        list_grad_a2[0] = a2

        grad_a2 = grad_a2_def(a1, a2, list_x, list_y)
        a2 = a2 - (grad_a2 * learning_rate)

        list_grad_a2[1] = a2
        differenz_a2 = abs(list_grad_a2[0] - list_grad_a2[1])

    i += 1

list_plot_x = []
list_plot_y = []
x = -2
while x <= 8:

    y = a1 * x + a2

    list_plot_x.append(x)
    list_plot_y.append(y)

    x += 1


plt.plot(list_x, list_y)
plt.plot(list_plot_x, list_plot_y)
plt.title("Gradientenabstiegverfahren")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
