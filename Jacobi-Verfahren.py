# Jacobi-Verfahren
# Milan Wenske
# 07.22


A = [[0, 2, -1],
     [-1, 2, -1],
     [0, -1, 2], ]

b = [3, 4, 5]

x = [2, 2, 2]

L = [[0,        0,      0],
     [A[1][0],  0,      0],
     [A[2][0], A[2][1],  0]]


D = [[A[0][0],  0,    0],
     [0, A[1][1],     0],
     [0,    0, A[2][2]]]


R = [[0,     A[0][1], A[0][2]],
     [0,     0,      A[1][2]],
     [0,     0,            0]]




def a_inv(a):  # Inverse von Zahl
    if a != 0:
        x = 0
        x = 1 / a
    else:
        x = 0
    return x

# Inverse von D
a00 = a_inv(A[0][0])
a11 = a_inv(A[1][1])
a22 = a_inv(A[2][2])

D_I = [[a00, 0,   0],
       [0, a11,   0],
       [0,   0, a22]]

# D_I_negativ

a00 = -a_inv(A[0][0])
a11 = -a_inv(A[1][1])
a22 = -a_inv(A[2][2])

D_In = [[a00, 0,   0],
        [0, a11,   0],
        [0,   0, a22]]



def multiply_3x3_3x3(A, B):
    C = [[],[],[]]

    for j in range(0, 3):
        row_a = j
        i = 0
        while i < 3:
            collum_b = 0
            if (i == 1):
                collum_b = 1
            if (i == 2):
                collum_b = 2
            a = A[row_a][0] * B[0][collum_b] + A[row_a][1] * B[1][collum_b] + A[row_a][2] * B[2][collum_b]
            i += 1
            C[j].append(a)

    return C


def multiply_3x3_3x1(A, b):
    C = []

    for j in range(0, 3):
        row_a = j
        a = A[row_a][0] * b[0] + A[row_a][1] * b[1] + A[row_a][2] * b[2]
        C.append(a)
    return C



def add_3x3_3x3(A, B):
    C = [[], [], []]

    for j in range(0, 3):
        i = 0
        while i < 3:
            a = A[j][i] + B[j][i]
            C[j].append(a)
            i += 1
    return C


def add_vector(A, B):
    C = []
    for j in range(0, 3):
        a = A[j] + B[j]
        C.append(a)
    return C


for i in range(0, 50):

    x_n = add_vector(multiply_3x3_3x1(multiply_3x3_3x3(D_In, add_3x3_3x3(L, R)), x), multiply_3x3_3x1(D_I, b))
    x = x_n

    print("Schritt", i, x_n)





